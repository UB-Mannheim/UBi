import datetime
import uuid
import json
from typing import Dict, Optional, List
from chainlit.data import BaseDataLayer
from chainlit import PersistedUser, User
from chainlit.types import Feedback, ThreadDict, Pagination, ThreadFilter, PaginatedResponse, PageInfo
from chainlit.element import ElementDict
from chainlit.step import StepDict
from db import save_interaction


class CustomDataLayer(BaseDataLayer):
    def __init__(self):
        self.users: Dict[str, PersistedUser] = {}
        self.threads: Dict[str, ThreadDict] = {}
        self.elements: Dict[str, ElementDict] = {}
        self.steps: Dict[str, StepDict] = {}
        self.feedback: Dict[str, Feedback] = {}

    async def build_debug_url(self) -> str:
        return ""

    async def get_user(self, identifier: str) -> Optional[PersistedUser]:
        return self.users.get(identifier)

    async def create_user(self, user: User) -> PersistedUser:
        persisted_user = PersistedUser(
            **user.__dict__,
            id=user.identifier,
            createdAt=datetime.datetime.now().date().strftime("%Y-%m-%d")
        )
        self.users[user.identifier] = persisted_user
        return persisted_user

    async def upsert_feedback(self, feedback: Feedback) -> str:
        feedback_id = feedback.id or str(uuid.uuid4())
        step_id = getattr(feedback, "forId", None) or getattr(feedback, "step_id", None)
        question, answer, session_id = "unknown", "unknown", "unknown"

        if step_id and step_id in self.steps:
            step = self.steps[step_id]
            question = step.get("input", "unknown")
            answer = step.get("output", "unknown")
            session_id = step.get("metadata", {}).get("session_id", "unknown")

        await save_interaction(
            session_id=session_id,
            question=question,
            answer=answer,
            feedback=json.dumps({
                "id": feedback_id,
                "step_id": step_id,
                "name": "user_feedback",
                "value": float(getattr(feedback, "value", 0)),
                "comment": getattr(feedback, "comment", ""),
            })
        )

        self.feedback[feedback_id] = feedback
        return feedback_id

    async def delete_feedback(self, feedback_id: str) -> bool:
        return self.feedback.pop(feedback_id, None) is not None

    async def create_element(self, element_dict: ElementDict) -> None:
        self.elements[element_dict["id"]] = element_dict

    async def get_element(self, thread_id: str, element_id: str) -> Optional[ElementDict]:
        return self.elements.get(element_id)

    async def delete_element(self, element_id: str, thread_id: Optional[str] = None) -> None:
        self.elements.pop(element_id, None)

    async def create_step(self, step_dict: StepDict) -> None:
        self.steps[step_dict["id"]] = step_dict

    async def update_step(self, step_dict: StepDict) -> None:
        self.steps[step_dict["id"]] = step_dict

    async def delete_step(self, step_id: str) -> None:
        self.steps.pop(step_id, None)

    async def get_thread_author(self, thread_id: str) -> str:
        return self.threads.get(thread_id, {}).get("userId", "Unknown")

    async def delete_thread(self, thread_id: str) -> None:
        self.threads.pop(thread_id, None)

    async def list_threads(self, pagination: Pagination, filters: ThreadFilter) -> PaginatedResponse[ThreadDict]:
        if not filters.userId:
            raise ValueError("userId is required")

        threads = [t for t in self.threads.values() if t["userId"] == filters.userId]
        start = next((i + 1 for i, t in enumerate(threads) if t["id"] == pagination.cursor), 0)
        end = start + pagination.first
        paginated_threads = threads[start:end] or []

        return PaginatedResponse(
            pageInfo=PageInfo(
                hasNextPage=len(threads) > end,
                startCursor=paginated_threads[0]["id"] if paginated_threads else None,
                endCursor=paginated_threads[-1]["id"] if paginated_threads else None,
            ),
            data=paginated_threads,
        )

    async def get_thread(self, thread_id: str) -> Optional[ThreadDict]:
        thread = self.threads.get(thread_id)
        if thread:
            thread["steps"] = [s for s in self.steps.values() if s["threadId"] == thread_id]
            thread["elements"] = [e for e in self.elements.values() if e["threadId"] == thread_id]
        return thread

    async def update_thread(
        self,
        thread_id: str,
        name: Optional[str] = None,
        user_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
        tags: Optional[List[str]] = None
    ):
        if thread_id in self.threads:
            if name:
                self.threads[thread_id]["name"] = name
            if user_id:
                self.threads[thread_id]["userId"] = user_id
            if metadata:
                self.threads[thread_id]["metadata"] = metadata
            if tags:
                self.threads[thread_id]["tags"] = tags
        else:
            self.threads[thread_id] = {
                "id": thread_id,
                "createdAt": datetime.datetime.now().isoformat() + "Z",
                "name": name or metadata.get("name") if metadata else None,
                "userId": user_id,
                "userIdentifier": user_id,
                "tags": tags,
                "metadata": json.dumps(metadata) if metadata else None,
            }

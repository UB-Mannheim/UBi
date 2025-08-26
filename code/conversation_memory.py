"""
Conversation Memory Module for AIMA
Handles session-based conversation state and context management
"""

import datetime
import uuid
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from config import RATE_LIMIT_CONFIG, SESSION_MEMORY_CONFIG


class MessageRole(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class ConversationTurn:
    """Represents a single turn in the conversation"""

    id: str
    role: MessageRole
    content: str
    timestamp: datetime.datetime
    metadata: Optional[Dict[str, Any]] = None
    tokens_used: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            **asdict(self),
            "role": self.role.value,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ConversationTurn":
        data["role"] = MessageRole(data["role"])
        data["timestamp"] = datetime.datetime.fromisoformat(data["timestamp"])
        return cls(**data)


@dataclass
class SessionContext:
    """Represents the current session context"""

    session_id: str
    topic: Optional[str] = None
    intent: Optional[str] = None
    entities: Optional[Dict[str, Any]] = None
    created_at: datetime.datetime = None
    # Rate limiting fields
    total_chars: int = 0
    total_turns: int = 0
    request_timestamps: Optional[List[datetime.datetime]] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()
        if self.request_timestamps is None:
            self.request_timestamps = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            **asdict(self),
            "created_at": self.created_at.isoformat(),
            "request_timestamps": (
                [ts.isoformat() for ts in self.request_timestamps]
                if self.request_timestamps
                else []
            ),
        }


class SessionMemory:
    """
    Manages session-based conversation memory
    Memory is cleared when session ends or new chat starts
    """

    def __init__(
        self,
        max_turns: int = 10,
        max_tokens: int = 4000,
        context_window: int = 5,
        # Rate limiting configuration
        max_chars_per_request: int = 500,
        max_chars_per_session: int = 5000,
        max_turns_per_session: int = 24,
        max_requests_per_minute: int = 12,
        rate_limit_window: int = 60,
    ):
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.context_window = context_window

        # Rate limiting configuration
        self.max_chars_per_request = max_chars_per_request
        self.max_chars_per_session = max_chars_per_session
        self.max_turns_per_session = max_turns_per_session
        self.max_requests_per_minute = max_requests_per_minute
        self.rate_limit_window = rate_limit_window

        # Session storage (cleared when session ends)
        self.sessions: Dict[str, List[ConversationTurn]] = {}
        self.contexts: Dict[str, SessionContext] = {}

    def create_session(self, session_id: str) -> str:
        """Create a new conversation session"""
        if session_id not in self.sessions:
            self.sessions[session_id] = []
            self.contexts[session_id] = SessionContext(session_id=session_id)
        return session_id

    def add_turn(
        self,
        session_id: str,
        role: MessageRole,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        tokens_used: Optional[int] = None,
    ) -> str:
        """Add a new turn to the conversation"""
        if session_id not in self.sessions:
            self.create_session(session_id)

        turn_id = str(uuid.uuid4())
        turn = ConversationTurn(
            id=turn_id,
            role=role,
            content=content,
            timestamp=datetime.datetime.now(),
            metadata=metadata or {},
            tokens_used=tokens_used,
        )

        self.sessions[session_id].append(turn)

        # Maintain conversation length limits
        self._trim_conversation(session_id)

        return turn_id

    def get_conversation_history(
        self,
        session_id: str,
        include_system: bool = False,
        max_turns: Optional[int] = None,
    ) -> List[ConversationTurn]:
        """Get conversation history for a session"""
        if session_id not in self.sessions:
            return []

        turns = self.sessions[session_id]

        # Filter by role if needed
        if not include_system:
            turns = [turn for turn in turns if turn.role != MessageRole.SYSTEM]

        # Apply turn limit
        if max_turns:
            turns = turns[-max_turns:]

        return turns

    def get_context_window(
        self, session_id: str, window_size: Optional[int] = None
    ) -> List[ConversationTurn]:
        """Get recent conversation context for RAG enhancement"""
        if session_id not in self.sessions:
            return []

        size = window_size or self.context_window
        return self.sessions[session_id][-size:]

    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get a summary of the session"""
        if session_id not in self.sessions:
            return {}

        turns = self.sessions[session_id]
        context = self.contexts.get(session_id)

        return {
            "session_id": session_id,
            "total_turns": len(turns),
            "user_turns": len(
                [t for t in turns if t.role == MessageRole.USER]
            ),
            "assistant_turns": len(
                [t for t in turns if t.role == MessageRole.ASSISTANT]
            ),
            "start_time": turns[0].timestamp if turns else None,
            "last_activity": turns[-1].timestamp if turns else None,
            "context": context.to_dict() if context else None,
            "estimated_tokens": sum(t.tokens_used or 0 for t in turns),
        }

    def update_context(self, session_id: str, **kwargs) -> None:
        """Update session context"""
        if session_id not in self.contexts:
            self.create_session(session_id)

        context = self.contexts[session_id]
        for key, value in kwargs.items():
            if hasattr(context, key):
                setattr(context, key, value)

    def clear_session(self, session_id: str) -> None:
        """Clear session memory (called when new chat starts)"""
        if session_id in self.sessions:
            self.sessions[session_id] = []
        if session_id in self.contexts:
            self.contexts[session_id] = SessionContext(session_id=session_id)

    def end_session(self, session_id: str) -> None:
        """End session and clear all memory"""
        if session_id in self.sessions:
            del self.sessions[session_id]
        if session_id in self.contexts:
            del self.contexts[session_id]

    def _trim_conversation(self, session_id: str) -> None:
        """Trim conversation to maintain limits"""
        if session_id not in self.sessions:
            return

        turns = self.sessions[session_id]

        # Trim by turn count
        if len(turns) > self.max_turns:
            self.sessions[session_id] = turns[-self.max_turns :]

        # Trim by token count (if tokens are tracked)
        total_tokens = sum(t.tokens_used or 0 for t in turns)
        if total_tokens > self.max_tokens:
            # Remove oldest turns until under token limit
            while turns and total_tokens > self.max_tokens:
                removed_turn = turns.pop(0)
                total_tokens -= removed_turn.tokens_used or 0

    def session_exists(self, session_id: str) -> bool:
        """Check if session exists"""
        return session_id in self.sessions

    def get_active_sessions(self) -> List[str]:
        """Get list of active session IDs"""
        return list(self.sessions.keys())

    def check_rate_limits(
        self, session_id: str, user_input: str
    ) -> tuple[bool, Optional[str]]:
        """
        Check all rate limits for a request

        Returns:
            Tuple of (allowed: bool, error_message: Optional[str])
        """
        # Initialize session if not exists
        if session_id not in self.contexts:
            self.create_session(session_id)

        context = self.contexts[session_id]

        # Check character limit per request
        if len(user_input) > self.max_chars_per_request:
            msg = (
                f"Sie haben die maximale Anzahl an Zeichen pro "
                f"Anfrage erreicht ({self.max_chars_per_request} "
                f"Zeichen)."
            )
            return False, msg

        # Check character limit per session
        current_session_chars = context.total_chars + len(user_input)
        if current_session_chars > self.max_chars_per_session:
            msg = (
                f"Sie haben die maximale Anzahl an Zeichen in "
                f"dieser Session erreicht ({self.max_chars_per_session} "
                f"Zeichen)."
            )
            return False, msg

        # Check turn limit per session
        if context.total_turns >= self.max_turns_per_session:
            msg = (
                f"Sie haben die maximale Anzahl an Anfragen für "
                f"diese Session erreicht ({self.max_turns_per_session} "
                f"Anfragen)."
            )
            return False, msg

        # Check rate limiting (requests per minute)
        current_time = datetime.datetime.now()

        # Remove timestamps older than the window
        while (
            context.request_timestamps
            and (current_time - context.request_timestamps[0]).total_seconds()
            > self.rate_limit_window
        ):
            context.request_timestamps.pop(0)

        # Check if we're over the limit
        if len(context.request_timestamps) >= self.max_requests_per_minute:
            return False, (
                "Zu viele Anfragen. Bitte warten Sie eine Minute, "
                "bevor Sie weitere Anfragen senden."
            )

        return True, None

    def record_request(self, session_id: str, user_input: str) -> None:
        """Record a successful request for rate limiting"""
        if session_id not in self.contexts:
            self.create_session(session_id)

        context = self.contexts[session_id]

        # Update character count
        context.total_chars += len(user_input)

        # Update turn count
        context.total_turns += 1

        # Record timestamp for rate limiting
        context.request_timestamps.append(datetime.datetime.now())

    def get_rate_limit_stats(self, session_id: str) -> Dict[str, Any]:
        """Get rate limiting statistics for a session"""
        if session_id not in self.contexts:
            return {}

        context = self.contexts[session_id]
        current_time = datetime.datetime.now()

        # Calculate session duration
        session_duration = (current_time - context.created_at).total_seconds()

        # Calculate percentages
        chars_percent = (
            context.total_chars / self.max_chars_per_session
        ) * 100
        turns_percent = (
            context.total_turns / self.max_turns_per_session
        ) * 100

        # Count recent requests
        recent_requests = 0
        for timestamp in context.request_timestamps:
            if (
                current_time - timestamp
            ).total_seconds() <= self.rate_limit_window:
                recent_requests += 1

        return {
            "session_id": session_id,
            "chars_used": context.total_chars,
            "chars_remaining": max(
                0, self.max_chars_per_session - context.total_chars
            ),
            "chars_percent": chars_percent,
            "turns_used": context.total_turns,
            "turns_remaining": max(
                0, self.max_turns_per_session - context.total_turns
            ),
            "turns_percent": turns_percent,
            "session_duration_seconds": session_duration,
            "requests_in_last_minute": recent_requests,
            "max_requests_per_minute": self.max_requests_per_minute,
            "rate_limit_percent": (
                recent_requests / self.max_requests_per_minute
            )
            * 100,
        }


# Global session memory instance
session_memory = SessionMemory(
    max_turns=SESSION_MEMORY_CONFIG["max_turns"],
    max_tokens=SESSION_MEMORY_CONFIG["max_tokens"],
    context_window=SESSION_MEMORY_CONFIG["context_window"],
    max_chars_per_request=RATE_LIMIT_CONFIG["max_chars_per_request"],
    max_chars_per_session=RATE_LIMIT_CONFIG["max_chars_per_session"],
    max_turns_per_session=RATE_LIMIT_CONFIG["max_turns_per_session"],
    max_requests_per_minute=RATE_LIMIT_CONFIG["max_requests_per_minute"],
    rate_limit_window=RATE_LIMIT_CONFIG["rate_limit_window"],
)


def create_conversation_context(session_id: str) -> List[Dict[str, str]]:
    """
    Create conversation context from recent turns and return the context
    as a list of message dictionaries.

    Return Example:
    [
        {'role': 'user', 'content': 'Query 1'},
        {'role': 'assistant', 'content': 'Response 1'},
        {'role': 'user', 'content': 'Query 2'},
        {'role': 'assistant', 'content': 'Response 2'},
        ...
    ]
    """
    recent_turns = session_memory.get_context_window(session_id)

    if not recent_turns:
        return []

    context_messages = []
    for turn in recent_turns:
        # Convert MessageRole enum to string format expected by the API
        role = turn.role.value  # This will be "user", "assistant", or "system"
        context_messages.append({"role": role, "content": turn.content})

    return context_messages

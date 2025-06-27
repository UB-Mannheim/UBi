"""
Conversation Memory Module for AIMA
Handles session-based conversation state and context management
"""

import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


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
            'role': self.role.value,
            'timestamp': self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversationTurn':
        data['role'] = MessageRole(data['role'])
        data['timestamp'] = datetime.datetime.fromisoformat(
            data['timestamp']
        )
        return cls(**data)


@dataclass
class SessionContext:
    """Represents the current session context"""
    session_id: str
    topic: Optional[str] = None
    intent: Optional[str] = None
    entities: Optional[Dict[str, Any]] = None
    created_at: datetime.datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            **asdict(self),
            'created_at': self.created_at.isoformat()
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
        context_window: int = 5
    ):
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.context_window = context_window
        
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
        tokens_used: Optional[int] = None
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
            tokens_used=tokens_used
        )
        
        self.sessions[session_id].append(turn)
        
        # Maintain conversation length limits
        self._trim_conversation(session_id)
        
        return turn_id
    
    def get_conversation_history(
        self,
        session_id: str,
        include_system: bool = False,
        max_turns: Optional[int] = None
    ) -> List[ConversationTurn]:
        """Get conversation history for a session"""
        if session_id not in self.sessions:
            return []
        
        turns = self.sessions[session_id]
        
        # Filter by role if needed
        if not include_system:
            turns = [
                turn for turn in turns 
                if turn.role != MessageRole.SYSTEM
            ]
        
        # Apply turn limit
        if max_turns:
            turns = turns[-max_turns:]
        
        return turns
    
    def get_context_window(
        self,
        session_id: str,
        window_size: Optional[int] = None
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
            "estimated_tokens": sum(t.tokens_used or 0 for t in turns)
        }
    
    def update_context(
        self,
        session_id: str,
        **kwargs
    ) -> None:
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
            self.sessions[session_id] = turns[-self.max_turns:]
        
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


# Global session memory instance
session_memory = SessionMemory() 


def create_conversation_context(session_id: str) -> str:
    """Create conversation context from recent turns"""
    recent_turns = session_memory.get_context_window(session_id)
    
    if not recent_turns:
        return ""
    
    context_lines = []
    for turn in recent_turns:
        role = "Nutzer" if turn.role == MessageRole.USER else "Assistent"
        context_lines.append(f"{role}: {turn.content}")
    
    return "\n".join(context_lines) 
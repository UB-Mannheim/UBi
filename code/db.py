import aiosqlite
import datetime
from config import DB_PATH

# Global flag to track if table has been created
_table_created = False


async def _ensure_table_exists(db):
    """Ensure the chat_interactions table exists with proper indexes."""
    global _table_created
    if _table_created:
        return
        
    await db.execute(
        """CREATE TABLE IF NOT EXISTS chat_interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            feedback TEXT
        )"""
    )
    
    # Create indexes for better performance
    await db.execute(
        """CREATE INDEX IF NOT EXISTS idx_session_question 
           ON chat_interactions(session_id, question)"""
    )
    await db.execute(
        """CREATE INDEX IF NOT EXISTS idx_timestamp 
           ON chat_interactions(timestamp)"""
    )
    
    _table_created = True


async def save_interaction(session_id: str, question: str, answer: str, feedback: str = None):
    """
    Saves a chat interaction to the database.
    
    If feedback is provided, it updates the most recent interaction
    for the given session_id and question.
    Otherwise, it inserts a new interaction record.
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    
    async with aiosqlite.connect(DB_PATH) as db:
        await _ensure_table_exists(db)

        if feedback:
            # Try to update the most recent interaction for this session/question
            result = await db.execute(
                """UPDATE chat_interactions 
                   SET feedback = ? 
                   WHERE id = (
                       SELECT MAX(id) 
                       FROM chat_interactions 
                       WHERE session_id = ? AND question = ?
                   )""",
                (feedback, session_id, question),
            )
            
            # If no rows were updated, insert a new record
            if result.rowcount == 0:
                await db.execute(
                    """INSERT INTO chat_interactions 
                       (session_id, question, answer, timestamp, feedback)
                       VALUES (?, ?, ?, ?, ?)""",
                    (session_id, question, answer, timestamp, feedback),
                )
        else:
            # Insert new interaction record
            await db.execute(
                """INSERT INTO chat_interactions 
                   (session_id, question, answer, timestamp, feedback)
                   VALUES (?, ?, ?, ?, ?)""",
                (session_id, question, answer, timestamp, None),
            )

        await db.commit()

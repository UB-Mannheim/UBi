import aiosqlite
import datetime
from config import DB_PATH

async def save_interaction(session_id: str, question: str, answer: str, feedback: str = None):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """CREATE TABLE IF NOT EXISTS chat_interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                question TEXT,
                answer TEXT,
                timestamp TEXT,
                feedback TEXT
            )"""
        )
        await db.execute(
            """INSERT INTO chat_interactions (session_id, question, answer, timestamp, feedback)
               VALUES (?, ?, ?, ?, ?)""",
            (session_id, question, answer, datetime.datetime.utcnow().isoformat(), feedback)
        )
        await db.commit()

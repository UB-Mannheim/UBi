"""
Session Statistics Module for AIMA
Provides user-friendly session statistics and usage information
"""

from typing import Dict, Optional
from conversation_memory import session_memory


def get_session_usage_message(session_id: str) -> str:
    """
    Get a user-friendly message showing current session usage

    Args:
        session_id: The session ID to get stats for

    Returns:
        Formatted message with usage statistics
    """
    stats = session_memory.get_rate_limit_stats(session_id)

    if not stats:
        return "Keine Session-Informationen verfügbar."

    # Create progress bars
    chars_bar = _create_progress_bar(stats["chars_percent"], 20)
    turns_bar = _create_progress_bar(stats["turns_percent"], 20)

    message = f"""📊 **Session-Statistiken**

**Zeichen-Nutzung:**
{chars_bar} {stats['chars_used']}/{session_memory.max_chars_per_session} ({stats['chars_percent']:.1f}%)
Verbleibend: {stats['chars_remaining']} Zeichen

**Anfragen-Nutzung:**
{turns_bar} {stats['turns_used']}/{session_memory.max_turns_per_session} ({stats['turns_percent']:.1f}%)
Verbleibend: {stats['turns_remaining']} Anfragen

**Rate Limiting:**
Anfragen in der letzten Minute: {stats['requests_in_last_minute']}/{stats['max_requests_per_minute']}

**Session-Dauer:**
{_format_duration(stats['session_duration_seconds'])}"""

    return message


def _create_progress_bar(percentage: float, width: int = 20) -> str:
    """Create a simple text-based progress bar"""
    filled = int((percentage / 100) * width)
    empty = width - filled

    bar = "█" * filled + "░" * empty
    return f"[{bar}]"


def _format_duration(seconds: float) -> str:
    """Format duration in a human-readable way"""
    if seconds < 60:
        return f"{int(seconds)} Sekunden"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes} Minuten, {secs} Sekunden"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours} Stunden, {minutes} Minuten"


def check_session_warnings(session_id: str) -> Optional[str]:
    """
    Check if session is approaching limits and return warning if needed

    Args:
        session_id: The session ID to check

    Returns:
        Warning message if approaching limits, None otherwise
    """
    stats = session_memory.get_rate_limit_stats(session_id)

    if not stats:
        return None

    warnings = []

    # Check character usage (warn at 80%)
    if stats["chars_percent"] >= 80:
        warnings.append(f"⚠️ Sie haben {stats['chars_percent']:.1f}% "
                       f"Ihres Zeichen-Limits erreicht.")

    # Check turn usage (warn at 80%)
    if stats["turns_percent"] >= 80:
        warnings.append(f"⚠️ Sie haben {stats['turns_percent']:.1f}% "
                       f"Ihres Anfragen-Limits erreicht.")

    # Check rate limiting (warn at 80%)
    if stats["rate_limit_percent"] >= 80:
        warnings.append("⚠️ Sie nähern sich dem Rate-Limit für "
                       "Anfragen pro Minute.")

    if warnings:
        return "\n".join(warnings)

    return None

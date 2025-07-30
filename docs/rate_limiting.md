# Rate Limiting and Session Management

## Overview

AIMA now includes comprehensive rate limiting and session management features to prevent abuse and ensure fair usage of the system.

## Features

### 1. Character Limits

- **Per Request**: Maximum 500 characters per individual message
- **Per Session**: Maximum 5,000 characters total per session

### 2. Turn Limits

- **Per Session**: Maximum 24 conversation turns per session

### 3. Rate Limiting

- **Requests per Minute**: Maximum 12 requests per minute per session
- **Sliding Window**: Uses a 60-second sliding window for rate limiting

## Error Messages

When limits are exceeded, users receive clear German error messages:

- **Character limit per request**: "Sie haben die maximale Anzahl an Zeichen pro Anfrage erreicht (2000 Zeichen)."
- **Character limit per session**: "Sie haben die maximale Anzahl an Zeichen in dieser Session erreicht (20000 Zeichen)."
- **Turn limit per session**: "Sie haben die maximale Anzahl an Anfragen für diese Session erreicht (20 Anfragen)."
- **Rate limit**: "Zu viele Anfragen. Bitte warten Sie eine Minute, bevor Sie weitere Anfragen senden."

## Session Statistics

Users can check their current usage by typing:
- `session stats`

This displays:
- Character usage with progress bar
- Turn usage with progress bar
- Rate limiting status
- Session duration
- Remaining limits

## Configuration

All limits can be configured in `code/config.py`:

```python
RATE_LIMIT_CONFIG = {
    "max_chars_per_request": 500,    # Maximum characters per request
    "max_chars_per_session": 5000,   # Maximum characters per session
    "max_turns_per_session": 24,      # Maximum turns per session
    "max_requests_per_minute": 12,    # Maximum requests per minute
    "rate_limit_window": 60,          # Rate limit window in seconds
}
```

## Security Benefits

1. **Bot Protection**: Rate limiting prevents automated bots from overwhelming the system
2. **Resource Management**: Character and turn limits prevent excessive resource usage
3. **Fair Usage**: Ensures all users have equal access to the system
4. **Cost Control**: Limits help control API costs and system resources

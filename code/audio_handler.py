from __future__ import annotations

import io
import os
import tempfile
import wave
from pathlib import Path
from typing import Optional

import numpy as np
from dotenv import load_dotenv

from config import ENV_PATH
from utils import print_err, print_info


# === .env Configuration ===
load_dotenv(ENV_PATH)

_enable_audio_input = os.getenv("ENABLE_AUDIO_INPUT", "False").lower() == "true"
_enable_audio_output = os.getenv("ENABLE_AUDIO_OUTPUT", "False").lower() == "true"
_whisper_model_size = os.getenv("WHISPER_MODEL", "base")
_whisper_device = os.getenv("WHISPER_DEVICE", "cpu")
_tts_language = os.getenv("TTS_LANGUAGE", "de")
_tts_speaker = os.getenv("TTS_SPEAKER", "random")
_tts_sample_rate = int(os.getenv("TTS_SAMPLE_RATE", "48000"))


# === Lazy-loaded model references ===
_whisper_model = None
_tts_model = None


# === Whisper Model ===
def initialize_whisper_model():
    """
    Lazy-load the Faster-Whisper model.

    Returns the loaded WhisperModel instance, or None if unavailable.
    """
    global _whisper_model
    if _whisper_model is not None:
        return _whisper_model
    try:
        from faster_whisper import WhisperModel

        print_info(
            f"[bold]🎙️ Loading Whisper model '{_whisper_model_size}' "
            f"on {_whisper_device}..."
        )
        _whisper_model = WhisperModel(
            _whisper_model_size, device=_whisper_device, compute_type="int8"
        )
        print_info("[bold]✅ Whisper model loaded.")
        return _whisper_model
    except ImportError:
        print_err(
            "[bold red]❌ faster-whisper is not installed. "
            "Run: pip install faster-whisper~=1.0.0"
        )
        return None
    except Exception as e:
        print_err(f"[bold red]❌ Failed to load Whisper model: {e}")
        return None


# === Silero TTS Model ===
def initialize_tts():
    """
    Lazy-load the Silero TTS model via torch hub.

    The language is specified via the TTS_LANGUAGE environment variable.
    Models are downloaded automatically on first use (~30 MB).

    Returns the loaded Silero model, or None if unavailable.
    """
    global _tts_model
    if _tts_model is not None:
        return _tts_model
    try:
        import torch

        print_info(
            f"[bold]🔊 Loading Silero TTS model for language '{_tts_language}'..."
        )
        model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_tts",
            language=_tts_language,
            speaker="v3_de" if _tts_language == "de" else "v3_en",
        )
        _tts_model = model
        print_info("[bold]✅ Silero TTS model loaded.")
        return _tts_model
    except ImportError as e:
        print_err(
            f"[bold red]❌ Required TTS dependencies not installed: {e}\n"
            "Run: pip install torch soundfile"
        )
        return None
    except Exception as e:
        print_err(f"[bold red]❌ Failed to load Silero TTS: {e}")
        return None


# === Speech-to-Text ===
def transcribe_audio(
    audio_data: bytes,
    mime_type: str = "audio/wav",
    language: Optional[str] = None,
) -> Optional[str]:
    """
    Transcribe audio bytes to text using Faster-Whisper.

    Args:
        audio_data: Raw audio bytes.
        mime_type:  MIME type of the audio (e.g. "audio/wav", "audio/webm", "pcm16").
        language:   ISO language code hint (e.g. "de", "en"), or None for
                    automatic detection.

    Returns:
        Transcribed text string, or None on failure / empty result.
    """
    import struct
    import wave

    model = initialize_whisper_model()
    if model is None:
        return None

    tmp_path = None
    try:
        # Handle raw PCM16 data by creating proper WAV file
        if mime_type == "pcm16" or "pcm" in mime_type.lower():
            # Create a proper WAV file from raw PCM16 data
            # Chainlit uses 44100 Hz sample rate for browser audio
            sample_rate = 44100
            channels = 1
            sample_width = 2  # 16-bit = 2 bytes

            tmp_path = tempfile.mktemp(suffix=".wav")

            with wave.open(tmp_path, 'wb') as wav_file:
                wav_file.setnchannels(channels)
                wav_file.setsampwidth(sample_width)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(audio_data)
        else:
            # For other formats, write as-is
            if "webm" in mime_type or "ogg" in mime_type:
                ext = ".webm"
            elif "mp4" in mime_type or "m4a" in mime_type:
                ext = ".m4a"
            elif "mp3" in mime_type:
                ext = ".mp3"
            else:
                ext = ".wav"

            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp.write(audio_data)
                tmp_path = tmp.name

        # Transcribe with Whisper
        segments, info = model.transcribe(
            tmp_path,
            language=language,
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )

        text = " ".join(seg.text for seg in segments).strip()
        detected_lang = info.language

        if text:
            print_info(f"[bold]🎙️ Transcribed ({detected_lang}): {text}")
            return text
        else:
            print_err("[bold yellow]⚠️ No speech detected in audio")
            return None

    except Exception as e:
        print_err(f"[bold red]❌ Transcription error: {e}")
        print_err(f"[bold red]   Audio data size: {len(audio_data)} bytes")
        print_err(f"[bold red]   MIME type: {mime_type}")
        return None
    finally:
        if tmp_path and Path(tmp_path).exists():
            Path(tmp_path).unlink(missing_ok=True)


# === Text-to-Speech ===
def generate_speech(
    text: str,
    language: str = "German",
    voice: Optional[str] = None,
) -> Optional[bytes]:
    """
    Generate WAV audio from text using Silero TTS.

    Args:
        text:     Text to synthesize.
        language: Detected language (e.g. "German", "English").
        voice:    Optional speaker name override.

    Returns:
        WAV audio bytes, or None on failure.
    """
    tts_model = initialize_tts()
    if tts_model is None:
        return None

    try:
        # Select speaker: honour override, then fall back to configured default
        speaker = voice or _tts_speaker

        # Generate audio tensor
        audio = tts_model.apply_tts(
            text=text,
            speaker=speaker,
            sample_rate=_tts_sample_rate,
        )

        # Convert tensor to numpy array and write WAV bytes
        audio_np = audio.cpu().numpy()
        audio_int16 = (audio_np * 32767).astype(np.int16)

        audio_buffer = io.BytesIO()
        with wave.open(audio_buffer, "wb") as wav_file:
            wav_file.setnchannels(1)   # Mono
            wav_file.setsampwidth(2)   # 16-bit
            wav_file.setframerate(_tts_sample_rate)
            wav_file.writeframes(audio_int16.tobytes())

        return audio_buffer.getvalue()
    except Exception as e:
        print_err(f"[bold red]❌ TTS generation error: {e}")
        return None


# === Feature Flags ===
def is_audio_input_enabled() -> bool:
    """Return True if audio input (speech-to-text) is enabled."""
    return _enable_audio_input


def is_audio_output_enabled() -> bool:
    """Return True if audio output (text-to-speech) is enabled."""
    return _enable_audio_output

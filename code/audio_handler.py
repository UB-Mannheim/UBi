from __future__ import annotations

import io
import os
import tempfile
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from config import ENV_PATH
from utils import print_err, print_info


# === .env Configuration ===
load_dotenv(ENV_PATH)

_enable_audio_input = os.getenv("ENABLE_AUDIO_INPUT", "False").lower() == "true"
_enable_audio_output = os.getenv("ENABLE_AUDIO_OUTPUT", "False").lower() == "true"
_whisper_model_size = os.getenv("WHISPER_MODEL", "base")
_whisper_device = os.getenv("WHISPER_DEVICE", "cpu")
_piper_voice = os.getenv("PIPER_VOICE", "de_DE-thorsten-high")
_piper_voice_dir = os.getenv("PIPER_VOICE_DIR", ".")


# === Lazy-loaded model references ===
_whisper_model = None
_piper_voice_model = None


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


# === Piper TTS Model ===
def initialize_piper():
    """
    Lazy-load the Piper TTS voice model.

    The voice model file is looked up as:
        {PIPER_VOICE_DIR}/{PIPER_VOICE}.onnx  (+ optional .onnx.json config)

    Returns the loaded PiperVoice instance, or None if unavailable.
    """
    global _piper_voice_model
    if _piper_voice_model is not None:
        return _piper_voice_model
    try:
        from piper.voice import PiperVoice

        voice_dir = Path(_piper_voice_dir)
        voice_path = voice_dir / f"{_piper_voice}.onnx"
        config_path = voice_dir / f"{_piper_voice}.onnx.json"

        if not voice_path.exists():
            print_err(
                f"[bold red]❌ Piper voice model not found: {voice_path}\n"
                "   Download models from: "
                "https://github.com/rhasspy/piper/blob/master/VOICES.md"
            )
            return None

        config_arg = str(config_path) if config_path.exists() else None
        print_info(f"[bold]🔊 Loading Piper TTS voice '{_piper_voice}'...")
        _piper_voice_model = PiperVoice.load(
            str(voice_path), config_path=config_arg
        )
        print_info("[bold]✅ Piper TTS voice loaded.")
        return _piper_voice_model
    except ImportError:
        print_err(
            "[bold red]❌ piper-tts is not installed. "
            "Run: pip install piper-tts~=1.2.0"
        )
        return None
    except Exception as e:
        print_err(f"[bold red]❌ Failed to load Piper TTS: {e}")
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
        mime_type:  MIME type of the audio (e.g. "audio/wav", "audio/webm").
        language:   ISO language code hint (e.g. "de", "en"), or None for
                    automatic detection.

    Returns:
        Transcribed text string, or None on failure / empty result.
    """
    model = initialize_whisper_model()
    if model is None:
        return None

    # Determine file extension from MIME type
    ext = ".wav"
    for fragment, suffix in (
        ("webm", ".webm"),
        ("ogg", ".ogg"),
        ("mp3", ".mp3"),
        ("mp4", ".mp4"),
        ("m4a", ".m4a"),
    ):
        if fragment in mime_type:
            ext = suffix
            break

    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
            tmp.write(audio_data)
            tmp_path = tmp.name

        segments, info = model.transcribe(
            tmp_path, language=language, beam_size=5
        )
        text = " ".join(seg.text for seg in segments).strip()
        detected_lang = info.language
        print_info(f"[bold]🎙️ Transcribed ({detected_lang}): {text}")
        return text or None
    except Exception as e:
        print_err(f"[bold red]❌ Transcription error: {e}")
        return None
    finally:
        if tmp_path:
            Path(tmp_path).unlink(missing_ok=True)


# === Text-to-Speech ===
def generate_speech(
    text: str,
    language: str = "German",
    voice: Optional[str] = None,
) -> Optional[bytes]:
    """
    Generate WAV audio from text using Piper TTS.

    Args:
        text:     Text to synthesize.
        language: Detected language (e.g. "German", "English").  Currently
                  used for informational purposes; the active voice is
                  configured via PIPER_VOICE in .env.
        voice:    Unused placeholder for future per-language voice selection.

    Returns:
        WAV audio bytes, or None on failure.
    """
    import wave

    piper_model = initialize_piper()
    if piper_model is None:
        return None
    try:
        audio_buffer = io.BytesIO()
        with wave.open(audio_buffer, "wb") as wav_file:
            piper_model.synthesize(text, wav_file)
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

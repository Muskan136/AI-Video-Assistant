import os
import subprocess
import requests

SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SARVAM_STT_TRANSLATE_URL = "https://api.sarvam.ai/speech-to-text-translate"
SARVAM_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

SARVAM_PIECE_SECONDS = 25


def split_audio(chunk_path):
    piece_length = SARVAM_PIECE_SECONDS

    output_pattern = chunk_path.replace(".wav", "_piece_%03d.wav")

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            chunk_path,
            "-f",
            "segment",
            "-segment_time",
            str(piece_length),
            "-c",
            "copy",
            output_pattern,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    pieces = []

    i = 0
    while True:
        piece = chunk_path.replace(".wav", f"_piece_{i:03d}.wav")
        if not os.path.exists(piece):
            break
        pieces.append(piece)
        i += 1

    return pieces


def _send_to_sarvam(piece_path):
    headers = {
        "api-subscription-key": SARVAM_API_KEY
    }

    with open(piece_path, "rb") as f:
        files = {
            "file": (os.path.basename(piece_path), f, "audio/wav")
        }

        data = {
            "model": SARVAM_MODEL,
            "with_diarization": "false"
        }

        response = requests.post(
            SARVAM_STT_TRANSLATE_URL,
            headers=headers,
            files=files,
            data=data,
            timeout=120,
        )

    response.raise_for_status()

    return response.json().get("transcript", "")


def transcribe_chunk(chunk_path, language="english"):

    if not SARVAM_API_KEY:
        raise RuntimeError("SARVAM_API_KEY not found.")

    pieces = split_audio(chunk_path)

    transcript = ""

    for i, piece in enumerate(pieces):
        print(f"Processing piece {i+1}/{len(pieces)}")

        transcript += _send_to_sarvam(piece) + " "

        os.remove(piece)

    return transcript.strip()


def transcribe_all(chunks, language="english"):

    transcript = ""

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}/{len(chunks)}")

        transcript += transcribe_chunk(chunk, language) + " "

    return transcript.strip()
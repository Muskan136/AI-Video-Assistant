import os
import subprocess
import yt_dlp
import ffmpeg

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    base = os.path.splitext(filename)[0]
    return base + ".wav"


def convert_to_wav(input_path: str) -> str:
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    (
        ffmpeg
        .input(input_path)
        .output(
            output_path,
            ac=1,
            ar=16000,
            format="wav"
        )
        .overwrite_output()
        .run(quiet=True)
    )

    return output_path


def get_audio_duration(file_path: str) -> float:
    probe = ffmpeg.probe(file_path)
    return float(probe["format"]["duration"])


def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:
    duration = get_audio_duration(wav_path)

    chunk_seconds = chunk_minutes * 60

    chunks = []

    start = 0
    index = 0

    while start < duration:
        chunk_path = f"{os.path.splitext(wav_path)[0]}_chunk_{index}.wav"

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                wav_path,
                "-ss",
                str(start),
                "-t",
                str(chunk_seconds),
                "-ac",
                "1",
                "-ar",
                "16000",
                chunk_path,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )

        chunks.append(chunk_path)

        start += chunk_seconds
        index += 1

    return chunks


def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected YouTube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)

    print(f"Audio ready — {len(chunks)} chunk(s) created.")

    return chunks
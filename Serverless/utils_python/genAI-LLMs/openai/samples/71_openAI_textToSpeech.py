
# https://platform.openai.com/
# https://platform.openai.com/docs/
# https://platform.openai.com/docs/guides/text-to-speech

from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key="<YOUR_OpenAI_API_KEY>",
    api_base="https://api.openai.com/v1",
)
speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone."
) as response:
    response.stream_to_file(speech_file_path)
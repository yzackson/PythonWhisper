# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from dotenv import load_dotenv
import os

load_dotenv()

audio_file= open("./audio.mp3", "rb")
openai.api_key = os.environ['api_key']
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
input()

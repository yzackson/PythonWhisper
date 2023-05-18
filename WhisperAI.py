# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
#from pydub import AudioSegment

#ogg_version = AudioSegment.from_ogg("audio.ogg")
#ogg_version.export("audio.mp3", format="mp3")

audio_file= open("./audio.mp3", "rb")
openai.api_key = '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'
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)
input()

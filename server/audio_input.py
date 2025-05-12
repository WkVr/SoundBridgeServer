import pyaudio
from .config import RATE, CHUNK, FORMAT, CHANNELS

def get_audio_stream():
    audio = pyaudio.PyAudio()
    return audio.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

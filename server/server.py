import asyncio
import time
import websockets
from .audio_input import get_audio_stream
from .config import CHUNK

async def stream_audio(websocket):
    stream = get_audio_stream()
    while True:
        data = stream.read(CHUNK)
        await websocket.send(data)

async def run_server(host="0.0.0.0", port=8080):
    async with websockets.serve(stream_audio, host, port):
        print(f"Server running on ws://{host}:{port}")
        await asyncio.Future()  # Run forever

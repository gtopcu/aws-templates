# pip install websockets

import asyncio
import websockets
import json
from datetime import datetime, timezone

async def connect_and_send():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send a chat message
        message = {"type": "chat", "user": "TestUser", "message": "Hello, World!"}
        await websocket.send(json.dumps(message))

        # Receive response
        while True:
            response = await websocket.recv()
            print(f"Received: {response}")


if __name__ == "__main__":
    asyncio.run(connect_and_send())



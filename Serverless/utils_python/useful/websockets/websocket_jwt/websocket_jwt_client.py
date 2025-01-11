# websocket_client.py

import asyncio
import websockets
import json
import aiohttp


async def get_token():
    """Get JWT token from the authentication endpoint"""
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8080/token") as response:
            return await response.text()


async def connect_and_send():
    # First get the authentication token
    token = await get_token()

    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send authentication
        await websocket.send(f"Bearer {token}")

        # Send a chat message
        message = {"type": "chat", "user": "TestUser", "message": "Hello, World!"}
        await websocket.send(json.dumps(message))

        # Receive response
        try:
            while True:
                response = await websocket.recv()
                print(f"Received: {response}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")


if __name__ == "__main__":
    asyncio.run(connect_and_send())

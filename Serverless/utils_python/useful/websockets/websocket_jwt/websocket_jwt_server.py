# websocket_server.py

# pip install websockets jwt
# pip install websockets python-jwt aiohttp

import asyncio
import websockets
import jwt
import os
from datetime import datetime, timedelta

# Get JWT secret from environment variable
# JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key-from-env")
JWT_SECRET = "secret1234"

# Store for valid tokens (in production, use a proper database/cache)
active_tokens = set()


def generate_jwt_token(username):
    """Generate a JWT token for a user"""
    expiration = datetime.now(timezone.utc) + timedelta(hours=1)
    token = jwt.encode(
        {"username": username, "exp": expiration}, JWT_SECRET, algorithm="HS256"
    )
    active_tokens.add(token)
    return token


def verify_token(token):
    """Verify the JWT token"""
    try:
        if token not in active_tokens:
            return False
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        active_tokens.discard(token)
        return False
    except jwt.InvalidTokenError:
        return False


async def websocket_handler(websocket, path):
    try:
        # Wait for authentication message
        auth_message = await websocket.recv()
        token = auth_message.split()[1]  # Format: "Bearer <token>"

        if not verify_token(token):
            await websocket.close(1008, "Invalid token")
            return

        # Handle authenticated messages
        async for message in websocket:
            # Echo the message back
            response = f"Server received: {message}"
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close(1011, "Internal server error")


async def start_server():
    server = await websockets.serve(
        websocket_handler,
        "localhost",
        8765,
        ssl=None,  # In production, configure SSL/TLS here
    )
    print("WebSocket server started")
    await server.wait_closed()


# HTTP endpoint to get JWT token (simplified)
async def http_handler(reader, writer):
    data = await reader.read(100)
    message = data.decode()

    if message.startswith("GET /token"):
        token = generate_jwt_token("test_user")
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n{token}"
        writer.write(response.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    # Start both servers
    await asyncio.gather(
        start_server(), asyncio.start_server(http_handler, "localhost", 8080)
    )


if __name__ == "__main__":
    asyncio.run(main())

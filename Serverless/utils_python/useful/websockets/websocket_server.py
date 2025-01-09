
import asyncio
import json
import websockets
from typing import Callable, Final
from datetime import datetime, UTC

WS_HOST: str[Final] = "localhost"
WS_PORT: int[Final] = 8765

class WebSocketServer:
    def __init__(self, host: str = WS_HOST, port: int = WS_PORT):
        self.host = host
        self.port = port
        self.clients: set[websockets.WebSocketServerProtocol] = set()
        self.handlers: dict[str, Callable] = {}
        
    async def handle_connection(self, websocket: websockets.WebSocketServerProtocol):
        """Handle incoming WebSocket connections."""
        try:
            # Register client
            self.clients.add(websocket)
            client_id = id(websocket)
            print(f"Client {client_id} connected. Total clients: {len(self.clients)}")
            
            # Handle messages
            async for message in websocket:
                await self.handle_message(websocket, message)
                
        except websockets.exceptions.ConnectionClosed:
            print(f"Client {client_id} connection closed unexpectedly.")
        finally:
            # Unregister client
            self.clients.remove(websocket)
            print(f"Client {client_id} disconnected. Total clients: {len(self.clients)}")

    async def handle_message(self, websocket: websockets.WebSocketServerProtocol, message: str):
        """Process incoming messages."""
        try:
            data = json.loads(message)
            message_type = data.get('type')
            
            if message_type in self.handlers:
                # Call registered handler for this message type
                await self.handlers[message_type](websocket, data)
            else:
                # Echo message back by default
                await self.send_message(websocket, {
                    'type': 'echo',
                    'timestamp': datetime.now(datetime.timezone.utc).isoformat(),
                    'data': data
                })
                
        except json.JSONDecodeError:
            await self.send_error(websocket, "Invalid JSON format")
        except Exception as e:
            await self.send_error(websocket, str(e))

    async def broadcast(self, message: dict):
        """Send message to all connected clients."""
        if self.clients:
            await asyncio.gather(*[self.send_message(client, message) for client in self.clients])

    async def send_message(self, websocket: websockets.WebSocketServerProtocol, message: dict):
        """Send message to specific client."""
        try:
            await websocket.send(json.dumps(message))
        except Exception as e:
            print(f"Error sending message: {e}")

    async def send_error(self, websocket: websockets.WebSocketServerProtocol, error: str):
        """Send error message to client."""
        await self.send_message(websocket, {
            'type': 'error',
            'timestamp': datetime.now(datetime.timezone.utc).isoformat(),
            'error': error
        })

    def register_handler(self, message_type: str, handler: Callable):
        """Register a message handler for specific message type."""
        self.handlers[message_type] = handler

    async def start(self):
        """Start the WebSocket server."""
        async with websockets.serve(self.handle_connection, self.host, self.port):
            print(f"WebSocket server started at ws://{self.host}:{self.port}")
            await asyncio.Future()  # run forever

# Example usage
async def chat_handler(websocket: websockets.WebSocketServerProtocol, data: dict):
    """Handle chat messages."""
    message = {
        'type': 'chat',
        'timestamp': datetime.now(datetime.timezone.utc).isoformat(),
        'user': data.get('user', 'anonymous'),
        'message': data.get('message', '')
    }
    await server.broadcast(message)

# Create and run server
if __name__ == "__main__":
    server = WebSocketServer()
    
    # Register handlers
    server.register_handler('chat', chat_handler)
    
    # Start server
    asyncio.run(server.start())
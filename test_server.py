import asyncio
import websockets
import logging
import json
import time
import argparse
import random

# ロギングの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class WebSocketServer:
    def __init__(self, host="localhost", port=8765, default_room=None):
        self.host = host
        self.port = port
        self.default_room = default_room
        self.logger = logging.getLogger(__name__)
        self.rooms = {}  # ルーム名とWebSocket接続のマッピング
        self.logger.debug(f"WebSocketServer initialized on {host}:{port}")
        
        # デフォルトルームが指定されていない場合はランダムなルーム番号を生成
        if not self.default_room:
            self.default_room = str(random.randint(1000, 9999))
            self.logger.debug(f"Generated random room number: {self.default_room}")
            print(f"\nランダムなルーム番号を生成しました: {self.default_room}")
        
        # デフォルトルームを作成
        self.rooms[self.default_room] = set()
        self.logger.debug(f"Created default room: {self.default_room}")
        print(f"\nデフォルトルームを作成しました: {self.default_room}")

    async def handle_client(self, websocket, path):
        """クライアントの接続を処理"""
        room_name = None
        try:
            self.logger.debug(f"New client connected from {websocket.remote_address}")
            
            # ルーム名を受信
            room_name = await websocket.recv()
            self.logger.debug(f"Received room name: {room_name}")

            # デフォルトルームが指定されている場合、そのルームに強制的に接続
            if self.default_room:
                room_name = self.default_room
                self.logger.debug(f"Using default room: {room_name}")

            # ルームに接続を追加
            if room_name not in self.rooms:
                self.rooms[room_name] = set()
                self.logger.debug(f"Created new room: {room_name}")
                print(f"\n新しいルームが作成されました: {room_name}")
            self.rooms[room_name].add(websocket)
            self.logger.info(f"Client connected to room: {room_name}")
            print(f"クライアントがルーム {room_name} に接続しました")

            # 接続確認を送信
            await websocket.send("Connected")
            self.logger.debug("Sent connection confirmation")

            # メッセージの受信ループ
            async for message in websocket:
                try:
                    self.logger.debug(f"Received message: {message}")
                    data = json.loads(message)
                    self.logger.info(f"Received data: {data}")

                    # メッセージを処理
                    if data["type"] == "place_cube":
                        # キューブ配置コマンドを処理
                        position = data["position"]
                        size = data["size"]
                        color = data["color"]
                        
                        response = {
                            "type": "cube_placed",
                            "position": position,
                            "size": size,
                            "color": color,
                            "message": f"キューブを配置しました: 位置({position['x']}, {position['y']}, {position['z']})"
                        }
                        await websocket.send(json.dumps(response))
                        self.logger.info(f"Processed cube placement: {response}")
                        print(f"キューブ配置コマンドを受信しました: 位置({position['x']}, {position['y']}, {position['z']})")

                    elif data["type"] == "test":
                        response = {
                            "type": "response",
                            "message": "Test message received"
                        }
                        await websocket.send(json.dumps(response))
                        self.logger.debug("Sent response")

                except json.JSONDecodeError as e:
                    self.logger.error(f"Invalid JSON message: {message}")
                    await websocket.send(json.dumps({
                        "type": "error",
                        "message": "Invalid JSON format"
                    }))
                except Exception as e:
                    self.logger.error(f"Error processing message: {e}")
                    await websocket.send(json.dumps({
                        "type": "error",
                        "message": str(e)
                    }))

        except websockets.exceptions.ConnectionClosed:
            self.logger.info(f"Client disconnected from room {room_name}")
            print(f"クライアントがルーム {room_name} から切断されました")
        except Exception as e:
            self.logger.error(f"Unexpected error in handle_client: {e}")
        finally:
            # ルームから接続を削除
            if room_name in self.rooms:
                self.rooms[room_name].remove(websocket)
                if not self.rooms[room_name]:
                    del self.rooms[room_name]
                    self.logger.debug(f"Room {room_name} deleted")
                    print(f"ルーム {room_name} が削除されました")

    async def start(self):
        """WebSocketサーバーを開始"""
        try:
            self.logger.info(f"Starting WebSocket server on {self.host}:{self.port}")
            print(f"\nWebSocketサーバーを開始しました")
            print(f"ホスト: {self.host}")
            print(f"ポート: {self.port}")
            if self.default_room:
                print(f"デフォルトルーム: {self.default_room}")
            print("\n接続を待機中...")
            
            server = await websockets.serve(
                self.handle_client,
                self.host,
                self.port
            )
            self.logger.info(f"WebSocket server started successfully")
            await server.wait_closed()
        except Exception as e:
            self.logger.error(f"Error starting WebSocket server: {e}")
            raise

async def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="WebSocket server for testing")
    parser.add_argument("--host", default="localhost", help="WebSocket server host")
    parser.add_argument("--port", type=int, default=8765, help="WebSocket server port")
    parser.add_argument("--room", help="Default room name")
    args = parser.parse_args()

    server = WebSocketServer(args.host, args.port, args.room)
    await server.start()

if __name__ == "__main__":
    asyncio.run(main()) 
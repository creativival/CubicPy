import asyncio
import websockets
import logging
import json
import argparse
import random

# ロギングの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class WebSocketClient:
    def __init__(self, host="localhost", port=8765, room=None):
        self.uri = f"ws://{host}:{port}"
        self.room = room
        self.websocket = None
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"WebSocketClient initialized for {self.uri}")

    async def connect(self):
        """WebSocketサーバーに接続"""
        try:
            self.websocket = await websockets.connect(self.uri)
            self.logger.info(f"Connected to {self.uri}")

            # ルーム名を送信
            if not self.room:
                self.room = str(random.randint(1000, 9999))
            await self.websocket.send(self.room)
            self.logger.debug(f"Sent room name: {self.room}")

            # 接続確認を待機
            response = await self.websocket.recv()
            if response == "Connected":
                self.logger.info("Connection confirmed")
                print(f"サーバーに接続しました (ルーム: {self.room})")
            else:
                self.logger.warning(f"Unexpected response: {response}")

        except Exception as e:
            self.logger.error(f"Connection error: {e}")
            raise

    async def place_cube(self, x=0, y=0, z=0, size=1.0, color="#FF0000"):
        """キューブを配置するコマンドを送信"""
        try:
            message = {
                "type": "place_cube",
                "position": {"x": x, "y": y, "z": z},
                "size": size,
                "color": color
            }
            await self.websocket.send(json.dumps(message))
            self.logger.debug(f"Sent cube placement command: {message}")
            print(f"キューブを配置しました: 位置({x}, {y}, {z}), サイズ{size}, 色{color}")

            # サーバーからの応答を待機
            response = await self.websocket.recv()
            self.logger.debug(f"Received response: {response}")
            return response

        except Exception as e:
            self.logger.error(f"Error sending cube placement command: {e}")
            raise

    async def close(self):
        """接続を閉じる"""
        if self.websocket:
            await self.websocket.close()
            self.logger.info("Connection closed")

async def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="WebSocket client for testing")
    parser.add_argument("--host", default="localhost", help="WebSocket server host")
    parser.add_argument("--port", type=int, default=8765, help="WebSocket server port")
    parser.add_argument("--room", help="Room name")
    args = parser.parse_args()

    client = WebSocketClient(args.host, args.port, args.room)
    
    try:
        # サーバーに接続
        await client.connect()
        
        # 原点に赤いキューブを配置
        await client.place_cube(0, 0, 0, 1.0, "#FF0000")
        
        # 少し待機してから接続を閉じる
        await asyncio.sleep(1)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main()) 
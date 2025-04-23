import asyncio
import websockets
import logging
import json
import argparse

# ロギングの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class RelayWebSocketClient:
    def __init__(self, relay_host="websocket.voxelamming.com", room=None):
        # ローカルホストの場合はws://を使用
        protocol = "wss://" if relay_host != "localhost" else f"ws://{relay_host}:8765"
        self.relay_uri = f"{protocol}{relay_host}"
        self.room = room
        self.websocket = None
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"RelayWebSocketClient initialized for {self.relay_uri}")

    async def connect(self):
        """リレーサーバーに接続"""
        try:
            # SSL検証を無効化（ローカルテスト用）
            ssl_context = None if "localhost" in self.relay_uri else True
            self.websocket = await websockets.connect(
                self.relay_uri,
                ssl=ssl_context,
                open_timeout=30,  # タイムアウト時間を30秒に延長
                close_timeout=10,
                ping_interval=20,
                ping_timeout=20
            )
            self.logger.info(f"Connected to relay server at {self.relay_uri}")

            if not self.room:
                self.logger.error("Room number is required")
                raise ValueError("ルーム番号を指定してください")
            
            # ルーム名を送信
            await self.websocket.send(self.room)
            self.logger.debug(f"Sent room name: {self.room}")
            print(f"サーバーに接続しました (ルーム: {self.room})")

        except websockets.exceptions.InvalidStatusCode as e:
            self.logger.error(f"Invalid status code: {e.status_code}")
            print(f"サーバー接続エラー: ステータスコード {e.status_code}")
        except websockets.exceptions.InvalidHandshake:
            self.logger.error("Invalid handshake")
            print("サーバーとのハンドシェイクに失敗しました")
        except TimeoutError:
            self.logger.error("Connection timeout")
            print("サーバーへの接続がタイムアウトしました。以下の点を確認してください：")
            print("1. サーバーが起動しているか")
            print("2. ホスト名とポート番号が正しいか")
            print("3. ファイアウォールの設定")
        except Exception as e:
            self.logger.error(f"Connection error: {e}")
            print(f"予期せぬエラーが発生しました: {e}")
            raise

    async def place_cube(self, x=0, y=0, z=0, size=1.0, r=0, g=0, b=0):
        """キューブを配置するコマンドを送信"""
        try:
            message = {
                "type": "place_cube",
                "position": {"x": x, "y": y, "z": z},
                "size": size,
                "color": {"r": r, "g": g, "b": b}
            }
            await self.websocket.send(json.dumps(message))
            self.logger.debug(f"Sent cube placement command: {message}")
            print(f"キューブを配置しました: 位置({x}, {y}, {z}), サイズ{size}, 色{r}, {g}, {b}")

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
    parser.add_argument("--host", default="websocket.voxelamming.com", 
                       help="Relay server host (without https:// or http://)")
    parser.add_argument("--room", required=True, help="Room number")
    args = parser.parse_args()

    client = RelayWebSocketClient(args.host, args.room)
    
    try:
        # サーバーに接続
        await client.connect()
        
        # 原点に赤いキューブを配置
        await client.place_cube(0, 0, 0, 1.0, 1, 0, 0)
        
        # 少し待機してから接続を閉じる
        await asyncio.sleep(1)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main()) 
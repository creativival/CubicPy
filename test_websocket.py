import asyncio
import websockets
import json
import logging
import argparse
from cubicpy.websocket_server import WebSocketServer

# ロギングの設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class TestWebSocketClient:
    def __init__(self, host="websocket.voxelamming.com"):
        # ローカルホストの場合はws://を使用
        protocol = "wss://" if host != "localhost" else f"ws://{host}:8765"
        self.relay_uri = f"{protocol}{host}"
        self.logger = logging.getLogger(__name__)
        self.websocket = None
        self.logger.debug(f"TestWebSocketClient initialized for {self.relay_uri}")

    async def connect(self, room):
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
            
            # ルーム名を送信
            await self.websocket.send(room)
            self.logger.debug(f"Sent room name: {room}")
            print(f"\nルーム {room} に接続しました")

            # メッセージの受信ループ
            async for message in self.websocket:
                try:
                    self.logger.debug(f"Received message: {message}")
                    data = json.loads(message)
                    self.logger.info(f"Received data: {data}")

                    # メッセージを処理
                    if data["type"] == "place_cube":
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
                        await self.websocket.send(json.dumps(response))
                        self.logger.info(f"Processed cube placement: {response}")
                        print(f"キューブ配置コマンドを受信しました: 位置({position['x']}, {position['y']}, {position['z']})")

                except json.JSONDecodeError as e:
                    self.logger.error(f"Invalid JSON message: {message}")
                except Exception as e:
                    self.logger.error(f"Error processing message: {e}")

        except websockets.exceptions.ConnectionClosed:
            self.logger.info("Disconnected from relay server")
            print("リレーサーバーから切断されました")
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
            self.logger.error(f"Error in connect: {e}")
            print(f"予期せぬエラーが発生しました: {e}")
            raise

    async def close(self):
        """接続を閉じる"""
        if self.websocket:
            await self.websocket.close()
            self.logger.info("Connection closed")
            
async def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="WebSocket server test")
    parser.add_argument("--host", default="websocket.voxelamming.com", 
                       help="Relay server host (without https:// or http://)")
    args = parser.parse_args()

    # 物理エンジンはテスト用にNoneを渡す
    server = WebSocketServer(None, args.host)
    
    # サーバーを別スレッドで起動
    server_thread = server.run_in_thread()
    
    # クライアントの接続を待つ
    await asyncio.sleep(2)
    
    # テストクライアントを実行
    client = TestWebSocketClient(args.host)
    try:
        await client.connect(server.room)
    except KeyboardInterrupt:
        print("\n終了します...")
    finally:
        await client.close()
        await server.close()

if __name__ == "__main__":
    asyncio.run(main()) 
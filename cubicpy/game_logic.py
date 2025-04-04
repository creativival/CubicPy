import threading
import time


class GameLogic:
    """ゲームのロジックを管理するクラス"""

    def __init__(self, app):
        """ゲームロジックの初期化"""
        self.app = app
        self.running = False
        self.thread = None
        self.score = 0
        self.last_update_time = 0
        self.target_type = 'cube'  # デフォルトのターゲットタイプ

    def start(self):
        """ゲームロジックのスレッドを開始"""
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """ゲームロジックのスレッドを停止"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)
            self.thread = None

    def get_moved_count(self):
        """倒れたピンの数を取得"""
        try:
            count = 0
            for obj in self.app.world_manager.body_objects:
                if obj['type'] == self.target_type:
                    # オブジェクトが動いたかチェック
                    initial_pos = obj['object'].node_pos
                    current_pos = obj['object'].cylinder_node.getPos()

                    # 位置の差を計算
                    dx = abs(current_pos.x - initial_pos.x)
                    dy = abs(current_pos.y - initial_pos.y)

                    # 閾値以上に動いたら倒れたと判断
                    if dx > 0.1 or dy > 0.1:
                        count += 1
            return count
        except Exception as e:
            print(f"エラー: {e}")
            return 0

    def update_score_display(self):
        """スコア表示を更新"""
        current_score = self.get_moved_count()

        if current_score != self.score:
            self.score = current_score
            self.app.set_bottom_left_text(f"スコア: {self.score}")

    def _run(self):
        """内部スレッドの実行関数"""
        while self.running:
            try:
                # 現在の時刻を取得（スコア更新の間隔調整用）
                current_time = time.time()

                # 一定間隔でスコア更新（負荷軽減のため）
                if current_time - self.last_update_time > 0.2:  # 0.2秒間隔
                    self.update_score_display()
                    self.last_update_time = current_time

                time.sleep(0.05)  # 短い待機時間でCPU負荷を抑える

            except Exception as e:
                print(f"ゲームロジック実行中にエラー: {e}")
                time.sleep(1)  # エラー時は長めに待機
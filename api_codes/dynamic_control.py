from cubicpy import CubicPyApp
import time

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# ターゲットとなる箱を配置
for i in range(5):
    for j in range(3):
        app.add_cube(
            position=(i * 2, j * 2, 0),
            scale=(1, 1, 1),
            color=(0.8, 0.2, 0.2)  # 赤
        )

    # 球を作成して発射
app.add_sphere(
    position=(-5, 5, 0),
    scale=(1, 1, 1),
    color=(0.2, 0.2, 0.8),  # 青
    mass=10,
    base_point=1,  # 底面中心
    velocity=(15, -5, 0)  # 右下向きに発射
)

# 動的に球を発射する関数
def launch_sequence():
    # 球が発射された瞬間に実際に動かす
    app.launch_objects()

    # メッセージを更新
    time.sleep(1)
    app.set_top_left_text("Rキーでリセット、もう一度発射するには何かキーを押してください")


# 初期情報を表示
app.set_top_left_text("何かキーを押して発射シーケンスを開始...")


# カスタムキーハンドラを設定（コールバック関数）
# 注: これは上級者向けの技術で、一般的なAPIの一部ではありません
# この例のみ参考用として提供します
def key_handler(key):
    if key != 'r':  # リセットキー以外が押されたとき
        launch_sequence()


# シミュレーションを実行（任意のキーハンドラ付き）
# 注: key_handler引数は一般的なAPIの一部ではなく、学習目的としてのみ提供
app.run(key_handler=key_handler)
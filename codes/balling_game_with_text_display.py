from cubicpy import CubicPyApp
# import threading
# import time

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 簡単なボウリングゲームのセットアップ
# ピンを配置
pin_positions = [
    (0, 0, 0),  # 一番前のピン
    (-1, 1, 0), (1, 1, 0),  # 2列目
    (-2, 2, 0), (0, 2, 0), (2, 2, 0),  # 3列目
]

for pos in pin_positions:
    app.add_cylinder(
        position=(pos[0], pos[1], 0),
        scale=(0.8, 0.8, 3.2),
        color=(1, 1, 1),  # 白
        base_point=1,  # 底面中心
    )

# ボールを作成
app.add_sphere(
    position=(0, -20, 0),
    scale=(2, 2, 2),
    color=(0.3, 0.3, 0.8),  # 青
    mass=10,
    velocity=(0, 10, 0),  # 前方向に発射
    base_point=1,  # 底面中心
)

# テキスト表示
app.set_top_left_text('ボウリングゲーム')
app.set_bottom_left_text("操作方法: 矢印キーでカメラ移動、R でリセット")

# アプリを実行
app.run()

# # 終了フラグ（スレッド間の通信用）
# stop_thread = False
#
# def is_nearly_equal(v1, v2, tolerance=0.01):
#     """二つのベクトルがほぼ同じかチェック"""
#     dx = abs(v1.x - v2.x)
#     dy = abs(v1.y - v2.y)
#     dz = abs(v1.z - v2.z)
#     return dx < tolerance and dy < tolerance and dz < tolerance
#
#
# # 別スレッドで実行する関数
# def game_logic():
#     while not stop_thread:
#         try:
#             print("ボウリングゲームを実行中...")
#
#             # 位置情報の取得
#             num_moved = 0
#             for obj in app.world_manager.body_objects:
#                 if obj['type'] == 'cylinder':
#                     # 追加したメソッドを使用してピンが動いたかチェック
#                     if obj['object'].has_moved(tolerance=0.1):  # より大きな許容誤差を使用
#                         num_moved += 1
#
#             if num_moved > 0:
#                 app.set_bottom_left_text(f"スコア: {num_moved}")
#
#             # スレッドの負荷を下げるために少し待機
#             time.sleep(0.1)
#
#         except Exception as e:
#             print(f"エラーが発生しました: {e}")
#             time.sleep(1)  # エラー時は少し長めに待機
#
#
# # ゲームロジックのスレッドを開始
# logic_thread = threading.Thread(target=game_logic)
# logic_thread.daemon = True  # メインスレッドが終了したら、このスレッドも終了
# logic_thread.start()
#
# try:
#     # シミュレーションを実行（メインスレッド）
#     app.run()
# finally:
#     # スレッドを終了するためのフラグをセット
#     stop_thread = True
#     # スレッドが終了するのを待つ
#     logic_thread.join(timeout=1.0)
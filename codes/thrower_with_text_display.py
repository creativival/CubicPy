from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 壁を追加
for j in range(20):
    for i in range(20):
        app.add_cube(
            position=(20, i, j),  # 位置
            scale=(1, 1, 1),     # サイズ
            color=(0.5, 0.5, 0.5)  # 色（灰色）
        )

# 投擲機を追加
for i in range(10):
    app.add_sphere(
        position=(0, i * 2, 0),  # 位置
        scale=(2, 2, 2),     # サイズ
        color=(0.8, 0.2, 0.2),  # 色（赤）
        mass=10,  # 質量
        velocity=(i, 0, i)  # 初速
    )

# テキスト表示
app.set_top_left_text('投擲機シミュレーション: スペースキーで発射！')
app.set_bottom_left_text("操作方法: 矢印キーでカメラ移動、R でリセット")

# アプリを実行
app.run()
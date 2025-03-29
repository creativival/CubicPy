from cubicpy import CubicPyApp

# インスタンス化
app = CubicPyApp(gravity_factor=1, window_size=(1800, 1200))

# 複数オブジェクトの追加（ループ）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),
        color=(i / 10, 0, 1 - i / 10)
    )

# 座標系の変換（1段目）
app.push_matrix()
app.translate(5, 5, 0)  # 地面から開始

# 複数オブジェクトの追加（ループ）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),
        color=(i / 10, 1 - i / 10, 0)
    )

# 座標系の変換（2段目）
app.push_matrix()
app.translate(5, 5, 0)  # 地面から開始
app.rotate_hpr(45, 10, 0)  # Y軸周りに45度回転

# 複数オブジェクトの追加（ループ）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),
        color=(0, i / 10, 1 - i / 10)
    )

# 座標系の変換から戻る（2段目）
app.pop_matrix()

# 座標系の変換から戻る（1段目）
app.pop_matrix()

# シミュレーション実行
app.run()

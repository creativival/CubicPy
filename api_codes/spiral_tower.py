from cubicpy import CubicPyApp
import math

app = CubicPyApp(gravity_factor=0.1, window_size=(1800, 1200))

# スパイラルタワーを作成
def create_spiral_tower(x, y, height, layers, radius, color_gradient=True):
    app.push_matrix()
    app.translate(x, y, 0)

    # 各層ごとにブロックを配置
    for i in range(layers):
        z_pos = i * height  # 高さの計算
        angle = i * 5  # 角度の変化

        # 色のグラデーション（オプション）
        if color_gradient:
            t = i / layers
            color = (0.7 * (1 - t), 0.3 + 0.4 * t, 0.2 + 0.6 * t)
        else:
            color = (0.5, 0.5, 0.5)

        app.push_matrix()
        app.translate(0, 0, z_pos)
        app.rotate_hpr(angle, 0, 0)  # Y軸周りに回転

        # ブロックを配置
        for j in range(4):
            block_angle = j * 90
            block_radius = radius

            # ブロックの位置を計算
            bx = block_radius * math.cos(math.radians(block_angle))
            by = block_radius * math.sin(math.radians(block_angle))

            app.push_matrix()
            app.translate(bx, by, 0)
            app.rotate_hpr(block_angle, 0, 0)

            # ブロックを追加
            app.add_cube(
                position=(0, 0, 0),
                scale=(2, 1, height),
                color=color,
                base_point=1  # 重心を基準に配置
            )

            app.pop_matrix()

        app.pop_matrix()

    app.pop_matrix()


# メインの塔
create_spiral_tower(0, 0, 2, 100, 8, True)

app.run()
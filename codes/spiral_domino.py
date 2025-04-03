import math

body_data = []

# ドミノの設定
domino_width = 0.5
domino_height = 2.0
domino_thickness = 0.2
radius = 10.0  # 円の半径
num_dominoes = 180  # ドミノの数

# 円形にドミノを配置
angle = -math.pi / 2  # 初期角度
for i in range(num_dominoes):
    # ドミノの半径を少しずつ増やす
    spiral_radius = radius * (1.005 ** i)

    # 円周上の位置を計算
    angle += math.atan2(1.0, spiral_radius)  # 角度（ラジアン）
    x_pos = spiral_radius * math.cos(angle)
    y_pos = spiral_radius * math.sin(angle) + radius

    # ドミノを円の中心に向けて配置
    body_data.append({
        'type': 'cube',
        'pos': (x_pos, y_pos, 0),
        'scale': (domino_thickness, domino_width, domino_height),
        'color': (i / num_dominoes, 1 - i / num_dominoes, 0),  # グラデーション
        'mass': 10 if i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
        'hpr': (math.degrees(angle + math.pi / 2), 0, 0),  # 角度を度数に変換して設定
        'base_point': 1,  # 中心を基準に配置
        'velocity': (2, 0, 0) if i == 0 else (0, 0, 0),  # X軸方向（右）に発射
    })
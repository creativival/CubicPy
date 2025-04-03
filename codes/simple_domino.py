body_data = []

# ドミノの設定
domino_width = 0.5
domino_height = 2.0
domino_thickness = 0.2
spacing = 0.8  # ドミノ間の距離
num_dominoes = 20

# 直線上にドミノを配置
for i in range(num_dominoes):
    # 各ドミノの位置を計算
    x_pos = i * spacing
    y_pos = 0
    z_pos = 0  # 地面にドミノの底面が接するように

    # ドミノを追加
    body_data.append({
        'type': 'cube',
        'pos': (x_pos, y_pos, 0),  # 位置（高さは半分の位置）
        'scale': (domino_thickness, domino_width, domino_height),
        'color': (i / num_dominoes, 1, 1 - i / num_dominoes),  # グラデーション
        'mass': 10 if i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
        'base_point': 1,  # 中心を基準に配置
        'velocity': (2, 0, 0) if i == 0 else (0, 0, 0),  # X軸方向（右）に発射
    })
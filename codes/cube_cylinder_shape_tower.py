from math import atan, cos, sin, pi, degrees

body_data = []
radius = 10  # 円の半径
height = 40  # 塔の高さ
box_size = 1  # キューブのサイズ

# キューブの半径と高さから、ボックスの数を決定
half_size = box_size / 2
half_angle = atan(half_size / (radius - box_size))
box_num = int(pi / half_angle)

# キューブを配置するための基準角度
base_angle = pi * 2 / box_num

# 塔の高さ分だけキューブを配置
for j in range(height):
    for i in range(box_num):
        # 偶数段と奇数段で角度を調整
        if j % 2 == 0:
            angle = base_angle * (i + 1 / 2)
        else:
            angle = base_angle * i

        # キューブの位置を計算
        x = radius * cos(angle)
        y = radius * sin(angle)
        z = j * box_size

        pos = (x, y, z)  # ボックスの下端がZ=0から始まるように調整
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (box_size, box_size, box_size),  # X方向の幅とZ方向の高さを適切に設定
            'color': (j / height, 0, 1 - j / height),  # 塔の高さに応じて色を変える
            'mass': 1,
            'hpr': (degrees(angle), 0, 0),  # キューブを配置した角度で回転させる
            'base_point': 1  # キューブの底の中心を基準点に設定
        })

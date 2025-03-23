from math import atan, cos, sin, pi, degrees

body_data = []
radius = 4  # 円の半径
height = 120
box_size = 1
half_size = box_size / 2
half_angle = atan(half_size / (radius - box_size))
box_num = int(pi / half_angle)
twist_radius = 5

for j in range(height):
    twist_angle = pi / height * j * 2

    for i in range(box_num):
        if j % 2 == 0:
            x = radius * cos(half_angle * i * 2)
            y = radius * sin(half_angle * i * 2)
        else:
            x = radius * cos(half_angle * (i * 2 + 1))
            y = radius * sin(half_angle * (i * 2 + 1))
        x += twist_radius * cos(twist_angle)
        y += twist_radius * sin(twist_angle)
        z = j * box_size
        angle = half_angle * i * 2 + twist_angle

        pos = (x, y, z)  # ボックスの下端がZ=0から始まるように調整
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),  # X方向の幅とZ方向の高さを適切に設定
            'color': (1, 0, 0),
            'mass': 1,
            'hpr': (degrees(angle), 0, 0),
            'position_mode': 'bottom_center'
        })

        pos_pair = (-x, -y, z)
        angle_pair = angle + pi
        body_data.append({
            'type': 'box',
            'pos': pos_pair,
            'scale': (1, 1, 1),  # X方向の幅とZ方向の高さを適切に設定
            'color': (1, 1, 1),
            'mass': 1,
            'hpr': (degrees(angle_pair), 0, 0),
            'position_mode': 'bottom_center'
        })

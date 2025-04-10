from math import atan, cos, sin, pi, degrees

body_data = []
radius = 20  # 円の半径
height = 20
cube_size = 1
half_size = cube_size / 2
half_angle = atan(half_size / (radius - cube_size))
cube_num = int(pi / half_angle)

for j in range(height):
    for i in range(cube_num):
        if j % 2 == 0:
            x = radius * cos(half_angle * i * 2)
            y = radius * sin(half_angle * i * 2)
        else:
            x = radius * cos(half_angle * (i * 2 + 1))
            y = radius * sin(half_angle * (i * 2 + 1))
        z = j * cube_size
        angle = half_angle * i * 2

        pos = (x, y, z)  # ボックスの下端がZ=0から始まるように調整
        body_data.append({
            'type': 'cube',
            'pos': pos,
            'scale': (1, 1, 1),  # X方向の幅とZ方向の高さを適切に設定
            'color': (1, 0, 0),
            'mass': 1,
            'hpr': (degrees(angle), 0, 0),
            'base_point': 1
        })

from math import atan, cos, sin, pi, degrees

body_data = []
radius = 20  # 円の半径
height = 40
box_size = 1
half_size = box_size / 2
# half_angle = atan(half_size / (radius - box_size))
# box_num = int(pi / half_angle)

for j in range(height):
    r = radius * (1 - j / height)
    half_angle = atan(half_size / (r - box_size))
    box_num = int(pi / half_angle)

    for i in range(box_num):
        if j % 2 == 0:
            x = r * cos(half_angle * i * 2)
            y = r * sin(half_angle * i * 2)
        else:
            x = r * cos(half_angle * (i * 2 + 1))
            y = r * sin(half_angle * (i * 2 + 1))
        z = j * box_size

        pos = (x, y, z)  # ボックスの下端がZ=0から始まるように調整
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),  # X方向の幅とZ方向の高さを適切に設定
            'color': (1, 0, 0),
            'mass': 1,
            'hpr': (degrees(half_angle * i * 2), 0, 0),
            'position_mode': 'bottom_center'
        })

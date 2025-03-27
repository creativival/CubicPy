from math import sqrt

body_data = []
step_num = 20

# X軸
for i in range(step_num):
    x = (step_num - (i + 1)) / sqrt(3)
    y = x
    z = i
    pos = (x, y, z)
    body_data.append({
        'type': 'box',
        'pos': pos,
        'scale': (1, 1, 1),
        'color': (1, 0, 0),
        'mass': 1
    })

    if i != step_num - 1:
        pos = (-x, y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })

        pos = (x, -y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })

        pos = (-x, -y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })

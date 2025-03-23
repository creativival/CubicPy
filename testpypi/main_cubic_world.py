from cubicpy import CubicWorld

world = CubicWorld()

# 単独オブジェクトの追加
world.add_box(position=(-3, 0, 0), color=(1, 0, 0))
world.add_sphere(position=(3, 0, 0), color=(0, 0, 1))

# 複数オブジェクトの追加（ループ）
for i in range(10):
    world.add_box(
        position=(0, 0, i),
        color=(i/10, 0, 1-i/10)
    )

# 従来のコードと互換性を保つbody_dataの追加
body_data = []
for i in range(10):
    body_data.append({
        'type': 'box',
        'pos': (0, 3, i),
        'scale': (1, 1, 1),
        'color': (i / 10, 0, 1 - i / 10),
    })

world.from_body_data(body_data)

# シミュレーション実行
world.run()
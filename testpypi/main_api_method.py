from cubicpy import CubicPyApp

# インスタンス化
app = CubicPyApp(gravity_factor=0.01, window_size=(1800, 1200))

# 単独オブジェクトの追加
# APIを使ってオブジェクトを追加
app.add_box(position=(0, 0, 0), scale=(1, 1, 1), color=(1, 0, 0))
app.add_sphere(position=(2, 0, 0),  scale=(1, 1, 1), color=(0, 1, 0))
app.add_cylinder(position=(4, 0, 0),  scale=(1, 1, 1), color=(0, 0, 1))

# 複数オブジェクトの追加（ループ）
for i in range(10):
    app.add_box(
        position=(0, 5, i),
        color=(i/10, 0, 1-i/10)
    )

# cubicpyコマンドと互換性を保つbody_dataの追加
body_data = []
for i in range(10):
    body_data.append({
        'type': 'box',
        'pos': (0, 10, i),
        'scale': (1, 1, 1),
        'color': (i / 10, 0, 1 - i / 10),
        'mass': 1,
        'color_alpha': 1,
    })

app.from_body_data(body_data)

# シミュレーション実行
app.run()
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 箱を追加
app.add_cube(
    position=(0, 0, 0),      # 位置
    scale=(1, 1, 1),         # サイズ
    color=(1, 0, 0),         # 色（赤）
    mass=1,                  # 質量
    color_alpha=1,           # 透明度（1=不透明、0=透明）
    hpr=(0, 0, 0),           # 回転（heading, pitch, roll）
    base_point=0,            # 基準点（0=角、1=底面中心、2=重心）
    velocity=(2, 0, 0)            # 初速度ベクトル
)

# 球を追加
app.add_sphere(
    position=(2, 0, 0),      # 位置（X座標を2にして右に配置）
    scale=(1, 1, 1),         # サイズ
    color=(0, 1, 0),          # 色（緑）
    remove=True,            # 削除フラグ
)

# 円柱を追加
app.add_cylinder(
    position=(4, 0, 0),      # 位置（X座標を4にして右に配置）
    scale=(1, 1, 1),         # サイズ
    color=(0, 0, 1)          # 色（青）
)

# シミュレーションを実行
app.run()
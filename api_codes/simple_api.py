from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 箱を追加
app.add_cube(
    position=(0, 0, 0),  # 位置
    scale=(1, 1, 1),     # サイズ
    color=(1, 0, 0)      # 色（赤）
)

# シミュレーションを実行
app.run()
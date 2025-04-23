import math
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()


# 家の基本構造を作成する関数
def create_house(pos_x, pos_y, width, depth, height, roof_angle=45):
    # 座標系を家の位置に移動
    app.push_matrix()
    app.translate(pos_x, pos_y, 0)

    # 家の基礎部分（立方体）
    app.add_cube(
        position=(0, 0, 0),
        scale=(width, depth, height),
        color=(0.8, 0.6, 0.4)  # 茶色
    )

    # 屋根部分

    # 座標系を屋根の底面中心に移動
    app.push_matrix()
    app.translate(width / 2, depth / 2, height)

    # 屋根の角度から屋根の階段高さを計算
    roof_step_height = 0.5 * math.tan(math.radians(roof_angle))

    # whileループで屋根を作成
    roof_width = width + 2
    roof_depth = depth + 2
    i = 0
    while roof_width >= 0.5 or i > 100:

        app.add_cube(
            position=(0, 0, i * roof_step_height),
            scale=(roof_width, roof_depth, roof_step_height),
            color=(1, 0, 0),  # 赤色
            base_point=1,  # 基準点を底面中心に設定
        )

        # 変数を更新
        roof_width -= 1
        i += 1

    # 屋根の座標系を戻す
    app.pop_matrix()

    # 家全体の座標系を戻す
    app.pop_matrix()


# 複数の家を配置
create_house(-10, 0, 5, 6, 5)  # 左側に小さな家
create_house(0, 0, 7, 8, 6, roof_angle=30)  # 中央に中くらいの家
create_house(12, 0, 10, 9, 8, roof_angle=60)  # 右側に大きな家

# シミュレーションを実行
app.run()
from cubicpy import CubicPyApp

app = CubicPyApp(gravity_factor=0.1, window_size=(1800, 1200))

# 座標系の変換を使って、簡単に複雑な構造を作る
def draw_branch(length, branch_count, branch_factor):
    if branch_count < 1:
        return

    # 木の幹を作成（太さも分岐レベルに応じて細くなる）
    app.add_cylinder(
        position=(0, 0, 1),
        scale=(0.5, 0.5, length - 1),
        color=(0, 1, 0),
        base_point=1  # 重心を基準に配置
    )

    # 次の枝の分岐点まで移動
    app.push_matrix()
    app.translate(0, 0, length)

    # 複数の枝を作成
    branch_length = length * branch_factor
    branch_count -= 1

    # 3方向に枝を伸ばす
    for angle in [0, 120, 240]:
        app.push_matrix()
        app.rotate_hpr(angle, 30, 0)  # Y軸周りに角度を変え、X軸周りに30度傾ける
        draw_branch(branch_length, branch_count, branch_factor)
        app.pop_matrix()

    app.pop_matrix()


# 木を描画
max_branch_count = 4  # より深いフラクタル
draw_branch(20, max_branch_count, 0.7)

app.run()
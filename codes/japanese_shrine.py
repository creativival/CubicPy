from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成（低重力設定）
app = CubicPyApp(gravity_factor=0.1)


# 神社を作成する関数
def create_shrine(pos_x, pos_y, size):
    # 座標系を神社の位置に移動
    app.push_matrix()
    app.translate(pos_x, pos_y, 0)

    # 基壇（土台）
    platform_height = size * 0.2
    platform_width = size * 3
    platform_depth = size * 2
    app.add_cube(
        position=(0, 0, 0),
        scale=(platform_width, platform_depth, platform_height),
        color=(0.7, 0.7, 0.7),  # 灰色
        base_point=1,  # 底面中心
    )

    # 神社本体
    main_width = size * 2
    main_depth = size * 1.5
    main_height = size * 1.2
    app.add_cube(
        position=(0, 0, platform_height),
        scale=(main_width, main_depth, main_height),
        color=(0.8, 0.3, 0.2),  # 朱色
        base_point=1,  # 底面中心
    )

    # 屋根
    roof_width = main_width * 1.3
    roof_depth = main_depth * 1.3
    roof_height = size * 0.8

    # 屋根の基部
    roof_base_height = size * 0.1
    app.add_cube(
        position=(0, 0, platform_height + main_height),
        scale=(roof_width, roof_depth, roof_base_height),
        color=(0.1, 0.1, 0.1),  # 黒
        base_point=1,  # 底面中心
    )

    # 屋根を表現（複数の立方体を重ねて表現）
    roof_layers = 10
    for i in range(roof_layers):
        progress = (i + 1) / (roof_layers - 1)
        layer_width = roof_width * (1 - 0.4 * progress)
        layer_depth = roof_depth * (1 - 0.4 * progress)
        layer_height = roof_height / roof_layers

        layer_z = platform_height + main_height + roof_base_height + \
                  i * layer_height

        app.add_cube(
            position=(0, 0, layer_z),
            scale=(layer_width, layer_depth, layer_height),
            color=(0.1, 0.1, 0.1),  # 黒
            base_point=1,  # 底面中心
        )

    # 鳥居
    torii_height = size * 2
    torii_width = size * 1.5
    pillar_thickness = size * 0.1

    # 鳥居の位置（神社の手前）
    app.push_matrix()
    app.translate(0, -platform_depth, 0)

    # 柱（左右）
    app.add_cube(
        position=(-torii_width / 2, 0, 0),
        scale=(pillar_thickness, pillar_thickness, torii_height),
        color=(0.9, 0.2, 0.1),  # 朱色
        base_point=1,  # 底面中心
    )

    app.add_cube(
        position=(torii_width / 2, 0, 0),
        scale=(pillar_thickness, pillar_thickness, torii_height),
        color=(0.9, 0.2, 0.1),  # 朱色
        base_point=1,  # 底面中心
    )

    # 上部の横木
    app.add_cube(
        position=(0, 0, torii_height),
        scale=(torii_width + pillar_thickness + 4, pillar_thickness, pillar_thickness),
        color=(0.9, 0.2, 0.1),  # 朱色
        base_point=1,  # 底面中心
    )

    # 中間の横木
    app.add_cube(
        position=(0, -pillar_thickness, torii_height - pillar_thickness * 3),
        scale=(torii_width + pillar_thickness + 4, pillar_thickness, pillar_thickness),
        color=(0.9, 0.2, 0.1),  # 朱色
        base_point=1,  # 底面中心
    )

    # 鳥居の座標系を戻す
    app.pop_matrix()

    # 参道（アプローチ通路）
    path_length = size * 5
    path_width = main_width * 0.6
    path_height = size * 0.05

    app.add_cube(
        position=(0, -(platform_depth + path_length) / 2, 0),
        scale=(path_width, path_length, path_height),
        color=(0.8, 0.8, 0.7),  # 砂色
        base_point=1,  # 底面中心
    )

    # 石灯籠（左右に配置）
    lantern_height = size * 0.8
    lantern_dist = path_width * 0.8

    # 座標系を参道の位置に移動
    app.push_matrix()
    app.translate(0, -(platform_depth + size), path_height)

    for side in [-1, 1]:
        app.push_matrix()
        app.translate(side * lantern_dist / 2, 0, 0)

        # 土台
        app.add_cube(
            position=(0, 0, 0),
            scale=(size * 0.3, size * 0.3, lantern_height * 0.2),
            color=(0.6, 0.6, 0.6),  # 灰色
            base_point=1,  # 底面中心
        )

        # 柱
        app.add_cylinder(
            position=(0, 0, lantern_height * 0.2),
            scale=(size * 0.1, size * 0.1, lantern_height * 0.3),
            color=(0.7, 0.7, 0.7),  # 灰色
            base_point=1,  # 底面中心
        )

        # 灯籠本体
        app.add_cube(
            position=(0, 0, lantern_height * 0.5),
            scale=(size * 0.25, size * 0.25, lantern_height * 0.2),
            color=(0.7, 0.7, 0.7),  # 灰色
            base_point=1,  # 底面中心
        )

        # 灯籠の屋根
        app.add_cube(
            position=(0, 0, lantern_height * 0.7),
            scale=(size * 0.3, size * 0.3, lantern_height * 0.1),
            color=(0.6, 0.6, 0.6),  # 灰色
            base_point=1,  # 底面中心
        )

        app.pop_matrix()

    # 石灯籠の座標系を戻す
    app.pop_matrix()

    # 神社全体の座標系を戻す
    app.pop_matrix()


# 神社を作成
create_shrine(0, 0, 4)

# テキスト表示
app.set_top_left_text("日本の神社モデル")
app.set_bottom_left_text("矢印キーでカメラ移動、SHIFT+WASDQE でカメラ位置移動")

# シミュレーションを実行
app.run()
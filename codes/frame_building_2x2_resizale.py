# グローバル変数として最初に定義
body_data = []


def create_building(building_x, building_y, building_z, step_num, _body_data):
    # Z軸
    for k in range(step_num):
        # Y軸
        for j in range(2):
            # X軸
            for i in range(2):
                if j < 1:
                    # Y方向の梁
                    pos_y_beam = (i * (building_x - 0.5), 0.5, (building_z - 1) + k * building_z)
                    scale_y_beam = (0.5, building_y - 1, 1)
                    _body_data.append({
                        'type': 'cube',
                        'pos': pos_y_beam,
                        'scale': scale_y_beam,
                        'color': (1, 0, 0),
                        'mass': 1
                    })

                if i < 1:
                    # X方向の梁
                    pos_x_beam = (0, j * (building_y - 0.5), (building_z - 1) + k * building_z)
                    scale_x_beam = (building_x, 0.5, 1)
                    _body_data.append({
                        'type': 'cube',
                        'pos': pos_x_beam,
                        'scale': scale_x_beam,
                        'color': (1, 0, 0),
                        'mass': 1
                    })

                # 柱の作成
                pos_beam = (i * (building_x - 1), j * (building_y - 1), k * building_z)
                scale_beam = (1, 1, building_z - 1)
                _body_data.append({
                    'type': 'cube',
                    'pos': pos_beam,
                    'scale': scale_beam,
                    'color': (i, j, k / step_num),
                    'mass': 1
                })


# ビルの生成
create_building(8, 6, 10, 10, body_data)

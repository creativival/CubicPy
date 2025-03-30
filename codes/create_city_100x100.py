import random
import math

# 全体のオブジェクトデータを格納するリスト
body_data = []

# 都市設定パラメータ
MIN_FLOOR_HEIGHT = 4  # 各階の最小高さ
MAX_FLOOR_HEIGHT = 5  # 各階の最大高さ
CITY_WIDTH = 100  # 都市の幅
CITY_LENGTH = 100  # 都市の長さ
DISTRICTS_PER_ROW = 4  # 1行あたりの区画数
DISTRICT_ROWS = 2  # 区画の行数

# 区画とビルの配置パターンを定義
# 各区画には複数のビルが配置される
district_templates = [
    {
        'size': (25, 40),  # 区画のサイズ (幅, 奥行き)
        'buildings': [
            {
                'size': (23, 18),  # ビルのサイズ (幅, 奥行き)
                'pos': (1, 1),  # 区画内の位置 (x, y)
                'floor_num': 20  # 階数
            },
            {
                'size': (13, 18),
                'pos': (1, 21),
                'floor_num': 10
            },
            {
                'size': (8, 18),
                'pos': (16, 21),
                'floor_num': 18
            },
        ]
    },
    {
        'size': (25, 40),
        'buildings': [
            {
                'size': (23, 18),
                'pos': (1, 21),
                'floor_num': 20
            },
            {
                'size': (13, 18),
                'pos': (1, 1),
                'floor_num': 10
            },
            {
                'size': (8, 18),
                'pos': (16, 1),
                'floor_num': 18
            },
        ]
    },
    {
        'size': (25, 40),
        'buildings': [
            {
                'size': (23, 28),
                'pos': (1, 1),
                'floor_num': 16
            },
            {
                'size': (23, 8),
                'pos': (1, 31),
                'floor_num': 6
            },
        ]
    },
    {
        'size': (25, 40),
        'buildings': [
            {
                'size': (23, 28),
                'pos': (1, 11),
                'floor_num': 16
            },
            {
                'size': (23, 8),
                'pos': (1, 1),
                'floor_num': 6
            },
        ]
    },
]


def create_building(x_pos, y_pos, z_pos, width, depth, floor_height, num_floors, target_data):
    """
    指定された位置とサイズでビルを生成し、target_dataリストに追加する

    Parameters:
    -----------
    x_pos: float
        ビルのX座標（左端）
    y_pos: float
        ビルのY座標（手前端）
    z_pos: float
        ビルのZ座標（底面）
    width: float
        ビルの幅（X方向のサイズ）
    depth: float
        ビルの奥行き（Y方向のサイズ）
    floor_height: float
        各階の高さ
    num_floors: int
        ビルの階数
    target_data: list
        生成したオブジェクトデータを追加するリスト
    """
    print(f'Creating building at ({x_pos}, {y_pos}) with size {width}x{depth}, {num_floors} floors')

    # 各階ごとに処理
    for floor in range(num_floors):
        # Y軸方向の繰り返し（手前と奥の2点）
        for j in range(2):
            # X軸方向の繰り返し（左と右の2点）
            for i in range(2):
                if j < 1:
                    # Y方向の梁（床の横方向の支え）
                    beam_y_pos = (
                    i * (width - 0.5) + x_pos, 0.5 + y_pos, (floor_height - 1) + floor * floor_height + z_pos)
                    beam_y_scale = (0.5, depth - 1, 1)
                    target_data.append({
                        'type': 'cube',
                        'pos': beam_y_pos,
                        'scale': beam_y_scale,
                        'color': (1, 0, 0),  # 赤色
                        'mass': 1
                    })

                if i < 1:
                    # X方向の梁（床の縦方向の支え）
                    beam_x_pos = (
                    0 + x_pos, j * (depth - 0.5) + y_pos, (floor_height - 1) + floor * floor_height + z_pos)
                    beam_x_scale = (width, 0.5, 1)
                    target_data.append({
                        'type': 'cube',
                        'pos': beam_x_pos,
                        'scale': beam_x_scale,
                        'color': (1, 0, 0),  # 赤色
                        'mass': 1
                    })

                # 柱の作成（建物の四隅に立つ支柱）
                column_pos = (i * (width - 1) + x_pos, j * (depth - 1) + y_pos, floor * floor_height + z_pos)
                column_scale = (1, 1, floor_height - 1)

                # 柱の色は位置と階数に応じて変化
                # i, j: 0または1（位置による色の変化）
                # floor/num_floors: 階数が上がるほど明るく
                target_data.append({
                    'type': 'cube',
                    'pos': column_pos,
                    'scale': column_scale,
                    'color': (i, j, floor / num_floors),
                    'mass': 1
                })

# 都市全体に区画を配置
district_x = 0  # 区画のX座標（左からの位置）
district_y = 0  # 区画のY座標（手前からの位置）

# 区画を配置（2行×4列）
for row in range(DISTRICT_ROWS):
    for col in range(DISTRICTS_PER_ROW):
        # 区画テンプレートからランダムに選択
        selected_district = random.choice(district_templates)

        # 区画内のすべてのビルを生成
        for building_data in selected_district['buildings']:
            # ビルの各パラメータを取得
            building_width, building_depth = building_data['size']
            building_x, building_y = building_data['pos']
            floor_count = building_data['floor_num']

            # 階高をランダムに決定
            floor_height = random.randint(MIN_FLOOR_HEIGHT, MAX_FLOOR_HEIGHT)

            # 区画内での相対座標を全体座標に変換
            absolute_x = building_x + district_x
            absolute_y = building_y + district_y
            base_z = 0  # 地面レベル

            # ビルを生成
            create_building(absolute_x, absolute_y, base_z, building_width, building_depth, floor_height, floor_count,
                            body_data)

        # 次の区画のX座標を更新（区画の幅 + 間隔）
        district_x += selected_district['size'][0]

    # 行の最後に達したらX座標をリセットしてY座標を更新
    district_x = 0
    district_y += 60  # 各行の間隔は50単位

print(f"都市の生成完了: {len(body_data)}個のオブジェクトを作成しました")

# # 隕石を生成
# body_data.append({
#     'type': 'sphere',
#     'pos': (CITY_WIDTH / 2, CITY_LENGTH / 2, 200),
#     'scale': (50, 50, 50),
#     'color': (1, 1, 1),
#     'mass': 1000,
#     'base_point': 2,
#     'vec': (0, 0, -100),
# })

# ボーリングのボールを生成
body_data.append({
    'type': 'sphere',
    'pos': (-200, 50, 25),
    'scale': (50, 50, 50),
    'color': (1, 1, 1),
    'mass': 1000,
    'base_point': 2,
    'vec': (100, 0, 0),
})
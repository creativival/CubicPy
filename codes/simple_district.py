import random

# 全体のオブジェクトデータを格納するリスト
body_data = []

# 区画の定義
district = {
  'size': (25, 40),  # 区画のサイズ (幅, 奥行き)
  'buildings': [
    {
      'size': (10, 15),  # ビルのサイズ (幅, 奥行き)
      'pos': (0, 0),  # 区画内の位置 (x, y)
      'num_floors': 5  # 階数
    },
    {
      'size': (10, 15), 'pos': (12, 0), 'num_floors': 4
    },
    {
      'size': (10, 15), 'pos': (0, 20), 'num_floors': 6
    },
    {
      'size': (10, 15), 'pos': (12, 20), 'num_floors': 3
    },
  ]
}


def create_building(x_pos, y_pos, z_pos, width, depth, floor_height, num_floors, target_data):
  # (前述の関数と同じコード)
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


# 区画内のすべてのビルを生成
for building_data in district['buildings']:
  # ビルの各パラメータを取得
  building_width, building_depth = building_data['size']
  building_x, building_y = building_data['pos']
  num_floors = building_data['num_floors']

  # 階高をランダムに決定
  floor_height = random.randint(5, 8)

  # ビルを生成
  create_building(building_x, building_y, 0, building_width, building_depth, floor_height, num_floors, body_data)
import math

body_data = []


# 直線ドミノを配置する関数
def create_line_dominoes(start_pos, length, direction_angle, spacing, color, target_data, start_line=False):
    direction_rad = math.radians(direction_angle)
    dx = math.cos(direction_rad) * spacing
    dy = math.sin(direction_rad) * spacing

    # ドミノの数を計算
    num_dominoes = int(length / spacing)

    for i in range(num_dominoes):
        x_pos = start_pos[0] + i * dx
        y_pos = start_pos[1] + i * dy

        target_data.append({
            'type': 'cube',
            'pos': (x_pos, y_pos, 0),
            'scale': (0.2, 0.5, 2),  # ドミノのサイズ
            'color': color,
            'mass': 10 if start_line and i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
            'hpr': (direction_angle, 0, 0),
            'base_point': 1,
            'velocity': (2, 0, 0) if start_line and i == 0 else (0, 0, 0),
        })

    # 最後のドミノの位置を返す（連結用）
    return (start_pos[0] + (num_dominoes - 1) * dx, start_pos[1] + (num_dominoes - 1) * dy)


# 円弧状のドミノを配置する関数
def create_arc_dominoes(center, radius, start_angle, end_angle, color, target_data):
    # 角度範囲内でドミノを配置
    current_angle = start_angle
    points = []
    step_angle = math.degrees(math.atan2(1.2, radius))  # ドミノの間隔を決定するステップ角度

    # 開始角度が終了角度より大きく、ステップが正の場合
    if start_angle > end_angle and step_angle > 0:
        # 終了角度を調整
        end_angle += 360

    while current_angle <= end_angle:
        rad_angle = math.radians(current_angle)
        x_pos = center[0] + radius * math.cos(rad_angle)
        y_pos = center[1] + radius * math.sin(rad_angle)

        target_data.append({
            'type': 'cube',
            'pos': (x_pos, y_pos, 0),
            'scale': (0.2, 0.5, 2),  # ドミノのサイズ
            'color': color,
            'mass': 1,
            'hpr': (current_angle + 90, 0, 0),  # 円の接線方向
            'base_point': 1
        })

        points.append((x_pos, y_pos))
        current_angle += step_angle

    # リストが空かチェック
    if not points:
        print("警告: 角度範囲内にドミノが配置されませんでした")
        return (center[0], center[1]), (center[0], center[1])  # デフォルト値を返す

    return points[0], points[-1]


# 複合パターン：「S」字型のドミノ配列
def create_s_pattern(start_pos, length, width, color, target_data, _create_line_dominoes=create_line_dominoes, _create_arc_dominoes=create_arc_dominoes):
    print("create_s_pattern")
    # 最初の直線
    line1_end = _create_line_dominoes(start_pos, length / 2, 0, 1, color, target_data, start_line=True)
    line1_end = (line1_end[0] + 0.8, line1_end[1])

    # 上部の円弧
    arc1_start, arc1_end = _create_arc_dominoes(
        (line1_end[0], line1_end[1] + width / 2),
        width / 2,
        270,
        90,
        color,
        target_data
    )

    # 中央の直線
    line2_start = (arc1_end[0] - 0.8, arc1_end[1])
    line2_end = _create_line_dominoes(line2_start, length / 2, 180, 0.8, color, target_data)
    line2_end = (line2_end[0] - 1, line2_end[1])

    # 下部の円弧
    arc2_start, arc2_end = _create_arc_dominoes(
        (line2_end[0], line2_end[1] - width),
        width,
        90,
        180,
        color,
        target_data
    )

    # 最後の直線
    line3_start = (arc2_end[0], arc2_end[1] - 0.8)
    line3_end = _create_line_dominoes(line3_start, length / 2, 270, 0.8, color, target_data)

    return line3_end

# U字L字接続パターン
u_l_end = create_s_pattern((0, 0), 20, 10, (0.8, 0.2, 0.2), body_data)
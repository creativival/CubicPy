# 第5回：キューブドミノ倒し選手権

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**一押しで連鎖反応！最後まで倒れるかドキドキの瞬間を作り出せ！**

## 前回のおさらい

前回は街を作り、隕石で破壊する壮大なシミュレーションを行いました。関数を使って効率的にビルを生成し、ランダム性を取り入れることで都市をよりリアルに表現しましたね。

今回はスケールを変えて、「ドミノ倒し」という繊細かつダイナミックな連鎖反応の世界に挑戦します！一つの小さな動きが次々と伝わり、最後まで倒れるかどうかのスリルを体験しましょう。

## ドミノの安定性と配置の秘訣

### ドミノ倒しの物理学

ドミノ倒しを成功させるには、物理の基本原理を理解することが重要です。

1. **重心**：ドミノの安定性は重心の位置で決まります。底面の中心から重心までの水平距離が短いほど安定します。
2. **接触角度**：ドミノ同士の角度と間隔が連鎖の成否を左右します。
3. **摩擦**：床との摩擦が少なすぎると滑ってしまい、連鎖が途切れることがあります。

### 最初の一歩：単純な直線ドミノ

まずは基本的な直線状のドミノ配列から始めましょう。simple_domino.py という名前で新しいファイルを作成し、以下のコードを入力してください。

```python
body_data = []

# ドミノの設定
domino_width = 0.5
domino_height = 2.0
domino_thickness = 0.2
spacing = 0.8  # ドミノ間の距離
num_dominoes = 20

# 直線上にドミノを配置
for i in range(num_dominoes):
    # 各ドミノの位置を計算
    x_pos = i * spacing
    y_pos = 0
    z_pos = 0  # 地面にドミノの底面が接するように

    # ドミノを追加
    body_data.append({
        'type': 'cube',
        'pos': (x_pos, y_pos, 0),  # 位置（高さは半分の位置）
        'scale': (domino_thickness, domino_width, domino_height),
        'color': (i / num_dominoes, 1, 1 - i / num_dominoes),  # グラデーション
        'mass': 10 if i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
        'base_point': 1,  # 中心を基準に配置
        'velocity': (2, 0, 0) if i == 0 else (0, 0, 0),  # X軸方向（右）に発射
    })
```

「0.2 x 0.5 x 2.0」サイズのドミノを直線に並べました（▲図1▲）。このコードを保存して実行してみましょう。

```bash
cubicpy simple_domino.py
```

![Simple Domino](https://creativival.github.io/CubicPy/assets/simple_domino.png)

**▲図1▲ 基本的な直線ドミノと発射ボール**

3D世界が表示されたら、スペースキーを押してボールを発射してみてください。上手くいけば、ボールが最初のドミノに当たり、それが次々と倒れていくでしょう。

> 💡 **先生からのヒント**: ドミノが倒れない場合は、`spacing`（ドミノ間の距離）を調整してみよう。近すぎると最初から倒れてしまい、遠すぎると連鎖が途切れてしまうよ！

### ドミノ配置の重要なパラメータ

ドミノの連鎖を成功させるためには、以下のパラメータのバランスが重要です。

1. **ドミノの高さと厚さの比率**：一般的に、高さが厚さの8〜10倍程度あると安定します。
2. **ドミノ間の距離**：ドミノの高さのおよそ1/2〜3/4が理想的です。
3. **ドミノの重さ**：重すぎると次のドミノを倒す力が弱まり、軽すぎると風や振動で倒れやすくなります。

## for文を駆使した複雑なドミノ配列の生成

直線上のドミノは基本ですが、もっと面白い配置にも挑戦してみましょう。for文を使って様々なパターンを作ることができます。

### 円形のドミノ配列

circular_domino.py という名前で新しいファイルを作成し、次のコードを入力しましょう。

```python
import math

body_data = []

# ドミノの設定
domino_width = 0.5
domino_height = 2.0
domino_thickness = 0.2
radius = 10.0  # 円の半径
num_dominoes = 60  # ドミノの数

# 円形にドミノを配置
angle = -math.pi / 2  # 初期角度
for i in range(num_dominoes):
    # 円周上の位置を計算
    angle += 2 * math.pi / num_dominoes  # 角度（ラジアン）
    x_pos = radius * math.cos(angle)
    y_pos = radius * math.sin(angle) + radius

    # ドミノを円の中心に向けて配置
    body_data.append({
        'type': 'cube',
        'pos': (x_pos, y_pos, 0),
        'scale': (domino_thickness, domino_width, domino_height),
        'color': (i / num_dominoes, 1 - i / num_dominoes, 1),  # グラデーション
        'mass': 10 if i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
        'hpr': (math.degrees(angle + math.pi / 2), 0, 0),  # 角度を度数に変換して設定
        'base_point': 1,  # 中心を基準に配置
        'velocity': (2, 0, 0) if i == 0 else (0, 0, 0),  # X軸方向（右）に発射
    })
```

このコードでは、円形にドミノを配置し、中心から外向きにドミノが倒れていくシミュレーションになります（▲図2▲）。スペースキーを押すと、上空から球が落下し、中心から放射状にドミノが倒れていきます。次のコマンドを実行します。

```bash
cubicpy circular_domino.py
```

![Circular Domino](https://creativival.github.io/CubicPy/assets/circular_domino.png)

**▲図2▲ 円形に配置されたドミノ**

> 🔍 **発見ポイント**: `hpr`パラメータをうまく使うと、ドミノを任意の方向に向けることができるよ。円形の配列では、各ドミノが円の中心を向くように角度を調整しているんだ。

### 螺旋状のドミノ配列

さらに複雑な例として、螺旋状のドミノ配列を作ってみましょう。spiral_domino.py という名前でファイルを作成し、次のコードを入力してください。

```python
import math

body_data = []

# ドミノの設定
domino_width = 0.5
domino_height = 2.0
domino_thickness = 0.2
radius = 10.0  # 円の半径
num_dominoes = 180  # ドミノの数

# 円形にドミノを配置
angle = -math.pi / 2  # 初期角度
for i in range(num_dominoes):
    # ドミノの半径を少しずつ増やす
    spiral_radius = radius * (1.005 ** i)

    # 円周上の位置を計算
    angle += math.atan2(1.0, spiral_radius)  # 角度（ラジアン）
    x_pos = spiral_radius * math.cos(angle)
    y_pos = spiral_radius * math.sin(angle) + radius

    # ドミノを円の中心に向けて配置
    body_data.append({
        'type': 'cube',
        'pos': (x_pos, y_pos, 0),
        'scale': (domino_thickness, domino_width, domino_height),
        'color': (i / num_dominoes, 1 - i / num_dominoes, 0),  # グラデーション
        'mass': 10 if i == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
        'hpr': (math.degrees(angle + math.pi / 2), 0, 0),  # 角度を度数に変換して設定
        'base_point': 1,  # 中心を基準に配置
        'velocity': (2, 0, 0) if i == 0 else (0, 0, 0),  # X軸方向（右）に発射
    })
```

螺旋パターンでは、各ドミノが螺旋カーブに沿って配置されます（▲図3▲）。円周の半径によりドミノの間隔を調整し、螺旋が均等に広がるようにしています。次のコマンドを実行します。

```bash
cubicpy spiral_domino.py
```

![Spiral Domino](https://creativival.github.io/CubicPy/assets/spiral_domino.png)

**▲図3▲ 螺旋状に配置されたドミノ**

> 💡 **先生からのヒント**: 半径や角度の増加率を調整すれば、緩やかな螺旋や急な螺旋など、様々な形を作れるよ！

## 崩壊連鎖のデザインパターン

ドミノ倒しの醍醐味は、複数のパターンを組み合わせて大規模な連鎖反応を作ることです。ここでは、いくつかの代表的なデザインパターンを紹介します。

### ドミノ配置関数の作成

複雑なドミノアートを作るには、まず基本的なパターンを関数化しておくと便利です。domino_patterns.py という名前で新しいファイルを作成し、次のコードを入力してください。

```python
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

# ここに続きのパターンを追加
```

このコードでは、直線、円弧の基本パターンを関数化し、それらを組み合わせて「U」字型、「L」地形などの複雑なパターンも作れるようにしています（▲図4▲）。次のコードを実行して、ドミノの配置を確認してみましょう。

```bash
cubicpy domino_patterns.py
```

![Domino Patterns](https://creativival.github.io/CubicPy/assets/domino_patterns.png)

**▲図4▲ 複数のパターンを組み合わせたドミノ配列**

> 🚀 **すごいね！**: 関数を使って部品化することで、複雑なドミノアートもパズルのように組み立てられるようになったよ！これがプログラミングの強みだね。

### 崩壊連鎖の設計ポイント

大規模なドミノ倒しを設計する際のポイントをいくつか紹介します。

1. **橋渡し**: パターン間を繋ぐ部分は特に注意が必要です。連鎖が途切れないように間隔を調整しましょう。`line1_end = (line1_end[0] + 0.8, line1_end[1])`
   のように、次のドミノの位置を調整することで、連鎖が途切れないようにしています。
2. **加速と減速**: 直線部分では加速し、カーブでは減速します。カーブの外側のドミノは間隔を広く取ると良いでしょう。

## 大規模ドミノ挑戦：リストパターン

最後に、より複雑で大規模なドミノ配置に挑戦してみましょう。list_pattern_domino.py という名前でファイルを作成し、次のコードを入力してください。

```python
body_data = []

# 迷路のサイズとパターン
list_pattern = [
    "000000000011111111111",
    "000000000100000000000",
    "000000001000000000000",
    "000000010000000000000",
    "000000101000000000000",
    "000001000100000000000",
    "000010000011111111111",
    "000100000000000000000",
    "001000000000000000000",
    "010000000000000000000",
    "100000000000000000000",
    "010000000000000000000",
    "001000000000000000000",
    "000100000000000000000",
    "000010000011111111111",
    "000001000100000000000",
    "000000101000000000000",
    "000000010000000000000",
    "000000001000000000000",
    "000000000100000000000",
    "000000000011111111111",
]

# ドミノの設定
spacing = 1.0  # ドミノ間の距離
domino_width = 1.0
domino_height = 2.0
domino_thickness = 0.2

# リストからドミノの配置を生成
num_list = len(list_pattern)
for i, row in enumerate(list_pattern):
    y = (num_list - i - 1) * domino_width / 2   # 上から下に向かうため、y座標を反転
    print(y, row)

    for j, dot in enumerate(list(row)):
        print(dot)
        if dot == '1':
            body_data.append({
                'type': 'cube',
                'pos': (j * spacing, y, 0),
                'scale': (domino_thickness, domino_width, domino_height),
                'color': (1, 0, 0),
                'mass': 10 if j == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
                'velocity': (2, 0, 0) if j == 0 else (0, 0, 0),
            })
```

このコードでは、テキストで定義されたリストパターンに沿ってドミノを配置しています（▲図5▲）。ドミノは配置は「0」「1」のドットで表現され、1の部分にドミノが配置されます。迷路のような形状を作ることができます。次のコードを実行します。

```bash
cubicpy list_pattern_domino.py
```

このコードを実行すると、迷路の形にドミノが配置され、最初のドミノを倒すためのボールが用意されます。スペースキーを押すと、迷路の通路に沿ってドミノが連鎖的に倒れていきます。

![List Pattern Domino](https://creativival.github.io/CubicPy/assets/list_pattern_domino.png)

**▲図5▲ 迷路パターンに配置されたドミノ**

> 🔍 **発見ポイント**: テキストで通路を定義し、それを物理的なドミノの配置に変換するというのは、データの表現方法の変換という重要なプログラミングの概念だよ。これはデータの視覚化の一例でもあるんだ！

## チャレンジ：最も複雑で美しいドミノ倒しを設計しよう

今回学んだ技術を使って、オリジナルのドミノ倒しを設計してみましょう！以下のようなアイデアを試してみてください。

1. **複合パターン**: 直線、円形、螺旋、階段などを組み合わせた独自のパターンを作る
2. **複数経路**: 一つのドミノから複数の経路に分岐させる
3. **色の変化**: パターンごとに色を変えたり、グラデーションを設定する
4. **サイズの変化**: 徐々に大きくなるドミノ、または小さくなるドミノの連鎖
5. **メッセージや絵**: ドミノを文字や絵の形に配置する
6. **ループとタイミング**: 複数の経路が特定の場所で合流するように設計する

## デバッグのコツ

大規模なドミノ配列を作る際には、いくつかの問題が発生することがあります。ここでは、よくある問題の解決方法を紹介します。

1. **途中で止まる**:
   - ドミノ間の距離を短くしてみる
   - ドミノを少し傾けて配置する（初期状態で不安定にする）
   - ドミノの高さと厚さの比率を調整する

2. **最初から倒れてしまう**:
   - 重力係数を下げて実行する（`cubicpy -g 0.1 your_file.py`）
   - ドミノ間の距離を広げる
   - 質量を小さくする

3. **方向がおかしい**:
   - `hpr`の角度を確認する
   - 円形や曲線の配置では接線方向にドミノを向ける

4. **処理が重い**:
   - ドミノの総数を減らす
   - 細かいパターンよりも、単純な直線や曲線を優先する

## まとめ：今回学んだこと

1. **ドミノの物理学**: 安定性、接触角度、摩擦などの基本原理を理解しました
2. **パターン設計**: 直線、円形、螺旋、複合パターンなど様々な配置方法を学びました
3. **関数化**: パターンを関数として実装し、再利用可能にする技術を身につけました
4. **大規模設計**: 迷路のような複雑なパターンの実装方法を学びました
5. **デバッグ技術**: ドミノが正しく倒れるように調整するコツを習得しました

これらの技術を組み合わせることで、自分だけのユニークなドミノ倒しシミュレーションを作ることができます。

## 次回予告

次回は「発射体でボーリングゲームを作ろう！」です。物理シミュレーションの世界をさらに広げ、ボーリングのピンとボールを作り、得点計算までできるゲームプログラムに挑戦します。力と角度を調整して、完璧なストライクを目指しましょう！

> 🎮 **宿題（やってみよう）**: 今回学んだパターンを組み合わせて、100個以上のドミノを使った大規模な連鎖反応を設計してみよう。最後まで倒れるように工夫し、途中で止まらないようにチャレンジしてみよう！

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
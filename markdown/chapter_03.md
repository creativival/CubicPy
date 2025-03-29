# 第3回：様々な形の3D建築を作ろう！

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**Pythonコードと数学の知識を使って、幾何学形状の建物を作れる魔法を学ぼう！**

## 前回のおさらい

前回は最初のキューブタワーを作りました。for文を使って箱を積み上げる方法と、色を変えるテクニックを学びましたね。今回はもっと複雑で面白い形の建物を作っていきます！

## いろんな形の建物を作ろう

キューブを積み上げるだけでも、実はいろんな形が作れるんです。今日は3つの特別な建築物を作る方法を学びましょう。

1. 円柱タワー - 円形に並べたブロックを積み上げて作る塔
2. コラム構造のビル - 柱（柱=縦棒）と梁（はり=横棒）で作る本格的な高層建築
3. 天空のピラミッド - 数式を使って美しい立体構造を作る

それぞれのコードを見ながら、どうやって作るのか一緒に考えていきましょう！

## 円柱タワーを作ろう

まずは円形に箱を並べて、円柱のような塔を作ってみましょう。

円柱タワーのコードはこんな感じです。少し難しく見えるかもしれませんが、一緒に理解していきましょう！box_cylinder_shape_tower.py という名前で保存してください。

```python
from math import atan, cos, sin, pi, degrees

body_data = []
radius = 10  # 円の半径
height = 40  # 塔の高さ
box_size = 1  # キューブのサイズ

# キューブの半径と高さから、ボックスの数を決定
half_size = box_size / 2
half_angle = atan(half_size / (radius - box_size))
box_num = int(pi / half_angle)

# キューブを配置するための基準角度
base_angle = pi * 2 / box_num

# 塔の高さ分だけキューブを配置
for j in range(height):
    for i in range(box_num):
        # 偶数段と奇数段で角度を調整
        if j % 2 == 0:
            angle = base_angle * (i + 1 / 2)
        else:
            angle = base_angle * i

        # キューブの位置を計算
        x = radius * cos(angle)
        y = radius * sin(angle)
        z = j * box_size

        pos = (x, y, z)  # ボックスの下端がZ=0から始まるように調整
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (box_size, box_size, box_size),  # X方向の幅とZ方向の高さを適切に設定
            'color': (j / height, 0, 1 - j / height),  # 塔の高さに応じて色を変える
            'mass': 1,
            'hpr': (degrees(angle), 0, 0),  # キューブを配置した角度で回転させる
            'base_point': 1  # キューブの底の中心を基準点に設定
        })
```

### コードの解説

この円柱タワーのコードのポイントを解説します。

1. **数学の関数を使う**: `from math import...` の部分で、円を作るために必要な数学関数を読み込んでいます。
   
2. **円の計算**: 円周上に箱を並べるには、三角関数（サイン・コサイン）を使います。三角関数と角度を使って、 (x, y) の位置を計算できます（▲図1▲）。

![Cube Position](https://creativival.github.io/CubicPy/assets/cube_position.png)

**▲図1▲ 角度からキューブの位置を計算する**

3. **偶数段と奇数段**: `if j % 2 == 0:` の部分で、偶数段と奇数段で箱の位置をずらしています。これによって、箱が交互に積み上がります（▲図2▲）。

![Stacking Cubes](https://creativival.github.io/CubicPy/assets/how_to_stack_cubes.png)

**▲図2▲ 偶数段と奇数段でキューブの配置を半分ずらして積み上げる**

4. **箱の向き**: `hpr` パラメータで箱の向きを設定しています。これにより、すべての箱が円の中心を向くようになります（▲図3▲）。
  - `hpr`: Heading, Pitch, Roll の略で、Y軸、X軸、Z軸の回転角度を表します。

![Column Building](https://creativival.github.io/CubicPy/assets/rotate_cube_add_angle.png)

**▲図3▲ キューブを「位置の角度」で回転させることで中心に向ける**

5. **基準点の設定**: `base_point: 1` の部分で、キューブの底の中心を基準点に設定しています。これにより、キューブが円周上に正確に配置されます（▲図3▲）。
  - `base_point` は、0: 原点に近い角が基準、1: 底面の中心が基準、2: 立方体の重心が基準 という意味です。通常の建築では、初期値（0）のままで問題ありませんが、円柱のような形状を作るときは、底面の中心（1）を基準にすると計算が簡単になります。

5. **色の変化**: `color: (j / height, 0, 1 - j / height)` の部分で、下から上に向かって赤から青へのグラデーションを作っています（▲図4▲）。

![Cylinder Tower](https://creativival.github.io/CubicPy/assets/box_cylinder_shape_tower.png)

**▲図4▲ 箱を円形に配置した円柱タワー**

> 💡 **先生からのヒント**: 円柱タワーのコードは少し難しいけど、半径を変えたり、高さを変えたりして実験してみよう。いろんな形の塔ができるよ！

## コラム構造のビルを作ろう

次は、本格的な高層ビルのような建物を作ってみましょう。柱（コラム）と梁（ビーム）で構成される建築物です。この建築物の構想を「フレーム構造」と呼びます。

![Column Building](https://creativival.github.io/CubicPy/assets/column_building_2x2_sample.png)

**▲図5▲ 柱と床で構成されたフレーム構造ビル**

コラム構造のビルのコードはこちらです。frame_building_2x2.py という名前で保存してください。

```python
body_data = []
step_num = 10  # 階数

# Z軸
for k in range(step_num):
    # Y軸
    for j in range(2):
        # X軸
        for i in range(2):
            if j < 1:
                # Y方向の梁
                pos_y_beam = (i * 9.5, 0.5, 9 + k * 10)
                scale_y_beam = (0.5, 9, 1)
                body_data.append({
                    'type': 'cube',
                    'pos': pos_y_beam,
                    'scale': scale_y_beam,
                    'color': (1, 0, 0),
                    'mass': 1
                })

            if i < 1:
                # X方向の梁
                pos_x_beam = (0, j * 9.5, 9 + k * 10)
                scale_x_beam = (10, 0.5, 1)
                body_data.append({
                    'type': 'cube',
                    'pos': pos_x_beam,
                    'scale': scale_x_beam,
                    'color': (1, 0, 0),
                    'mass': 1
                })

            # 柱の作成
            pos_beam = (i * 9, j * 9, k * 10)
            scale_beam = (1, 1, 9)
            body_data.append({
                'type': 'cube',
                'pos': pos_beam,
                'scale': scale_beam,
                'color': (i, j, k /step_num),
                'mass': 1
            })
```

### コードの解説

コラム構造のビルを作るコードのポイントを解説します。

1. **3重ループ**: 階数(k)、Y軸方向(j)、X軸方向(i)の3重ループで建物全体を作っています（▲図5▲）。

2. **柱と梁**: 
   - `scale_beam = (1, 1, 9)` の部分で柱を作っています。高さが9の細長い箱です。
   - `scale_y_beam = (0.5, 9, 1)` と `scale_x_beam = (10, 0.5, 1)` で梁（床）を作っています。

3. **位置の計算**:
   - 柱の位置は `pos_beam = (i * 9, j * 9, k * 10)` で計算しています。
   - 床の位置は柱の上部に合わせて調整しています。

4. **色の設定**:
   - 柱の色は位置によって変わります: `color: (i, j, k / step_num)`
   - 床はすべて赤色: `color: (1, 0, 0)`

> 🏗️ **建築のコツ**: 建物のサイズを変えたいときは、`pos_beam`、`pos_y_beam`、`pos_x_beam` の計算式を調整しよう。例えば、`i * 9` の `9` を大きくすると柱と柱の間隔が広がるよ！

## 天空のピラミッドを作ろう

最後に、幾何学的な美しさを持つピラミッド型のフレーム構造を作ります。

![Pyramid Frame](https://creativival.github.io/CubicPy/assets/cube_pyramid_frame.png)

**▲図6▲ ピラミッドのフレーム構造**

ピラミッドのコードはこちらです。cube_pyramid_frame.py という名前で保存してください。

```python
from math import sqrt

body_data = []
step_num = 20  # 段数

# ピラミッドの各辺を作成
for i in range(step_num):
    # 数学的に正確なピラミッドの形を計算
    x = (step_num - (i + 1)) / sqrt(3)
    y = x
    z = i
    
    # 4つの辺を作成
    pos = (x, y, z)
    body_data.append({
        'type': 'box',
        'pos': pos,
        'scale': (1, 1, 1),
        'color': (1, 0, 0),
        'mass': 1
    })

    # 頂点以外の場所では、残りの3辺も作成
    if i != step_num - 1:
        pos = (-x, y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })

        pos = (x, -y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })

        pos = (-x, -y, z)
        body_data.append({
            'type': 'box',
            'pos': pos,
            'scale': (1, 1, 1),
            'color': (1, 0, 0),
            'mass': 1
        })
```

### コードの解説

ピラミッドフレームを作るコードのポイントを解説します。

1. **数学的な計算**: `from math import sqrt` で平方根の関数を読み込み、ピラミッドの傾きを計算しています。

2. **ピラミッドの形状**: 
   - `x = (step_num - (i + 1)) / sqrt(3)` の計算で、各段の横幅が徐々に小さくなるようにしています。
   - `sqrt(3)` で割ることで、正確な四角錐の形になります。

3. **4つの辺**: 一つの高さ(z)に対して、4つの座標(x, y)、(-x, y)、(x, -y)、(-x, -y)を計算し、ピラミッドの四角形の各頂点を作っています。

4. **頂点の処理**: `if i != step_num - 1:` の条件で、ピラミッドの頂点では1つだけブロックを置くようにしています。

> 🔍 **発見ポイント**: ピラミッドのサイズを変えたいときは `step_num` の値を変えてみよう。大きくすると高いピラミッドに、小さくするとコンパクトなピラミッドになるよ！

## プログラムの実行方法

作成したプログラムを実行するには、前回と同じようにファイルを作成して保存し、`cubicpy`コマンドで実行します。

1. テキストエディタ（メモ帳やVisual Studio Codeなど）で新しいファイルを作成
2. コピーしたコードを貼り付ける
3. 適当な名前（例: `my_cylinder_tower.py`）で保存
4. PowerShellまたはターミナルで次のコマンドを実行:

```bash
cubicpy my_cylinder_tower.py
```

## 応用編：建物を自由にカスタマイズしよう

これまで紹介したコードを元に、自分だけの建物を作ってみましょう。以下のようなアイデアはいかがでしょうか？

1. **円柱タワーをカスタマイズ**:
   - `radius` の値を変えて、太い塔や細い塔を作る
   - `height` を変えて、超高層タワーを作る
   - 色の計算式を変えて、別の色のグラデーションにする
   - `radius`　を徐々に小さくすることで、円錐タワーを作る

2. **コラム構造ビルをカスタマイズ**:
   - `step_num` を増やして超高層ビルにする
   - 柱の数を増やす（`range(2)` を `range(3)` や `range(4)` に変更）
   - 柱や床の色を階数によって変える

3. **ピラミッドをカスタマイズ**:
   - 色を変える（例: `color: (0, i/step_num, 0)` で緑のグラデーション）
   - 箱のサイズを変える（例: `scale: (0.5, 0.5, 0.5)` でより細かいフレーム）
   - 複数のピラミッドを異なる位置に配置する

## チャレンジ：複合建築物を設計しよう

今回学んだ技術を組み合わせて、オリジナルの複合建築物を作ってみましょう！

**チャレンジ例**:
1. 円柱タワーの上に円錐タワーを置く「城の尖塔」
2. コラム構造ビルを複数並べて「未来都市」を作る
3. 円柱と壁を組み合わせた「西欧風のお城」

### ヒント

複合建築物を作るときは、各部分のコードを1つのファイルに結合し、位置を調整するのがコツです。例えば:

```python
# 円柱タワーのコード
# ...（円柱タワーのコード）...

# 位置をずらしてピラミッドを追加
for i in range(step_num):
    x = (step_num - (i + 1)) / sqrt(3)
    y = x
    # 円柱の高さ分だけz座標をずらす
    z = i + height  # heightは円柱の高さ
    # ...（以下ピラミッドのコード）...
```

## 次回予告

次回は「衝撃の物理実験室①〜落下破壊実験〜」です。巨大ボールを使って、今日作った建物を粉々に破壊する方法を学びますよ！物理の力を使った破壊の美学を体験しましょう。

> 🎮 **宿題（やってみよう）**: 今回学んだ3つの建築物のどれかを改造してみよう。パラメータを変えたり、色を工夫したりして、自分だけのオリジナル建築を作ってみよう！

## デバッグのコツ

もしエラーが出たり、思ったような形にならない場合は:

- 数値を少しずつ変えて実験してみる（急激な変更は予想外の結果になることも）
- `print()` 文を使って、計算結果を確認してみる
- コードを分けて、部分ごとに実行してみる

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
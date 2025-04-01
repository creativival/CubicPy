# 第4回：街を作って、隕石で破壊しよう！

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**自分だけの3D都市を作って、巨大な隕石で粉々に粉砕する！**

## 前回のおさらい

前回は様々な3D建築物を作る方法を学びました。円柱タワー、コラム構造のビル、そしてピラミッド型の建築物など、複雑な形を作るテクニックを習得しましたね。

今回はもっと大きなスケールで考えます。一つの建物ではなく、街全体を作り出します！最後に隕石の衝突による壮大な破壊を体験しましょう！

## 関数を使ってビルを簡単に作るテクニック

前回は個別のビルを作りましたが、複数のビルを効率よく作るには「関数」という便利な魔法を使います。関数とは、一連の処理をまとめて名前を付け、何度でも呼び出せるようにするものです。

### 関数とは？

プログラミングにおける関数は、料理のレシピのようなものです。材料（引数）を指定して関数を呼び出すと、決められた手順で処理が行われ、結果が得られます。

たとえば、「カレーを作る」という関数があれば、材料（肉の種類、野菜の量など）を変えるだけで、いろいろな種類のカレーを簡単に作れます。関数を使うことで、同じコードを何度も書く必要がなくなり、効率よくプログラミングできるのです。

### ビルを作る関数を作ろう

まずは、コラム構造のビル（柱と床で構成された建物）を簡単に作るための関数を作りましょう。five_buildings.py という名前で新しいファイルを作成し、以下のコードを入力してください。

```python
import random

# グローバル変数として最初に定義
body_data = []


def create_building(x_pos, y_pos, z_pos, width, depth, floor_height, num_floors, target_data):
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

# ランダムな位置と大きさでビル5棟を生成
shift_x = 0
for _ in range(5):
    pos_x = random.randint(0, 15) + shift_x
    pos_y = random.randint(0, 15)
    pos_z = 0
    building_width = random.randint(15, 35)
    building_depth = random.randint(15, 55)
    floor_height = random.randint(5, 10)
    num_floors = random.randint(3, 8)

    create_building(pos_x, pos_y, pos_z, building_width, building_depth, floor_height, num_floors, body_data)

    shift_x += 50
```

### コードの解説

このコードでは、`create_buildings`という関数を定義しています。この関数は、以下のパラメータを受け取ります。

1. `x_pos`, `y_pos`, `z_pos`: ビルを配置する基準位置
2. `width`, `depth`: ビルの幅と奥行き
3. `floor_height`: 各階の高さ
4. `num_floors`: 階数
5. `target_data`: オブジェクトデータを追加するリスト

関数の中では、コラム構造のビルを作るコードが入っていますが、これらのパラメータを使うことで、大きさや位置、階数の異なるビルを簡単に作れるようになりました。

> 💡 **先生からのヒント**: 関数は「魔法の呪文集」のようなものだよ。一度呪文を覚えておけば（関数を定義しておけば）、簡単に何度でも呼び出せるんだ！

このコードの最後では、`random`モジュールを使って、ランダムな位置と大きさのビルを5棟生成しています（▲図1▲）。ビル同士がぶつからないように、shift_xを使って、一棟ずつX座標にずらして建築しています。

`random`モジュールを使うと、ビルの位置やサイズを毎回ランダムに決められます！ このコードを実行するたびに、異なるビル群が生成されるので、毎回新鮮な景色を楽しめます。

`random`は「クリエイティブコーディング」と呼ばれる分野でもよく使われており、 偶然性を活かしたデザインやシミュレーションに最適な道具です。

five_buildings.pyを保存して実行すると、ランダムな位置と大きさのビルが5棟生成されます。以下のコマンドを実行してください。「-g 0.1」は、重力を0.1倍にするオプションです。これにより、ビルがが自重で崩壊することを防ぎます。

```bash
cubicpy -g 0.1 five_buildings.py
```

![Random Buildings](https://creativival.github.io/CubicPy/assets/five_random_buildings.png)

**▲図1▲ ランダムな位置と大きさのビル**

> 🔍 **発見ポイント**: `random.randint(a, b)` は、a以上b以下のランダムな整数を返す関数だよ。これを使うと、毎回違う位置や大きさのビルが作れるんだ！

## 街づくりの準備：区画を考えよう

▲図1▲のように、ランダムにビルを配置するだけでは、間隔が不均一でスカスカな街になってしまいます。

そこで、土地を区分する「区画」の概念を使い、ビルの配置をあらかじめ設計しておくことで、整然としたリアルな街並みを再現できます。

まずは、区画を定義するためのデータ構造を考えましょう。simple_district.py という名前でファイルを作成し、以下のコードを入力してください。

```python
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
            'size': (10, 15),  'pos': (12, 0), 'num_floors': 4
        },
        {
            'size': (10, 15),  'pos': (0, 20), 'num_floors': 6
        },
        {
            'size': (10, 15),  'pos': (12, 20), 'num_floors': 3
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
```

このコードでは、まず区画を定義しています。区画にはサイズと、その中に配置するビルの情報（サイズ、位置、階数）が含まれています。そして、区画内のすべてのビルを生成しています。

simple_district.pyを保存して実行すると、区画内にビルが配置された様子が表示されます（▲図2▲）。以下のコマンドを実行してください。

```bash
cubicpy -g 0.1 simple_district.py
```

![Simple District](https://creativival.github.io/CubicPy/assets/simple_district.png)

**▲図2▲ 単一区画に配置されたビル群**

> 💡 **先生からのヒント**: このように「辞書」と「リスト」を組み合わせることで、複雑な構造を表現できるんだ。区画には複数のビルが含まれていて、各ビルには様々な情報が含まれているよ。

## 巨大都市を作ろう

さあ、いよいよ巨大な都市を作成します！区画のテンプレートをいくつか用意し、それを組み合わせて大規模な都市を構築しましょう。create_city_100x100.py という名前でファイルを作成し、以下のコードを入力してください。

```python
import random

# 全体のオブジェクトデータを格納するリスト
body_data = []

# 都市設定パラメータ
MIN_FLOOR_HEIGHT = 8  # 各階の最小高さ
MAX_FLOOR_HEIGHT = 12  # 各階の最大高さ
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
                'size': (25, 20),  # ビルのサイズ (幅, 奥行き)
                'pos': (0, 0),  # 区画内の位置 (x, y)
                'num_floors': 5  # 階数
            },
            {
                'size': (15, 20),  'pos': (0, 20), 'num_floors': 4
            },
            {
                'size': (10, 20),  'pos': (15, 20), 'num_floors': 3
            },
        ]
    },
    {
        'size': (25, 40),  # 区画のサイズ (幅, 奥行き)
        'buildings': [
            {
                'size': (25, 20), 'pos': (0, 20), 'num_floors': 5
            },
            {
                'size': (15, 20),  'pos': (0, 0), 'num_floors': 4
            },
            {
                'size': (10, 20),  'pos': (15, 0), 'num_floors': 3
            },
        ]
    },
    {
        'size': (25, 40),
        'buildings': [
            {
                'size': (25, 30),  'pos': (0, 0), 'num_floors': 4
            },
            {
                'size': (25, 10),  'pos': (0, 30), 'num_floors': 3
            },
        ]
    },
    {
        'size': (25, 40),
        'buildings': [
            {
                'size': (25, 30),  'pos': (0, 10), 'num_floors': 4
            },
            {
                'size': (25, 10),  'pos': (0, 0), 'num_floors': 3
            },
        ]
    },
]


def create_building(x_pos, y_pos, z_pos, width, depth, floor_height, num_floors, target_data):
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
            building_width -= random.randint(3, 5)  # 幅をランダムに調整
            building_depth -= random.randint(3, 5)  # 奥行きをランダムに調整

            building_x, building_y = building_data['pos']
            building_x += random.randint(0, 3)  # X座標をランダムに調整
            building_y += random.randint(0, 3)  # Y座標をランダムに調整

            num_floors = building_data['num_floors']
            num_floors += random.randint(-2, 2)  # 階数をランダムに調整

            # 階高をランダムに決定
            floor_height = random.randint(MIN_FLOOR_HEIGHT, MAX_FLOOR_HEIGHT)

            # 区画内での相対座標を全体座標に変換
            absolute_x = building_x + district_x
            absolute_y = building_y + district_y
            base_z = 0  # 地面レベル

            # ビルを生成
            create_building(absolute_x, absolute_y, base_z, building_width, building_depth, floor_height, num_floors,
                            body_data)

        # 次の区画のX座標を更新（区画の幅 + 間隔）
        district_x += selected_district['size'][0]

    # 行の最後に達したらX座標をリセットしてY座標を更新
    district_x = 0
    district_y += 60  # 各行の間隔は60単位

print(f"都市の生成完了: {len(body_data)}個のオブジェクトを作成しました")
```

このコードでは、次のようなことを行っています：

1. いくつかの区画テンプレートを定義
2. 都市の設定パラメータを定義（都市の大きさ、区画の数など）
3. 都市全体に区画を配置（2行×4列）
4. 各区画内のビルをランダムに調整して生成

create_city_100x100.pyを保存して実行すると、巨大な都市が生成されます（▲図3▲）。以下のコマンドを実行してください。

```bash
cubicpy -g 0.1 create_city_100x100.py
```

![City Generation](https://creativival.github.io/CubicPy/assets/create_city_100x100.png)

**▲図3▲ 自動生成された巨大都市**

> 🚀 **すごいね！**: たった数百行のコードで、数千個のオブジェクトからなる巨大都市が作れちゃうよ！これがプログラミングの力だね！

## 隕石の追加：破壊の準備

さて、せっかく作った都市ですが…今度はこれを破壊する準備をします！都市に向かって落下する巨大隕石を追加しましょう。city_with_meteor.py という名前で新しいファイルを作成し、先ほどのコードの最後に以下のコードを追加してください。

```python
# create_city_100x100.pyのコードをここにコピー

# 隕石を生成
body_data.append({
    'type': 'sphere',
    'pos': (CITY_WIDTH / 2, CITY_LENGTH / 2, 200),  # 都市の中心上空に配置
    'scale': (50, 50, 50),  # 直径100のかなり大きな球体
    'color': (1, 1, 1),  # 白色
    'mass': 100,  # 重い質量を設定
    'base_point': 2,  # 重心を基準に配置
    'velocity': (0, 0, -100),  # 下向きに高速で移動（スペースキーで発射）
})
```

### 隕石のパラメータ解説

隕石のパラメータについて詳しく見ていきましょう：

1. `'type': 'sphere'` - 球体として作成
2. `'pos': (CITY_WIDTH / 2, CITY_LENGTH / 2, 200)` - 都市の中心上空200に配置
3. `'scale': (50, 50, 50)` - 直径100の巨大な球体
4. `'color': (1, 1, 1)` - 白色
5. `'mass': 100` - 非常に重い質量（標準は1）
6. `'base_point': 2` - 重心を基準に配置（球体の中心を位置の基準にする）
7. `'velocity': (0, 0, -100)` - 下向きに高速で移動

特に重要なのは `'velocity'` パラメータで、これにより隕石に初速度を与えます。スペースキーを押すと、この速度で発射されます。

完成したファイルを実行して、隕石衝突実験を行いましょう。以下のコマンドを実行してください。

```bash
cubicpy -g 0.1 create_city_100x100_with_meteor.py
```

![Meteor Impact](https://creativival.github.io/CubicPy/assets/create_city_100x100_with_meteor.png)

**▲図4▲ 隕石が都市に衝突する瞬間**

3D世界が表示されたら：
1. マウスホイールでズームアウトしてから、カメラを右に移動させて、都市全体と隕石を見渡せるようにする
2. スペースキーを押して隕石を発射
3. 隕石が都市に落下し、建物が粉々になるのを観察！

> 🔍 **発見ポイント**: 隕石が重いほど、衝突時の破壊力が大きくなります。`'mass'` の値を変えると、破壊の仕方が変わるよ！

## チャレンジ：最も派手に崩れる建築物を設計しよう

今回学んだ知識を活用して、最も派手に崩れる建築物やシチュエーションを考えてみましょう。例えば：

1. **ボーリングで街を破壊**: 隕石のコード（create_city_100x100_with_meteor.py）を修正して、巨大なボールを地面上に作成して、ビルに向かって転がす
2. **ドミノ効果の都市**: 細長いビルを一列に並べて、最初のビルが倒れると連鎖的に全てが崩れるように設計
3. **ピラミッド都市**: 高さの違うビルをピラミッド状に配置し、頂上に大きな球体を落とす
4. **バランスタワー**: とても細い柱の上に重い建物を載せて、少しの衝撃で崩れるように設計

## デバッグのコツ

大規模な都市を作るときに、問題が起きることもあります。ここではいくつかのデバッグのコツを紹介します。

1. **段階的に構築**: まず小さな部分から始めて、正しく動作することを確認してから大きな構造を作りましょう
2. **オブジェクト数に注意**: 非常に多くのオブジェクトを生成すると、処理が遅くなることがあります
3. **位置の計算を確認**: ビルの位置がおかしいときは、座標計算の部分を確認しましょう
4. **print()文を活用**: プログラムの途中で変数の値を表示して、期待通りになっているか確認しましょう

例えば、ビルの位置を確認するには：

```python
for building_data in district['buildings']:
    building_x, building_y = building_data['pos']
    absolute_x = building_x + district_x
    absolute_y = building_y + district_y
    print(f"相対位置: ({building_x}, {building_y}), 絶対位置: ({absolute_x}, {absolute_y})")
```

## まとめ：今回学んだこと

1. **関数を使ったコード再利用**: `create_building()`関数を定義して、複数の場所でビルを生成できました
2. **区画を使った都市設計**: 区画（ディストリクト）という概念を使って、整然とした都市を設計しました
3. **物理シミュレーションの応用**: 隕石やボーリングボールを使って、物理シミュレーションを体験しました
4. **ランダム性の導入**: `random`モジュールを使って、毎回異なる都市を生成しました

これらの技術を組み合わせることで、自分だけの仮想都市を作り、そこで様々な物理実験を行うことができます。

## 次回予告

次回は「キューブドミノ倒し選手権」です。一押しで連鎖反応を起こす、壮大なドミノ倒しの作り方を学びます。ドミノの安定性と配置パターン、崩壊連鎖のデザインなど、より高度な物理シミュレーションにチャレンジしましょう！

> 🎮 **宿題（やってみよう）**: 今回学んだ都市生成と物理シミュレーションを組み合わせて、自分だけのユニークな破壊シナリオを作ってみよう。友達に「これ見て！」と言いたくなるような派手な崩壊を目指そう！

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
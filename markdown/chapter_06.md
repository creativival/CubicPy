# 第6回：APIモードでパワーアップ！

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**プログラマーの新しい魔法の杖、APIモードをマスターして、より自由な3D世界を作り出そう！**

## 前回のおさらい

前回は「キューブドミノ倒し選手権」で連鎖反応の世界を探索しました。ドミノを様々なパターンで配置し、一押しで全てが倒れる様子を楽しみましたね。

今回はもっと自由度の高いプログラミング方法、「APIモード」を学びます。これまでのキューパイの知識にもう一段階の力を加えて、より複雑で面白い3D世界を作れるようになりましょう！

## APIモードって何？ より強力な魔法の杖

これまでのキューパイでは、`body_data` というリストにオブジェクトを追加する方法でプログラミングしてきました。この方法はシンプルで分かりやすいのですが、できることに限りがありました。

APIモードは、より多くの機能を直接呼び出せるプログラミング方法です。これまでの方法よりも記述量が増えることがありますが、その分だけ自由度が広がります！

### APIモードのメリット

1. **メソッドの豊富さ**: オブジェクトの追加、削除、変更などが直感的に行える
2. **座標変換**: 座標系を自由に変換できるので、複雑な構造物も簡単に作れる
3. **テキスト表示**: 画面上にテキストを表示することができる
4. **柔軟な制御**: シミュレーションの開始や再開、オブジェクトの発射などを自由にコントロールできる

> 💡 **先生からのヒント**: これまでの方法は`body_data`リストを「魔法の箱」に入れる方法だったのに対し、APIモードは「魔法の杖」を直接振るような感覚だよ！より直接的にキューパイを操れるんだ。

## CubicPyAppクラスを使ったプログラミングの基本

APIモードでは、`CubicPyApp`というクラスを使ってプログラミングします。最初の例として、単純なキューブを配置するコードを見てみましょう。simple_api.py という名前で新しいファイルを作成し、以下のコードを入力してください。

```python
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 箱を追加
app.add_cube(
    position=(0, 0, 0),  # 位置
    scale=(1, 1, 1),     # サイズ
    color=(1, 0, 0)      # 色（赤）
)

# シミュレーションを実行
app.run()
```

このコードを保存して、次のコマンドで実行してみましょう。APIモードでは、`cubicpy`コマンドを使う必要はありません。Pythonのスクリプトを直接実行します。

```bash
python simple_api.py
```

画面に赤い箱が表示されましたか（▲図1▲）？おめでとうございます！これがAPIモードでの最初のステップです。

![Simple API Example](https://creativival.github.io/CubicPy/assets/simple_api_mode.png)

**▲図1▲ APIモードで作成した最初のキューブ**

### CubicPyAppクラスの初期化オプション

`CubicPyApp`クラスを作成するときには、いくつかのオプションを指定できます。

```python
app = CubicPyApp(
    gravity_factor=1,            # 重力係数（標準は1、小さいと低重力）
    window_size=(900, 600),      # ウィンドウサイズ（幅, 高さ）
    camera_lens='perspective'    # カメラレンズ（'perspective'または'orthographic'）
)
```

これらのオプションは、これまで`cubicpy`コマンドのパラメータで指定していたものと同じです。

> 🔍 **発見ポイント**: APIモードでは、`cubicpy -g 0.1 your_file.py`のようなコマンドではなく、コード内で直接`gravity_factor=0.1`と指定します。これにより、プログラム内でいつでも重力を変更することができます！

## オブジェクト追加メソッドのマスター

APIモードでは、様々な形状のオブジェクトを追加するためのメソッドが用意されています。ここでは、主要なメソッドとその使い方を紹介します。

### 基本的なオブジェクト追加メソッド

箱、球、円柱を追加するための3つの基本メソッドがあります。shape_methods.py という名前でファイルを作成し、次のコードを入力してください。

```python
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 箱を追加
app.add_cube(
    position=(0, 0, 0),      # 位置
    scale=(1, 1, 1),         # サイズ
    color=(1, 0, 0),         # 色（赤）
    mass=1,                  # 質量
    color_alpha=1,           # 透明度（1=不透明、0=透明）
    hpr=(0, 0, 0),           # 回転（heading, pitch, roll）
    base_point=0,            # 基準点（0=角、1=底面中心、2=重心）
    velocity=(2, 0, 0)            # 初速度ベクトル
)

# 球を追加
app.add_sphere(
    position=(2, 0, 0),      # 位置（X座標を2にして右に配置）
    scale=(1, 1, 1),         # サイズ
    color=(0, 1, 0),          # 色（緑）
    remove=True,            # 削除フラグ
)

# 円柱を追加
app.add_cylinder(
    position=(4, 0, 0),      # 位置（X座標を4にして右に配置）
    scale=(1, 1, 1),         # サイズ
    color=(0, 0, 1)          # 色（青）
)

# シミュレーションを実行
app.run()
```

このコードを保存して実行すると、赤い箱、緑の球、青い円柱が横一列に並んで表示されます（▲図2▲）。`velocity`パラメータを指定すると、スペースキーを押すとオブジェクトが初期速度を持って動き出します。`remove`パラメータを`True`にすると、Xキーでオブジェクトが一つずつ削除されます。

```bash
python shape_methods.py
```

![Shape Methods](https://creativival.github.io/CubicPy/assets/shape_methods.png)

**▲図2▲ 3種類の基本形状**

各メソッドのパラメータは、これまでの`body_data`に追加していたパラメータとほぼ同じです。ただし、`'type'`はメソッド名で指定するため不要になりました。また、`pos`は`position`と名前が変わっていることに注意してください。

> 💡 **先生からのヒント**: パラメータは基本的に省略可能です。例えば`color`や`scale`を省略すると、デフォルト値が使われます。でも、`position`だけは常に指定します！

## 座標変換機能を使いこなす

APIモードの最も強力な機能の一つが「座標変換」です。これにより、複雑な構造物を簡単に作れるようになります。

### 座標変換とは？

座標変換とは、「現在の位置」を基準にして新しいオブジェクトを配置する機能です。これにより、複雑な構造物の各部分を相対的な位置で指定できるため、全体を移動させたり回転させたりするのが簡単になります。

座標変換は以下の5つのメソッドで操作します：

1. `push_matrix()`: 現在の座標系をスタックに保存し、新しい変換ノードを作成
2. `pop_matrix()`: スタックから座標系を取り出し、前の状態に戻す
3. `translate(x, y, z)`: 座標系をx, y, z方向に移動
4. `rotate_hpr(h, p, r)`: 座標系をh, p, r角度で回転
5. `reset_matrix()`: 全ての変換をリセット

これらのメソッドを使って、簡単な家モデルを作ってみましょう。house_with_matrix.py という名前でファイルを作成し、次のコードを入力してください。

```python
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
```

このコードでは、`create_house`関数内で座標変換を使って、「家」という複雑な構造物を作っています。異なる位置に、異なるサイズの家を簡単に配置できることに注目してください。次のコマンドで実行してみましょう。

```bash
python house_with_matrix.py
```

3つの三角屋根の家が簡単に建築できました（▲図3▲）。座標変換`push_matrix()`と`pop_matrix()`を使うことで、各家の位置を簡単に指定できることがわかります。次に、屋根の中心に座標変換することで、屋根の階段を簡単に積み上げられます。

![Houses with Matrix](https://creativival.github.io/CubicPy/assets/houses_with_matrix.png)

**▲図3▲ 座標変換を使用して作成した3つの家**

> 💡 **先生からのヒント**: `push_matrix()`と`pop_matrix()`は、必ずペアで使いましょう。「スタック」というのは、データを積み重ねる構造のことで、`push`で積み上げて、`pop`で一番上から取り出します。これを正しく使わないと、思わぬ場所にオブジェクトが配置されることになります！

## テキスト表示機能の活用

APIモードでは、画面上にテキストを表示することができます。これは、ゲームのスコア表示や、操作方法の説明などに便利です。thrower_with_text_display.py という名前でファイルを作成し、次のコードを入力してください。

```python
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 壁を追加
for j in range(20):
    for i in range(20):
        app.add_cube(
            position=(20, i, j),  # 位置
            scale=(1, 1, 1),     # サイズ
            color=(0.5, 0.5, 0.5)  # 色（灰色）
        )

# 投擲機を追加
for i in range(10):
    app.add_sphere(
        position=(0, i * 2, 0),  # 位置
        scale=(2, 2, 2),     # サイズ
        color=(0.8, 0.2, 0.2),  # 色（赤）
        mass=10,  # 質量
        velocity=(i, 0, i)  # 初速
    )

# テキスト表示
app.set_top_left_text('投擲機シミュレーション: スペースキーで発射！')
app.set_bottom_left_text("操作方法: 矢印キーでカメラ移動、R でリセット")

# アプリを実行
app.run()
```

このコードでは、画面の左上と左下にテキストを表示しています。ゲームの説明やヒントなど、様々な用途に使うことができます。次のコマンドでアプリを実行します。

```bash
python thrower_with_text_display.py
```

![Text Display](https://creativival.github.io/CubicPy/assets/thrower_with_text_display.png)

**▲図5▲ 画面上にテキストを表示した投擲機シミュレーション**

> 💡 **先生からのヒント**: テキスト表示は、あなたが作ったアプリケーションをより使いやすくするために重要です。特に複雑な操作が必要なゲームやシミュレーションでは、ユーザーへの指示を表示するのに役立ちます！

## コードの書き方が変わる！より自由度の高い表現

APIモードに切り替えると、コードの構造が大きく変わります。従来の`body_data`リストに追加する方法と比較してみましょう。

### 従来のbody_dataスタイル

```python
# 物体データの配列を作成
body_data = []

# 10段の箱を積み上げる
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 0, i),
        'scale': (1, 1, 1),
        'color': (i/10, 0, 1-i/10)
    })
```

### APIモードスタイル

```python
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 10段の箱を積み上げる
for i in range(10):
    app.add_cube(
        position=(0, 0, i),
        scale=(1, 1, 1),
        color=(i/10, 0, 1-i/10)
    )

# シミュレーションを実行
app.run()
```

APIモードスタイルでは、最初に`CubicPyApp`のインスタンスを作成し、その後メソッドを呼び出す形になります。また、最後に必ず`app.run()`でシミュレーションを実行する必要があります。

APIモードの利点は、オブジェクトの追加方法が直感的になり、さらに座標変換やテキスト表示などの追加機能が使える点です。

> 💡 **先生からのヒント**: どちらのスタイルが優れているというわけではありません。単純なオブジェクト配置なら従来の`body_data`スタイルでも十分ですが、より複雑なプログラムを作りたい場合はAPIモードが便利です！

## 応用例：APIを使って複合建築物を作る

APIモードの力を使って、より複雑な建築物を作ってみましょう。例として、日本の神社をモデルにした建物を作ってみます。japanese_shrine.py という名前でファイルを作成し、次のコードを入力してください。

```python
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
```

このコードでは、APIモードの座標変換機能を使って、日本の神社を構成する様々な要素（本殿、鳥居、参道、石灯籠など）を組み合わせています。特に屋根の部分では、複数の立方体を少しずつずらして重ねることで、日本建築の特徴的な反り屋根を表現しています。次のコマンドを実行してみましょう。

```bash
python japanese_shrine.py
```

![Japanese Shrine](https://creativival.github.io/CubicPy/assets/japanese_shrine.png)

**▲図6▲ APIモードで作成した日本の神社モデル**

> 🔍 **発見ポイント**: 実際の建築物をモデル化するとき、単純な形状の組み合わせで複雑な形を表現することが重要です。座標変換を使うことで、全体の構造を把握しながら細部を作り込むことができます！

## チャレンジ：APIを使って日本のお城を作ろう

今回学んだAPIモードの知識を活用して、日本のお城を作ってみましょう。多層の天守閣や石垣、瓦屋根など、日本の城の特徴を表現してみてください。

以下は、基本的な構造のヒントです：

1. **石垣**: 基底部分の大きな立方体で表現
2. **天守閣の各層**: 上に行くほど小さくなる立方体を積み重ねる
3. **反り屋根**: 神社の例を参考に、複数の立方体を重ねて表現
4. **装飾**: 鯱（しゃち）や瓦などの細部も追加に挑戦

以下のようなスケルトンコードから始めると良いでしょう：

```python
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp(gravity_factor=0.1)

# お城を作成する関数
def create_castle(pos_x, pos_y, size):
    # 座標系をお城の位置に移動
    app.push_matrix()
    app.translate(pos_x, pos_y, 0)
    
    # 石垣（基礎部分）
    # ここにコードを追加
    
    # 天守閣（各層）
    # ここにコードを追加
    
    # 屋根
    # ここにコードを追加
    
    # 装飾
    # ここにコードを追加
    
    # お城全体の座標系を戻す
    app.pop_matrix()

# お城を作成
create_castle(0, 0, 5)

# テキスト表示
app.set_top_left_text("日本のお城モデル")

# シミュレーションを実行
app.run()
```

## デバッグのコツ

APIモードでプログラミングする際の、いくつかのデバッグのコツを紹介します：

1. **座標変換のバランス**: `push_matrix()`と`pop_matrix()`の数が一致することを確認しましょう。
2. **シンプルから始める**: まずは単純な形状から始めて、徐々に複雑にしていきましょう。
3. **print文の活用**: 特定の値や座標を確認するには、プログラム中に`print()`文を挿入しましょう。
4. **段階的テスト**: 複雑な関数を作る場合は、一部分ずつ実装してテストするのが効果的です。
5. **座標系のリセット**: 何かおかしくなったら、`reset_matrix()`で座標系をリセットしてみましょう。

```python
# デバッグ用のprint文の例
def create_complex_structure(x, y, size):
    print(f"Creating structure at ({x}, {y}) with size {size}")
    app.push_matrix()
    app.translate(x, y, 0)
    
    # 構造物を作成
    
    print("Structure created, popping matrix")
    app.pop_matrix()
```

## まとめ：今回学んだこと

1. **APIモードの基本**: `CubicPyApp`クラスのインスタンス化と基本メソッド
2. **オブジェクト追加メソッド**: `add_cube()`, `add_sphere()`, `add_cylinder()`などの使い方
3. **座標変換**: `push_matrix()`, `pop_matrix()`, `translate()`, `rotate_hpr()`を使った座標系の操作
4. **テキスト表示**: `set_top_left_text()`, `set_bottom_left_text()`による画面上のテキスト表示
5. **動的制御**: `launch_objects()`などを使ったオブジェクトの動的な操作

これらの技術を組み合わせることで、より複雑で自由度の高い3D世界を作ることができるようになりました。

## 次回予告

次回は「3Dボーリングゲームを作ろう！」です。今回学んだAPIモードの知識を活用して、本格的なボーリングゲームを作成します。球の発射、ピンの配置、そして得点計算までを実装する方法を学びましょう！

> 🎮 **宿題（やってみよう）**: 今回学んだAPIモードを使って、自分だけのオリジナル建築物を作ってみよう。座標変換を駆使して、複雑な形状にも挑戦してみよう！

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
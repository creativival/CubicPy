# CubicPy

*日本語 | [English](https://creativival.github.io/CubicPy/)*

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

CubicPy - コードで物理オブジェクトを配置・構築する3Dプログラミング学習アプリ

「キュービックパイ」 - 略して「キューパイ」と呼んでください！

## アプリの説明

CubicPyは、Pythonコードを使って3D空間にオブジェクトを配置し、リアルな物理演算で動作する世界を構築できるアプリケーションです。ボックスや球体などの物体を自由に配置して建築物を作り、重力や衝突などの物理法則を体験しながらプログラミングを学べます。

![CubicPy Sample Animation Gif](https://creativival.github.io/CubicPy/assets/cubicpy_sample.gif)

作成したオブジェクト建築物は、地面を傾けたり、オブジェクトを消すことで物理演算を使ったリアルな崩壊過程を観察できます。また、重力係数を変更することで、異なる重力環境下での物理挙動を確認できます。さらに、オブジェクトに初速度ベクトルを設定して発射することも可能です。

## インストール方法

```
pip install cubicpy
```

## cubicpyコマンドの使用方法

インストール後、コマンドラインから簡単に実行できます：

```
# サンプルコードをランダムに選択して実行
cubicpy

# ヘルプを表示
cubicpy --help
cubicpy -h

# サンプル一覧を表示
cubicpy --list
cubicpy -l

# 特定のサンプルを実行
cubicpy --example cube_tower_sample
cubicpy -e cube_tower_sample

# 自作のPythonファイルを実行
cubicpy your_body_data_script.py

# 重力係数を変更して実行（重力に10の何乗倍を掛けるか指定する）
cubicpy --gravity 0.01 --example cube_tower_sample
cubicpy -g 0.01 -e cube_tower_sample

# カスタムウィンドウサイズ(1280x720)で実行
cubicpy -e cube_tower_sample -w 1280,720
cubicpy --window-size 1280,720 -e cube_tower_sample

# カメラレンズの種類を指定して実行（perspective または orthographic）
cubicpy -e cube_tower_sample -c orthographic
cubicpy --camera-lens orthographic -e cube_tower_sample
```

## サンプルコードの解説

### 箱の塔を作る (cube_tower_sample.py)

![Sample cube tower](https://creativival.github.io/CubicPy/assets/cube_tower.png)

```python
# 物体データの配列を作成
body_data = []

# 10段の箱を積み上げる
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 0, i),  # 位置: x, y, z
        'scale': (1, 1, 1),  # サイズ: 幅, 奥行き, 高さ
        'color': (i/10, 0, 1-i/10),  # 色: 赤, 緑, 青 (0〜1)
        'mass': 1  # 質量（省略可）
    })
```

### 初速度ベクトルを使ったオブジェクトの発射

```python
# 発射体を作成
body_data.append({
    'type': 'sphere',
    'pos': (5, 5, 2),  # 位置: x, y, z
    'scale': (1, 1, 1),  # サイズ
    'color': (1, 0, 0),  # 赤色
    'mass': 5,  # 質量
    'velocity': (10, -5, 3)  # 初速度ベクトル: x, y, z方向
})
```

## コマンドモードの他のサンプル

追加のサンプルコードは「codes」ディレクトリにあります。`cubicpy your_file.py`コマンドで実行します。

## オブジェクト定義の詳細（cubicコマンド用）

`body_data`リストに追加するオブジェクト定義の詳細：

| パラメータ       | 説明                                     | 必須 | デフォルト値         |
|--------------|----------------------------------------|------|----------------|
| `type`       | オブジェクトの種類: 'cube', 'sphere', 'cylinder' | 必須 | -              |
| `pos`        | 位置座標 (x, y, z)                         | 必須 | -              |
| `scale`      | 大きさ (幅, 奥行き, 高さ)                       | 任意 | (1, 1, 1)      |
| `color`      | 色 (赤, 緑, 青) - 各値は0〜1                   | 任意 | (0.5, 0.5, 0.5) |
| `mass`       | 質量 (0: 固定物体)                           | 任意 | 1              |
| `color_alpha`| 透明度 (0: 透明 〜 1: 不透明)                   | 任意 | 1              |
| `hpr`        | 回転角度 (heading, pitch, roll)            | 任意 | (0, 0, 0)      |
| `base_point` | 配置するときの位置基準                            | 任意 | 0              |
| `remove`     | 削除するオブジェクト                             | 任意 | False          |
| `vec`        | 初速度ベクトル (x, y, z)                      | 任意 | (0, 0, 0)      |

※ `base_point`は以下の値が指定可能:
- `0`: 原点に近い角が基準
- `1`: 底面の中心が基準
- `2`: 立方体の重心が基準

## cubicpyコマンドでワールドをビルドする方法

1. サンプルのような形式でPythonファイルを作成
2. `cubicpy your_file.py`コマンドで実行

## APIモードでビルドするサンプルコード

![Sample api mode](https://creativival.github.io/CubicPy/assets/sample_api_mode.png)

```python
from cubicpy import CubicPyApp

# インスタンス化
app = CubicPyApp(gravity_factor=0.01)

# 単独オブジェクトの追加
# APIを使ってオブジェクトを追加
app.add_cube(position=(0, 0, 0), scale=(1, 1, 1), color=(1, 0, 0))
app.add_sphere(position=(2, 0, 0),  scale=(1, 1, 1), color=(0, 1, 0))
app.add_cylinder(position=(4, 0, 0),  scale=(1, 1, 1), color=(0, 0, 1))

# 初速度ベクトルを設定したオブジェクトを追加
app.add_sphere(
    position=(5, 5, 2),
    scale=(1, 1, 1),
    color=(1, 0, 0),
    mass=5,
    vec=(10, -5, 3)  # スペースキーを押すと、この速度で発射される
)

# 複数オブジェクトの追加（ループ）
for i in range(10):
    app.add_cube(
        position=(0, 5, i),
        color=(i/10, 0, 1-i/10)
    )

# cubicpyコマンドと互換性を保つbody_dataの追加
body_data = []
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 10, i),
        'scale': (1, 1, 1),
        'color': (i / 10, 0, 1 - i / 10),
        'mass': 1,
        'color_alpha': 1,
    })

app.from_body_data(body_data)

# シミュレーション実行
app.run()
```

## APIモードの他のサンプルコード

追加のサンプルコードは「api_codes」ディレクトリにあります。`python your_file.py`コマンドで実行します。

## APIモードのメソッド詳細

### CubicPyAppクラス

```python
CubicPyApp(code_file=None, gravity_factor=1, window_size=(900, 600), camera_lens='perspective')
```
- `code_file`: 実行するPythonファイルのパス（任意）
- `gravity_factor`: 重力係数（任意、デフォルト: 1）
- `window_size`: ウィンドウサイズ（任意、デフォルト: (900, 600)）
- `camera_lens`: カメラレンズのタイプ（'perspective'または'orthographic'、任意、デフォルト: 'perspective'）

### オブジェクト追加メソッド

#### 箱を追加
```python
add_cube(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- `position`: 位置座標 (x, y, z)
- `scale`: 大きさ (幅, 奥行き, 高さ)
- `color`: 色 (赤, 緑, 青) - 各値は0〜1
- `mass`: 質量 (0: 固定物体)
- `color_alpha`: 透明度 (0: 透明 〜 1: 不透明)
- `hpr`: 回転角度 (heading, pitch, roll)
- `base_point`: 配置するときの位置基準 (0: 原点に近い角が基準, 1: 底面の中心が基準, 2: 立方体の重心が基準)
- `remove`: 削除するオブジェクト(真偽値) - Xキーで削除可能
- `vec`: 初速度ベクトル (x, y, z) - スペースキーを押すと適用される

#### 球体を追加
```python
add_sphere(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- パラメータは`add_cube`と同様

#### 円柱を追加
```python
add_cylinder(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- パラメータは`add_cube`と同様

#### body_dataリストからオブジェクトを構築
```python
from_body_data(body_data) 
```
- `body_data`: cubicpyコマンドのオブジェクト定義（辞書形式）のリスト

### 汎用オブジェクト追加
```python
add(obj_type, **kwargs)
```

-obj_type: オブジェクトの種類 ('cube', 'sphere', 'cylinder')
- **kwargs: オブジェクトのパラメータ（以下のキーワード引数が使用可能）
  - positionまたはpos: 位置座標
  - scale: 大きさ
  - color: 色
  - mass: 質量
  - color_alpha: 透明度
  - remove: 削除するオブジェクト
  - vec: 初速度ベクトル

### テキスト表示関連のAPIメソッド

アプリケーション画面上にテキストを表示することができます。

#### set_top_left_text(text)
画面左上にテキストを表示します。
- `text`: 表示するテキスト

#### set_bottom_left_text(text)
画面左下にテキストを表示します。
- `text`: 表示するテキスト

### 座標変換メソッド

CubicPyでは、Processingのような座標系操作を実現するための座標変換メソッドを提供しています。これらを使うことで、オブジェクトの配置を相対的に行うことができます。

#### 座標変換のメソッド一覧

```python
push_matrix()   # 現在の変換状態をスタックに保存し、新しい変換ノードを作成
pop_matrix()    # スタックから変換状態を復元
translate(x, y, z)    # 指定した位置に移動
rotate_hpr(h, p, r)   # HPR（Heading-Pitch-Roll）で回転
reset_matrix()   # 変換をリセット
```

#### 使用例

以下は座標変換を使って3つの塔を異なる位置に配置する例です：

```python
from cubicpy import CubicPyApp

# インスタンス化
app = CubicPyApp(gravity_factor=1, window_size=(1800, 1200))

# 1つ目の塔（原点に配置）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),
        color=(i / 10, 0, 1 - i / 10)
    )

# 座標系の変換（1段目）
app.push_matrix()
app.translate(5, 5, 0)  # 原点から(5,5,0)の位置に座標系を移動

# 2つ目の塔（相対位置(5,5,0)に配置）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),  # この位置は新しい座標系での位置
        color=(i / 10, 1 - i / 10, 0)
    )

# 座標系の変換（2段目）
app.push_matrix()
app.translate(5, 5, 0)  # さらに(5,5,0)移動（元の原点から見ると(10,10,0)）
app.rotate_hpr(45, 10, 0)  # Y軸周りに45度、X軸周りに10度回転

# 3つ目の塔（さらに相対位置(5,5,0)に配置し、回転も適用）
for i in range(10):
    app.add_cube(
        position=(0, 0, i),  # この位置は最新の座標系での位置
        color=(0, i / 10, 1 - i / 10)
    )

# 座標系の変換から戻る（2段目）
app.pop_matrix()

# 座標系の変換から戻る（1段目）
app.pop_matrix()

# シミュレーション実行
app.run()
```

#### 座標変換の仕組み

座標変換はスタック構造で管理されており、以下のように動作します：

1. `push_matrix()`を呼び出すと、現在の座標変換状態をスタックに保存し、新しい変換ノードを作成します
2. `translate()`や`rotate_hpr()`で座標系を変更します
3. オブジェクトを追加すると、現在の座標系に対して相対的に配置されます
4. `pop_matrix()`を呼び出すと、前の座標系に戻ります
5. `reset_matrix()`でスタックをすべてクリアし、初期状態に戻ります

この機能により、複雑な構造物を相対的な座標で簡単に構築できます。例えば、家の各部分（壁、屋根、窓など）を相対位置で配置し、家全体を移動させたい場合に便利です。

#### 注意点

- 必ず`push_matrix()`と`pop_matrix()`をペアで使用してください
- 多くの階層を作る場合は、`pop_matrix()`の呼び出し順序に注意してください
- デバッグ時は`reset_matrix()`で状態をリセットすると便利です

### ワールド操作メソッド

```python
run()  # ワールドを構築して実行
reset()  # ワールドをリセット
launch_objects()  # 初速度設定されたオブジェクトを発射（スペースキーでも実行可能）
```

## APIモードでワールドを構築する方法

1. Pythonスクリプトで`CubicPyApp`のインスタンスを作成
2. `add_cube()`、`add_sphere()`などのメソッドでオブジェクトを追加
3. `run()`メソッドを呼び出してワールドを構築・実行
4. 必要に応じて`reset()`メソッドで再構築可能
5. `python your_script.py`で実行

## アプリの操作方法

- **矢印キー**: カメラ角度の変更
- **SHIFT + W/S/A/D/Q/E**: カメラの注視点（目標点）を移動
- **マウスホイール**: ズームイン/アウト（perspective モード）または表示範囲の拡大/縮小（orthographic モード）
- **W/S/A/D**: 地面を傾ける
- **F/G**: 重力の強さを変更
- **R**: リセット（カメラ位置と注視点もリセット）
- **Z**: デバッグ表示切替
- **X**: 選択したオブジェクトを一つずつ削除
- **スペースキー**: 初速度ベクトル(`vec`)が設定されたオブジェクトを発射
- **ESC**: 終了

## WebSocketモード

CubicPyは外部アプリケーションからWebSocket経由でオブジェクトデータを受け取ることができます。これにより、CubicPyと他のアプリケーション間でリアルタイムな連携が可能になります。

### WebSocketサーバーの起動

WebSocketモードでCubicPyを起動するには、以下のコマンドを使用します：

```bash
cubicpy --external

cubicpy -x
```

### 例：Voxelammingクライアントからのデータ送信

VoxelammingクライアントアプリケーションからCubicPyにデータを送信できます。以下はPythonを使用した例です：

```python
# voxelammingパッケージからVoxelammingクラスをインポート
from voxelamming import Voxelamming

# CubicPyアプリケーションに表示されるルーム名を指定
room_name = "1000"
# Voxelammingクラスのインスタンスを作成
vox = Voxelamming(room_name)

# ボクセルのサイズを設定
vox.set_box_size(1)
# ボクセルの配置間隔を設定
vox.set_build_interval(0.01)

# ボクセルの配置位置と色を設定
for i in range(100):
    vox.create_box(-1, i, 0, r=0, g=1, b=1, alpha=1)
    vox.create_box(0, i, 0, r=1, g=0, b=0, alpha=1)
    vox.create_box(1, i, 0, r=1, g=1, b=0, alpha=1)
    vox.create_box(2, i, 0, r=0, g=1, b=1, alpha=1)

# ボクセルの削除位置を設定
for i in range(50):
    vox.remove_box(0, i * 2 + 1, 0)
    vox.remove_box(1, i * 2, 0)

# ボクセルデータをアプリケーションに送信
vox.send_data("main")
# vox.close_connection()
```

### インストールと実行

```bash
# voxelammingパッケージのインストール
$ pip install voxelamming
$ pip install --upgrade voxelamming

# サンプルの実行
$ cd sample/python
$ python main.py
# または
$ python3 main.py
```

詳細については、Voxelamming公式ウェブサイトを参照してください：

[Voxelamming公式](https://creativival.github.io/voxelamming/)

## 必須条件

- Python 3.9以上
- Panda3D
- NumPy

これらの依存パッケージは`pip install cubicpy`で自動的にインストールされます。

## フォントについて

本アプリケーションは「PixelMplus（ピクセル・エムプラス）」フォントを使用しています。このフォントは8bitゲーム機のビットマップフォントを再現したTrueTypeフォントです。

### ライセンス情報
PixelMplusフォントはM+ FONT LICENSEの下で提供されています。このライセンスでは、改変の有無や商業利用に関わらず、自由に利用、複製、再配布が可能です（無保証）。

詳細な情報やフォントのダウンロードは以下のリンクから：
https://github.com/itouhiro/PixelMplus

## 著作権

MITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 貢献

バグ報告や機能改善の提案は、GitHubのIssueやPull Requestでお願いします。また、新しいサンプルの作成や、ドキュメントの改善なども歓迎します。

## 開発とリリースプロセス

### CLIモードのテスト

PyPIに新しいバージョンをリリースする前に、ローカルファイルでcli.pyをテストします。

```bash
PYTHONPATH=$PYTHONPATH:. python cubicpy/cli.py
```

### リリース前のテスト

PyPIに新しいバージョンをリリースする前に、すべてが正しく動作することを確認するためにテストを実行することが重要です：

```bash
# 開発依存関係のインストール
pip install pytest

# すべてのテストを実行
pytest

# 特定のテストファイルを実行
pytest tests/test_physics.py
```

### PyPIへの公開

すべてのテストが通過したことを確認した後、パッケージをPyPIに公開できます：

```bash
# ビルドツールのインストール
pip install build twine

# パッケージのビルド
python -m build

# PyPIにアップロード（PyPIアカウントとトークンが必要）
python -m twine upload dist/*
```

PyPIトークンの詳細については、[PyPIドキュメント](https://pypi.org/help/#apitoken)を参照してください。

---

CubicPyで楽しくプログラミングを学びましょう！
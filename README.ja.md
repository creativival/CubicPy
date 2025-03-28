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
    'vec': (10, -5, 3)  # 初速度ベクトル: x, y, z方向
})
```

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

## APIモードのメソッド詳細

### CubicPyAppクラス

```python
CubicPyApp(code_file=None, gravity_factor=1)
```
- `code_file`: 実行するPythonファイルのパス（任意）
- `gravity_factor`: 重力係数（任意、デフォルト: 1）

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
- **マウスホイール**: ズームイン/アウト
- **W/S/A/D**: 地面を傾ける
- **F/G**: 重力の強さを変更
- **R**: リセット
- **Z**: デバッグ表示切替
- **X**: 選択したオブジェクトを削除
- **スペースキー**: 初速度ベクトル(`vec`)が設定されたオブジェクトを発射
- **ESC**: 終了

## 必須条件

- Python 3.9以上
- Panda3D
- NumPy

これらの依存パッケージは`pip install cubicpy`で自動的にインストールされます。

## 著作権

MITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 貢献

バグ報告や機能改善の提案は、GitHubのIssueやPull Requestでお願いします。また、新しいサンプルの作成や、ドキュメントの改善なども歓迎します。

---

CubicPyで楽しくプログラミングを学びましょう！
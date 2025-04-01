# 第1回：キューパイの世界へ飛び込もう！

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**3Dの世界でプログラミングの第一歩を踏み出そう！**

## キューパイって何？

「キュービックパイ」、略して「キューパイ」！これは、みなさんがPythonというプログラミング言語を使って、3D空間に物を置いたり、積み上げたり、壊したりできるプログラミング学習アプリです。

実はね、普通のプログラミングだと「画面に文字を表示する」とか「計算する」とか、ちょっと地味なことから始めることが多いんだ。でも、キューパイなら最初から3D世界で遊べるんだよ！

![CubicPy Sample Animation](https://creativival.github.io/CubicPy/assets/cubicpy_sample.gif)

**▲図1▲ キューパイのサンプルアニメーション**

キューパイでは、こんなことができるよ。

- 箱や球を自由に配置して、建物や塔を作る
- 色とりどりのブロックでアートを作る
- 地面を傾けて、作ったものを崩す実験をする
- 宇宙みたいな低重力や、逆に超重力の世界で遊ぶ
- 物を投げたり、発射したりする物理実験

すごいでしょ？たった数行のコードで、こんな世界が作れちゃうんだ！

## 魔法の道具を手に入れよう

まずは「Python（パイソン）」と「CubicPy（キュービックパイ）」をインストールしましょう。これが今日の最初の冒険です！

### Pythonのインストール

Pythonはプログラミング言語のひとつで、キューパイを動かすために必要です。

お使いのパソコンがMacの場合は、すでにPythonがインストールされています。

Windowsの場合は、Pythonをインストールする必要があります。 インストール方法は簡単です。

![Python Official Download](https://creativival.github.io/CubicPy/assets/python_official_download.png)

**▲図2▲ Pythonの公式ダウンロードページ**

1. [Python公式サイト](https://www.python.org/downloads/)にアクセス
2. 「Download Python」ボタンをクリック
3. ダウンロードしたファイルをダブルクリックして実行
4. **重要！** インストール画面で「Add Python to PATH」にチェックを入れる
5. 「Install Now」をクリック

> 💡 **先生からのヒント**: 「Add Python to PATH」のチェックを忘れると、あとで魔法が使えなくなっちゃうよ！　チェックを忘れたときは、Pythonをアンインストールしてから、再インストールします。

### キューパイ（CubicPy）のインストール

Pythonがインストールできたら、次は「キューパイ」ライブラリをインストールします。ライブラリとは、便利な機能がまとめられたプログラムでインターネットから無料でダウンロードして使うことができます。

> 💡 **先生からのヒント**: ライブラリは「魔法の道具箱」みたいなもの。自分で全部作るのではなく、先輩プログラマーが作った便利な機能をそのまま使えるんだ！キューパイもそんなライブラリの一つだよ。

これには、PowerShell（Windowsの場合）またはターミナル（Macの場合）という、プログラマーの命令を文字で入力する画面を使います。映画で凄腕のハッカーが使っているあれです！普段使っているアプリでは操作できない、パソコンの真の力を使うことができます。

#### Windowsの場合：
1. スタートメニューで「PowerShell」と検索
2. 出てきたアプリをクリックして起動

#### Macの場合：
1. 「Finder」→「アプリケーション」→「ユーティリティ」→「ターミナル」

起動したら、次のコマンド（呪文）を入力してEnterキーを押します。

#### Windowsの場合：
```bash
python -V
```

#### Macの場合：
```bash
python3 -V
```

Pythonのバージョン番号が表示されたら、Pythonが正しくインストールされています。次に、キューパイをインストールします。

![Windows PowerShell](https://creativival.github.io/CubicPy/assets/terminal_pip3_install_cubicpy.png)

**▲図3▲ WindowsのPowerShell**


#### Windowsの場合：
```bash
pip install cubicpy
```

![Mac Terminal](https://creativival.github.io/CubicPy/assets/terminal_pip3_install_cubicpy.png)

**▲図4▲ Macのターミナル**

#### Macの場合：
```bash
pip3 install cubicpy
```

インストールが完了すると、『Successfully installed cubicpy...』のような成功メッセージが表示されます！

**この後の説明では、コマンドの説明では、Windowsの場合のみを記載します。Macの場合は、コマンドの先頭に`python3` `pip3`を付けることを忘れないでください。**

> 🚀 **すごいね！**: たった1行のコマンドで、3D世界を作る魔法の道具が手に入ったよ！

## 最初の呪文を唱えよう

![Cube Tower](https://creativival.github.io/CubicPy/assets/cube_tower.png)

**▲図5▲ ランダムで選ばれたサンプルプログラムの一例**

さあ、キューパイが正しくインストールされたか確かめてみましょう。PowerShellまたはターミナルで、次の呪文を唱えます。

```bash
cubicpy
```

ワオ！画面に3D世界が現れましたか？▲図5▲は、ランダム（無作為）に選ばれたサンプルプログラムです。cubicpyコマンドを実行するたびに、ランダムで選ばれた別のプログラムが実行されます。

## 3D世界を操作しよう

矢印キーでカメラ角度を変えたり、W/A/S/Dキーで地面を傾けたりしてみよう！

> 🎮 **操作方法**:
> - **矢印キー**: カメラ角度の変更
> - **Shift + W/A/S/D/Q/E**: カメラの移動
> - **マウスホイール**: ズームイン/アウト
> - **W/S/A/D**: 地面を傾ける（崩れる！）
> - **F/G**: 重力の強さを変更
> - **R**: リセット
> - **ESC**: 終了

![Breaking Cube Tower](https://creativival.github.io/CubicPy/assets/breaking_cube_tower_sample.png)

**▲図6▲ 床を傾けて、キューブ建築を破壊する**

▲図6▲は、Aキーを押して地面と傾けて、キューブタワーを崩している様子です。

## サンプルで遊んでみよう

キューパイにはいろんなサンプルが用意されています。サンプル一覧を見るには、

```bash
cubicpy --list
# または省略形
cubicpy -l
```
と入力します。すると、たくさんのサンプルが表示されます（▲図7▲）。

![Sample List](https://creativival.github.io/CubicPy/assets/display_sample_list.png)

**▲図7▲ 初めから用意されているサンプルプログラムのリストを表示する**

特定のサンプルを実行するには、

```bash
cubicpy --example cube_tower_sample
# または省略形
cubicpy -e cube_tower_sample
```

を入力します。すると、cube_tower_sampleのサンプルコードが実行されます。

cubicpyを終了するには、`ESC`キーを押すか、PowerShell/ターミナルで`Ctrl+C`を入力します。

cubicpyコマンドはこれまで示したもの以外にも、複数の機能が含まれています。詳細は、この連載記事の中で説明していきます！

## 見て見て！先輩たちの作った作品

これからあなたが作れるようになる素敵な作品の例を見てみましょう。

1. **ピラミッドのフレーム**：簡単なプログラムから、立体的な作品を作ることができます。

![Pyramid Frame](https://creativival.github.io/CubicPy/assets/cube_pyramid_frame.png)

**▲図8▲ ピラミッドのフレーム**

2. **円錐（コーン）の塔**：徐々に半径を小さくすることで、円錐の形を作ることができます。

![Pyramid Frame](https://creativival.github.io/CubicPy/assets/cube_cone.png)

**▲図9▲ 円錐の塔**

3. **ねじれた塔**：トグロをまく蛇ような塔を作ることもできます。

![Pyramid Frame](https://creativival.github.io/CubicPy/assets/cube_twisted_tower.png)

**▲図10▲ ねじれた塔**

次回から、あなた自身がこういう作品を作れるようになりますよ！

## 次回予告

次回は「最初のキューブタワーを作ろう！」。自分だけのカラフルなタワーを作って、思いっきり崩す快感を味わいましょう！

> 🎮 **宿題（やってみよう）**: 今回インストールしたキューパイで、いろんなサンプルを実行して遊んでみよう。いちばん面白かったサンプルはどれかな？

## デバッグのコツ

もしエラーが出たら、こんなことを確認してみよう。

- Pythonは正しくインストールされている？PowerShell/ターミナルで `python --version` と入力すると、バージョンが表示されるはず
- キューパイのインストールは成功した？`pip show cubicpy` と入力するとインストール情報が見られるよ
- コマンドを入力するとき、スペースや大文字・小文字にも注意しよう

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
# 第7回：3Dボーリングゲームを作ろう

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

## 今日のミッション
**自分だけのボーリング場を作って、本格的な3Dボーリングゲームをプログラミングしよう！**

## 前回のおさらい

前回は「APIモードでパワーアップ！」と題して、CubicPyの高度な機能を学びました。APIモードを使うことで、より自由度の高い3D世界を作れるようになりましたね。今回はその知識を活かして、本格的な3Dボーリングゲームを作っていきましょう！

## ボーリングのルールとゲームデザイン

まずは、ボーリングの基本的なルールをおさらいしましょう。

### ボーリングの基本ルール

1. **フレーム構成**: ボーリングは10フレームで構成される
2. **ピン配置**: 10本のピンが三角形状に配置される
3. **得点計算**:
   - ストライク（1投目で10本全て倒した）: 10点 + 次の2投の点数
   - スペア（2投で10本全て倒した）: 10点 + 次の1投の点数
   - オープンフレーム（2投しても全て倒せなかった）: 倒した本数が得点

### ゲームデザイン

シンプルなボーリングゲームから始めて、徐々に機能を追加していきましょう。

1. **ベーシックモード**: 1フレーム、6本のピン、基本的なスコア計算
2. **スタンダードモード**: 10フレーム、10本のピン、本格的なスコア計算
3. **チャレンジモード**: 独自のピン配置、障害物、特殊効果などの追加

今回は、まずベーシックモードを完成させて、徐々に機能を追加していきます。

## ボーリングピンの配置とボールの動き

まずは基本的なボーリングゲームを作ってみましょう。以下のコードをbowling_game.py という名前で保存してください。

```python
from cubicpy import CubicPyApp
import threading
import time
import math

class BowlingGame(CubicPyApp):
    """ボウリングゲーム機能を追加したCubicPyAppの拡張クラス"""
    
    def __init__(self):
        """ボウリングゲームの初期化"""
        # 親クラスのコンストラクタを呼び出し
        super().__init__(gravity_factor=1)
        
        # ゲームの状態を管理する変数
        self.score = 0
        self.pins_knocked_down = 0
        self.pins = []
        self.initial_pin_positions = []
        self.balls_thrown = 0
        self.max_balls = 2  # 1フレームで投げられるボールの数
        self.current_frame = 1
        self.max_frames = 10
        self.frame_scores = [0] * self.max_frames
        
        # スレッド関連の設定
        self.game_thread = None
        self.running = False
        self.last_update_time = 0
        
        # ピン配置の定義（標準的な10ピン配置）
        self.pin_positions = [
            (0, 0, 0),           # 1番ピン（先頭）
            (-1, 1, 0), (1, 1, 0),        # 2-3番ピン
            (-2, 2, 0), (0, 2, 0), (2, 2, 0),  # 4-6番ピン
            (-3, 3, 0), (-1, 3, 0), (1, 3, 0), (3, 3, 0),  # 7-10番ピン
        ]
        
        # 最大スコアを設定
        self.max_score = len(self.pin_positions)
        
        # レーン設定
        self.lane_length = 30  # レーンの長さ
        self.lane_width = 8    # レーンの幅
        
        # ゲームの初期設定
        self.setup_game()
    
    def setup_game(self):
        """ゲームの初期設定"""
        # ボウリングレーン（床）を作成
        self.add_cube(
            position=(0, self.lane_length/2 - 5, -0.1),  # 少し手前に配置
            scale=(self.lane_width, self.lane_length, 0.2),
            color=(0.9, 0.7, 0.5),  # 木目調の色
            mass=0  # 動かないように固定
        )
        
        # ガターを作成（左右）
        for x_offset in [-self.lane_width/2 - 0.5, self.lane_width/2 + 0.5]:
            self.add_cube(
                position=(x_offset, self.lane_length/2 - 5, 0.3),
                scale=(0.5, self.lane_length, 0.8),
                color=(0.3, 0.3, 0.3),  # 暗い色
                mass=0  # 動かないように固定
            )
        
        # ピンを配置
        self.setup_pins()
        
        # ボールを作成
        self.create_ball()
        
        # テキスト表示
        self.set_top_left_text('3Dボウリングゲーム - スペースキーでボールを発射！')
        self.set_bottom_left_text(f"フレーム: {self.current_frame}/{self.max_frames}  投球: {self.balls_thrown+1}/{self.max_balls}")
    
    def setup_pins(self):
        """ピンを配置"""
        # 既存のピンをクリア
        self.pins.clear()
        self.initial_pin_positions.clear()
        
        # ピンを配置
        for i, pos in enumerate(self.pin_positions):
            pin = self.add_cylinder(
                position=(pos[0], pos[1], 1.6),  # 高さを調整
                scale=(0.8, 0.8, 3.2),
                color=(1, 1, 1),  # 白
                base_point=1,     # 底面中心
            )
            # ピンの参照と初期位置を保存
            self.pins.append(pin)
            self.initial_pin_positions.append(pos)
    
    def create_ball(self):
        """ボールを作成"""
        self.ball = self.add_sphere(
            position=(0, -self.lane_length/2 + 5, 1.2),  # レーンの手前に配置
            scale=(1.2, 1.2, 1.2),
            color=(0.3, 0.3, 0.8),  # 青
            mass=10,
            base_point=1,          # 底面中心
        )
    
    def throw_ball(self, angle=0, power=10):
        """ボールを投げる"""
        # 角度に応じた方向ベクトルを計算
        angle_rad = math.radians(angle)
        direction_x = math.sin(angle_rad) * power
        direction_y = math.cos(angle_rad) * power
        
        # ボールに初速度を設定
        self.add_sphere(
            position=(0, -self.lane_length/2 + 5, 1.2),  # レーンの手前に配置
            scale=(1.2, 1.2, 1.2),
            color=(0.3, 0.3, 0.8),  # 青
            mass=10,
            velocity=(direction_x, direction_y, 0),  # 方向と力に応じた初速度
            base_point=1,          # 底面中心
        )
        
        # ボールを投げた回数をカウント
        self.balls_thrown += 1
        
        # テキスト表示更新
        self.set_bottom_left_text(f"フレーム: {self.current_frame}/{self.max_frames}  投球: {self.balls_thrown}/{self.max_balls}")
        
        # ボールを発射
        self.launch_objects()
    
    def start_game_logic(self):
        """ゲームロジックのスレッドを開始"""
        if self.running:
            return
            
        self.running = True
        self.game_thread = threading.Thread(target=self._run_game_logic)
        self.game_thread.daemon = True
        self.game_thread.start()
    
    def stop_game_logic(self):
        """ゲームロジックのスレッドを停止"""
        self.running = False
        if self.game_thread:
            self.game_thread.join(timeout=1.0)
            self.game_thread = None
    
    def get_knocked_pins_count(self):
        """倒れたピンの数を取得"""
        try:
            count = 0
            for i, pin in enumerate(self.pins):
                # ピンが動いたかチェック
                initial_pos = self.initial_pin_positions[i]
                
                # オブジェクト参照から現在位置を取得
                # 注: WorldManagerのオブジェクトリストから探す必要がある
                for obj in self.world_manager.body_objects:
                    if obj['type'] == 'cylinder' and obj['object'] == pin:
                        current_pos = obj['object'].cylinder_node.getPos()
                        current_hpr = obj['object'].cylinder_node.getHpr()
                        
                        # 位置と回転の差を計算
                        dx = abs(current_pos.x - initial_pos[0])
                        dy = abs(current_pos.y - initial_pos[1])
                        
                        # 傾きを計算
                        dh = abs(current_hpr.x) % 360
                        dp = abs(current_hpr.y) % 360
                        
                        # 180度を超える場合は小さい方の角度を使用
                        if dh > 180: dh = 360 - dh
                        if dp > 180: dp = 360 - dp
                        
                        # 位置が大きく変わったか、傾きが大きい場合は倒れたと判断
                        if dx > 0.5 or dy > 0.5 or dh > 45 or dp > 45:
                            count += 1
                        
                        break
            
            return count
        except Exception as e:
            print(f"ピン数の計算中にエラー: {e}")
            return 0
    
    def update_score(self):
        """スコアを更新"""
        knocked_pins = self.get_knocked_pins_count()
        
        if knocked_pins > self.pins_knocked_down:
            self.pins_knocked_down = knocked_pins
            
            # フレームスコアを更新
            self.frame_scores[self.current_frame - 1] = knocked_pins
            
            # 画面表示を更新
            self.set_top_left_text(f'3Dボウリングゲーム - 倒したピン: {knocked_pins}/{self.max_score}')
            
            # すべてのピンを倒した場合（ストライク）
            if knocked_pins == self.max_score:
                self.set_top_left_text(f'ストライク！ 全部倒した！ {knocked_pins}/{self.max_score}')
            # 半分以上倒した場合
            elif knocked_pins > self.max_score // 2:
                self.set_top_left_text(f'ナイス！ {knocked_pins}/{self.max_score}')
    
    def next_ball(self):
        """次の投球に進む"""
        # 全てのピンを倒した場合、または2投目の場合は次のフレームへ
        if self.pins_knocked_down == self.max_score or self.balls_thrown >= self.max_balls:
            self.next_frame()
        else:
            # ボールのみリセット
            self.create_ball()
    
    def next_frame(self):
        """次のフレームに進む"""
        self.current_frame += 1
        self.balls_thrown = 0
        self.pins_knocked_down = 0
        
        # ゲーム終了チェック
        if self.current_frame > self.max_frames:
            self.set_top_left_text(f'ゲーム終了！ 最終スコア: {sum(self.frame_scores)}')
            self.set_bottom_left_text(f"全フレーム終了！ Rキーでリセット")
            return
        
        # ピンとボールをリセット
        self.setup_pins()
        self.create_ball()
        
        # 表示更新
        self.set_bottom_left_text(f"フレーム: {self.current_frame}/{self.max_frames}  投球: {self.balls_thrown+1}/{self.max_balls}")
    
    def _run_game_logic(self):
        """内部スレッドの実行関数"""
        ball_stopped_counter = 0
        last_ball_position = None
        
        while self.running:
            try:
                # 現在の時刻を取得（更新の間隔調整用）
                current_time = time.time()
                
                # 一定間隔でスコア更新（負荷軽減のため）
                if current_time - self.last_update_time > 0.2:  # 0.2秒間隔
                    self.update_score()
                    
                    # ボールの位置を取得
                    ball_position = None
                    for obj in self.world_manager.body_objects:
                        if obj['type'] == 'sphere':
                            ball_position = obj['object'].sphere_node.getPos()
                            break
                    
                    # ボールが停止したかチェック
                    if ball_position and last_ball_position:
                        # ボールの移動距離が小さい場合、停止カウンターを増加
                        dx = abs(ball_position.x - last_ball_position.x)
                        dy = abs(ball_position.y - last_ball_position.y)
                        dz = abs(ball_position.z - last_ball_position.z)
                        
                        if dx < 0.01 and dy < 0.01 and dz < 0.01:
                            ball_stopped_counter += 1
                        else:
                            ball_stopped_counter = 0
                    
                    # ボールが3秒間停止したら次の投球へ
                    if ball_stopped_counter >= 15:  # 0.2秒 x 15 = 3秒
                        self.next_ball()
                        ball_stopped_counter = 0
                    
                    last_ball_position = ball_position
                    self.last_update_time = current_time
                
                time.sleep(0.05)  # 短い待機時間でCPU負荷を抑える
                
            except Exception as e:
                print(f"ゲームロジック実行中にエラー: {e}")
                time.sleep(1)  # エラー時は長めに待機
    
    def reset_game(self):
        """ゲームをリセット"""
        self.current_frame = 1
        self.balls_thrown = 0
        self.pins_knocked_down = 0
        self.frame_scores = [0] * self.max_frames
        
        # ピンとボールをリセット
        self.setup_pins()
        self.create_ball()
        
        # 表示更新
        self.set_top_left_text('3Dボウリングゲーム - スペースキーでボールを発射！')
        self.set_bottom_left_text(f"フレーム: {self.current_frame}/{self.max_frames}  投球: {self.balls_thrown+1}/{self.max_balls}")
    
    def run(self, key_handler=None):
        """ゲームを実行"""
        try:
            # カスタムキーハンドラを設定
            if key_handler:
                self.set_key_handler(key_handler)
            else:
                # デフォルトのキーハンドラを設定
                self.set_key_handler(self.default_key_handler)
            
            # ゲームロジックの開始
            self.start_game_logic()
            
            # 親クラスのrun()を呼び出し
            super().run()
        finally:
            # ゲームロジックの停止
            self.stop_game_logic()
    
    def default_key_handler(self, key):
        """デフォルトのキーハンドラ"""
        if key == 'space':
            # ボールを投げる
            if self.balls_thrown < self.max_balls and self.current_frame <= self.max_frames:
                self.throw_ball()
        elif key == 'r':
            # ゲームをリセット
            self.reset_game()


# メイン実行部分
if __name__ == "__main__":
    # ボウリングゲームを作成
    game = BowlingGame()
    
    # ゲーム実行
    game.run()
```

このコードは、基本的なボーリングゲームの枠組みを実装しています。主な機能は以下の通りです：

1. **ボウリングレーンの作成**: レーンとガターを配置
2. **ピンの配置**: 標準的な10ピン配置
3. **ボールの動き**: 角度とパワーを調整して投げられる
4. **スコア計算**: 倒れたピンを検出して得点を計算
5. **ゲーム進行**: フレームと投球を管理

### コードの解説

#### ピンの配置

ピンは三角形状に配置されています。以下のコードでピンの位置を設定しています。

```python
# ピン配置の定義（標準的な10ピン配置）
self.pin_positions = [
    (0, 0, 0),           # 1番ピン（先頭）
    (-1, 1, 0), (1, 1, 0),        # 2-3番ピン
    (-2, 2, 0), (0, 2, 0), (2, 2, 0),  # 4-6番ピン
    (-3, 3, 0), (-1, 3, 0), (1, 3, 0), (3, 3, 0),  # 7-10番ピン
]
```

#### ボールの動き

ボールは`throw_ball`メソッドで投げることができます。角度とパワーを指定すると、それに応じた方向と速度でボールが発射されます。

```python
def throw_ball(self, angle=0, power=10):
    """ボールを投げる"""
    # 角度に応じた方向ベクトルを計算
    angle_rad = math.radians(angle)
    direction_x = math.sin(angle_rad) * power
    direction_y = math.cos(angle_rad) * power
    
    # ボールに初速度を設定
    self.add_sphere(
        position=(0, -self.lane_length/2 + 5, 1.2),  # レーンの手前に配置
        scale=(1.2, 1.2, 1.2),
        color=(0.3, 0.3, 0.8),  # 青
        mass=10,
        velocity=(direction_x, direction_y, 0),  # 方向と力に応じた初速度
        base_point=1,          # 底面中心
    )
    
    # ボールを発射
    self.launch_objects()
```

#### 倒れたピンの検出

ピンが倒れたかどうかを判定するために、位置と傾きをチェックしています。

```python
def get_knocked_pins_count(self):
    """倒れたピンの数を取得"""
    try:
        count = 0
        for i, pin in enumerate(self.pins):
            # ピンが動いたかチェック
            initial_pos = self.initial_pin_positions[i]
            
            # オブジェクト参照から現在位置を取得
            for obj in self.world_manager.body_objects:
                if obj['type'] == 'cylinder' and obj['object'] == pin:
                    current_pos = obj['object'].cylinder_node.getPos()
                    current_hpr = obj['object'].cylinder_node.getHpr()
                    
                    # 位置と回転の差を計算
                    dx = abs(current_pos.x - initial_pos[0])
                    dy = abs(current_pos.y - initial_pos[1])
                    
                    # 傾きを計算
                    dh = abs(current_hpr.x) % 360
                    dp = abs(current_hpr.y) % 360
                    
                    # 180度を超える場合は小さい方の角度を使用
                    if dh > 180: dh = 360 - dh
                    if dp > 180: dp = 360 - dp
                    
                    # 位置が大きく変わったか、傾きが大きい場合は倒れたと判断
                    if dx > 0.5 or dy > 0.5 or dh > 45 or dp > 45:
                        count += 1
                    
                    break
        
        return count
    except Exception as e:
        print(f"ピン数の計算中にエラー: {e}")
        return 0
```

## スコア計算とゲームの進行

ボーリングのスコア計算にはいくつかのルールがあります。基本的なスコア計算と、ゲームの進行を管理するコードを見ていきましょう。

### スコア計算の実装

スコア計算をさらに本格的にするには、ストライクとスペアを考慮する必要があります。以下のようなメソッドを追加してみましょう。

```python
def calculate_score(self):
    """すべてのフレームのスコアを計算"""
    total_score = 0
    running_score = 0
    
    for i in range(self.max_frames):
        if i >= self.current_frame:
            break
            
        frame_score = self.frame_scores[i]
        
        # ストライク（1投目で10本全て倒した）
        if frame_score == self.max_score and self.balls_thrown == 1:
            # ボーナス: 次の2投の点数を加算
            # 注: 簡易版なので、次の2投が別フレームになる場合は考慮していない
            bonus = 0
            if i + 1 < self.max_frames:
                bonus += self.frame_scores[i + 1]
            frame_score += bonus
        
        # スペア（2投で10本全て倒した）
        elif frame_score == self.max_score and self.balls_thrown == 2:
            # ボーナス: 次の1投の点数を加算
            bonus = 0
            if i + 1 < self.max_frames:
                # 次のフレームの1投目のみを考慮
                bonus += min(self.frame_scores[i + 1], self.max_score // 2)
            frame_score += bonus
        
        running_score += frame_score
        total_score = running_score
    
    return total_score
```

### ゲーム進行の改良

より本格的なゲーム進行のために、以下のようなメソッドを追加しましょう。

```python
def show_score_board(self):
    """スコアボードの表示"""
    score_text = f"フレーム: {self.current_frame}/{self.max_frames}  "
    score_text += f"投球: {self.balls_thrown+1}/{self.max_balls}  "
    score_text += f"スコア: {self.calculate_score()}"
    
    self.set_bottom_left_text(score_text)
    
    # 詳細なスコア表示（オプション）
    if hasattr(self, 'detailed_score_text'):
        detailed_text = "フレーム別スコア: "
        for i in range(self.current_frame):
            if i < len(self.frame_scores):
                detailed_text += f"[{i+1}]:{self.frame_scores[i]} "
        self.detailed_score_text.setText(detailed_text)
```

## 応用編：3Dボーリングゲームの拡張

基本的なボーリングゲームができたので、さらに機能を拡張してみましょう。

### 角度とパワーの調整

より本格的なボーリングゲーム体験のために、ボールの角度とパワーを調整できるようにしましょう。以下のコードを追加してみてください：

```python
def setup_game(self):
    """ゲームの初期設定"""
    # 既存のコード...
    
    # 投球の設定
    self.throw_angle = 0  # 初期角度（度）
    self.throw_power = 10  # 初期パワー
    
    # 矢印表示（方向指示器）
    self.direction_indicator = self.add_cube(
        position=(0, -self.lane_length/2 + 3, 0.1),
        scale=(0.2, 2, 0.1),
        color=(1, 0, 0),  # 赤
        mass=0  # 動かないように
    )
    
    # テキスト表示
    self.set_top_left_text('3Dボウリングゲーム - スペースキーでボールを発射！')
    self.set_bottom_left_text(f"フレーム: {self.current_frame}/{self.max_frames}  投球: {self.balls_thrown+1}/{self.max_balls}")
    
    # パワーと角度の表示
    self.power_angle_text = Draw2DText(self.font, self.a2dBottomRight, 
                                      f"角度: {self.throw_angle}° パワー: {self.throw_power}",
                                      pos=(-1.0, 0.1))

def default_key_handler(self, key):
    """デフォルトのキーハンドラ"""
    if key == 'space':
        # ボールを投げる
        if self.balls_thrown < self.max_balls and self.current_frame <= self.max_frames:
            self.throw_ball(self.throw_angle, self.throw_power)
    elif key == 'r':
        # ゲームをリセット
        self.reset_game()
    elif key == 'left' or key == 'a':
        # 左に角度を調整
        self.throw_angle = max(self.throw_angle - 5, -45)
        self.update_direction_indicator()
    elif key == 'right' or key == 'd':
        # 右に角度を調整
        self.throw_angle = min(self.throw_angle + 5, 45)
        self.update_direction_indicator()
    elif key == 'up' or key == 'w':
        # パワーを上げる
        self.throw_power = min(self.throw_power + 1, 20)
        self.update_power_angle_display()
    elif key == 'down' or key == 's':
        # パワーを下げる
        self.throw_power = max(self.throw_power - 1, 5)
        self.update_power_angle_display()

def update_direction_indicator(self):
    """方向指示器の回転を更新"""
    if hasattr(self, 'direction_indicator'):
        self.direction_indicator.setH(self.throw_angle)
        self.update_power_angle_display()

def update_power_angle_display(self):
    """パワーと角度の表示を更新"""
    if hasattr(self, 'power_angle_text'):
        self.power_angle_text.setText(f"角度: {self.throw_angle}° パワー: {self.throw_power}")
```

### マルチプレイヤー対応

複数人でプレイできるように、プレイヤー管理機能を追加してみましょう：

```python
def __init__(self):
    """ボウリングゲームの初期化"""
    # 親クラスのコンストラクタを呼び出し
    super().__init__(gravity_factor=1)
    
    # ゲームの状態を管理する変数
    self.players = ["プレイヤー1", "プレイヤー2"]  # プレイヤー名
    self.current_player = 0  # 現在のプレイヤーのインデックス
    
    # 各プレイヤーのスコアを管理
    self.player_scores = []
    for _ in range(len(self.players)):
        self.player_scores.append([0] * self.max_frames)
    
    # 他の初期化コード...

```python
def next_player(self):
    """次のプレイヤーに切り替え"""
    self.current_player = (self.current_player + 1) % len(self.players)
    
    # 表示を更新
    self.set_top_left_text(f"{self.players[self.current_player]}の番 - スペースキーでボールを発射！")
    self.show_score_board()
```

## チャレンジ：オリジナルのボーリング場を作ろう

基本的な3Dボーリングゲームができたので、次は自分だけのオリジナルボウリング場を作ってみましょう！以下のようなアイデアで拡張してみてください。

### 1. 障害物を追加

レーン上に障害物を配置して、ボールの軌道を複雑にしてみましょう。以下のコードで障害物を追加できます：

```python
def add_obstacles(self):
    """レーン上に障害物を追加"""
    # バンパー（レーンの途中の障害物）
    for x_pos in [-2, 2]:
        for y_pos in [5, 15]:
            self.add_cylinder(
                position=(x_pos, y_pos, 1),
                scale=(0.8, 0.8, 2),
                color=(0.7, 0.2, 0.2),  # 赤っぽい色
                mass=0  # 動かないように固定
            )
    
    # ランプ（傾斜のある障害物）
    self.add_cube(
        position=(0, 10, 0.5),
        scale=(3, 3, 1),
        color=(0.2, 0.7, 0.2),  # 緑っぽい色
        mass=0,  # 動かないように固定
        hpr=(0, 10, 0)  # X軸回りに10度傾ける
    )
```

### 2. カスタムピン配置

独自のピン配置を作ってみましょう：

```python
def setup_custom_pins(self, pattern="standard"):
    """カスタムピン配置"""
    # 既存のピンをクリア
    self.pins.clear()
    self.initial_pin_positions.clear()
    
    if pattern == "standard":
        # 標準的な10ピン配置
        self.pin_positions = [
            (0, 0, 0),           # 1番ピン（先頭）
            (-1, 1, 0), (1, 1, 0),        # 2-3番ピン
            (-2, 2, 0), (0, 2, 0), (2, 2, 0),  # 4-6番ピン
            (-3, 3, 0), (-1, 3, 0), (1, 3, 0), (3, 3, 0),  # 7-10番ピン
        ]
    elif pattern == "diamond":
        # ダイヤモンド型配置
        self.pin_positions = [
            (0, 0, 0),          # 中央
            (-2, 2, 0), (2, 2, 0), (0, 4, 0), # 周囲
            (-4, 4, 0), (4, 4, 0), (-2, 6, 0), (2, 6, 0), # 外周
            (0, 8, 0) # 最奥
        ]
    elif pattern == "circle":
        # 円形配置
        self.pin_positions = []
        radius = 3
        for i in range(10):
            angle = 2 * math.pi * i / 10
            x = radius * math.cos(angle)
            y = radius * math.sin(angle) + radius  # 中心を少し奥にずらす
            self.pin_positions.append((x, y, 0))
    
    # ピンを配置
    for pos in self.pin_positions:
        pin = self.add_cylinder(
            position=(pos[0], pos[1], 1.6),  # 高さを調整
            scale=(0.8, 0.8, 3.2),
            color=(1, 1, 1),  # 白
            base_point=1,     # 底面中心
        )
        # ピンの参照と初期位置を保存
        self.pins.append(pin)
        self.initial_pin_positions.append(pos)
    
    # 最大スコアを更新
    self.max_score = len(self.pin_positions)
```

### 3. テーマパークボウリング

テーマパークのような楽しいボウリング場を作ってみましょう：

```python
def setup_themed_bowling(self, theme="space"):
    """テーマに合わせたボウリング場の設定"""
    if theme == "space":
        # 宇宙テーマ
        # 重力を下げる
        self.change_gravity(0.3)
        
        # 背景を黒に
        self.setBackgroundColor(0, 0, 0)
        
        # 宇宙のような床
        self.add_cube(
            position=(0, self.lane_length/2 - 5, -0.1),
            scale=(self.lane_width, self.lane_length, 0.2),
            color=(0.1, 0.1, 0.3),  # 暗い青
            mass=0
        )
        
        # 星のような装飾（発光する球体）
        for _ in range(20):
            x = random.uniform(-15, 15)
            y = random.uniform(-10, 30)
            z = random.uniform(5, 15)
            size = random.uniform(0.1, 0.5)
            
            self.add_sphere(
                position=(x, y, z),
                scale=(size, size, size),
                color=(1, 1, 1),  # 白
                mass=0
            )
    
    elif theme == "beach":
        # ビーチテーマ
        # 背景を水色に
        self.setBackgroundColor(0.5, 0.8, 1.0)
        
        # 砂浜のような床
        self.add_cube(
            position=(0, self.lane_length/2 - 5, -0.1),
            scale=(self.lane_width, self.lane_length, 0.2),
            color=(0.9, 0.8, 0.6),  # 砂色
            mass=0
        )
        
        # 波のような装飾
        for i in range(10):
            x = -self.lane_width/2 - 2 + i * 2
            
            self.add_cylinder(
                position=(x, self.lane_length/2, 0.5),
                scale=(0.5, 0.5, random.uniform(0.5, 1.5)),
                color=(0.7, 0.8, 1.0),  # 水色
                mass=0
            )
```

## 完成したボウリングゲームの実行

以上のコードを組み合わせて、オリジナルの3Dボウリングゲームを作成できました！以下のように実行して遊んでみましょう：

```python
if __name__ == "__main__":
    # ボウリングゲームを作成
    game = BowlingGame()
    
    # テーマ設定（オプション）
    # game.setup_themed_bowling("space")
    
    # カスタムピン配置（オプション）
    # game.setup_custom_pins("diamond")
    
    # 障害物追加（オプション）
    # game.add_obstacles()
    
    # ゲーム実行
    game.run()
```

## デバッグのコツ

3Dゲームを作るときに役立つデバッグのコツをいくつか紹介します：

1. **位置関係の確認**: カメラを移動して、オブジェクトが正しい位置に配置されているか確認しましょう
2. **物理挙動の調整**: 重力係数（`gravity_factor`）を変更して、ピンの倒れやすさを調整できます
3. **オブジェクトの参照**: `world_manager.body_objects`からオブジェクトを検索するときは、型や参照を慎重に確認しましょう
4. **エラーログの活用**: `print`文を使って、変数の値や処理の流れを確認することが有効です

## まとめ：今回学んだこと

1. **3Dボーリングゲームの基本実装**: ボウリングレーン、ピン、ボールの配置と物理挙動
2. **スコア計算**: 倒れたピンを検出し、得点を計算する方法
3. **ゲーム進行管理**: フレームと投球を管理し、ゲームの流れを制御する方法
4. **ユーザーインタラクション**: キー入力で角度やパワーを調整する仕組み
5. **拡張機能の実装**: マルチプレイヤー対応、障害物追加、テーマ設定など

これらを応用すれば、さらに複雑で面白いゲームを作ることができます。

## 次回予告

次回は「立体迷路ゲームを作ろう！」をテーマに、3D空間内を移動しながら目標を達成するゲームの作り方を学びます。移動と衝突判定のプログラミング、目標達成の判定方法、ゲームメカニクスの設計など、ゲーム開発の基本をさらに深く探究していきましょう！

> 🎮 **宿題（やってみよう）**: 今回紹介したコードを元に、自分だけのボウリングゲームを作ってみよう。障害物の配置やピンの並びを工夫したり、新しいテーマを追加したりして、友達に自慢できるオリジナルゲームを目指そう！

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**
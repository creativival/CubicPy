from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from panda3d.core import *
from . import (
    CameraControl, Axis, Box, Sphere, Cylinder, SafeExec,
    InputHandler, ModelManager, PhysicsEngine
)


class CubicPyApp(ShowBase):
    GRAVITY_VECTOR = Vec3(0, 0, -9.81)
    RESTITUTION = 0  # 反発係数
    FRICTION = 0.5  # 摩擦係数

    def __init__(self, code_file, gravity_factor=1):
        ShowBase.__init__(self)
        self.code_file = code_file
        self.gravity_factor = gravity_factor
        self.body_objects = []
        self.tilt_x = 0
        self.tilt_y = 0
        self.tilt_speed = 5
        self.target_tilt_x = 0
        self.target_tilt_y = 0
        self.tilt_step = 0  # 現在のフレーム数
        self.max_tilt_frames = 10  # 10フレームかけて傾ける

        # ウィンドウ設定など
        props = WindowProperties()
        props.setTitle('CubicPy World')
        props.setSize(1800, 1200)
        self.win.requestProperties(props)

        # カメラの位置を設定
        CameraControl(self)

        # 座標軸を描画
        Axis(self)

        # モデル管理
        self.model_manager = ModelManager(self)

        # 物理エンジン
        self.physics = PhysicsEngine(self, gravity_factor)

        # すべてのノードの親
        self.world_node = self.render.attachNewNode("world_node")

        # ユーザーコードよりワールドを生成する
        self.build_world()

        # キー入力ハンドラの設定
        self.input_handler = InputHandler(self)

        # Task
        # 物理演算を実行
        self.taskMgr.add(self.update, 'update')

    def tilt_ground(self, dx, dy):
        """目標の傾きを設定し、100フレームでゆっくり傾ける"""
        self.target_tilt_x = self.tilt_x + dx * self.tilt_speed
        self.target_tilt_y = self.tilt_y + dy * self.tilt_speed
        print(f'Target Tilt: {self.target_tilt_x}, {self.target_tilt_y}')
        self.tilt_step = 0  # 現在のフレーム数
        self.taskMgr.add(self.smooth_tilt_update, 'smooth_tilt_update')

    def smooth_tilt_update(self, task):
        """100フレームで徐々に地面を傾ける処理"""
        if self.tilt_step >= self.max_tilt_frames:
            # 重力の再設定
            self.change_gravity(1)
            return task.done  # 完了したらタスクを終了

        # 徐々に目標角度に近づける
        alpha = (self.tilt_step + 1) / self.max_tilt_frames
        self.tilt_x = (1 - alpha) * self.tilt_x + alpha * self.target_tilt_x
        self.tilt_y = (1 - alpha) * self.tilt_y + alpha * self.target_tilt_y

        # ワールドの回転を適用
        self.world_node.setHpr(0, self.tilt_x, self.tilt_y)

        self.tilt_step += 1  # フレームカウントを増やす
        return task.cont  # 継続実行

    def build_body_data(self, body_data):
        for body in body_data:
            if body['type'] == 'box':
                body_object = Box(self, body)
            elif body['type'] == 'sphere':
                body_object = Sphere(self, body)
            elif body['type'] == 'cylinder':
                body_object = Cylinder(self, body)
            else:
                body_object = Box(self, body)
            self.body_objects.append({'type': body['type'], 'object': body_object})

    def toggle_debug(self):
        self.physics.toggle_debug()

    def change_gravity(self, value):
        # 物理エンジンの重力を変更
        self.physics.change_gravity(value)
        # そしてワールドを再構築
        self.reset_build()

    # 物理演算を定期実行
    def update(self, task):
        dt = globalClock.getDt()
        self.physics.update(dt)
        return task.cont

    def reset_world_rotation(self):
        # ワールドの傾斜をリセット
        self.tilt_x = 0
        self.tilt_y = 0
        self.world_node.setHpr(0, 0, 0)

    def reset_gravity(self):
        # 重力を初期化
        self.physics.reset_gravity()

    def reset_build(self):
        """物理エンジンをリセットし、建物を再生成する"""
        # 既存のオブジェクトを削除
        for body in self.body_objects:
            body['object'].remove()

        self.body_objects = []

        # ワールドを再生成
        self.build_world()

    def build_world(self):
        """地面と建物を生成する"""
        safe_exec = SafeExec(self.code_file)
        body_data = safe_exec.run()

        # 地面を作成
        body_data.append({
            'type': 'box',
            'pos': (-500, -500, -1),
            'scale': (1000, 1000, 1),
            'color': (0, 1, 0),
            'mass': 0,
            'color_alpha': 0.3
        })

        # 建物を再構築
        self.build_body_data(body_data)

        # 物理エンジンを即座に更新
        self.physics.bullet_world.doPhysics(0)

    def reset_all(self):
        self.reset_gravity()
        self.reset_world_rotation()
        self.reset_build()
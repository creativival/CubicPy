from panda3d.core import *
from . import Box, Sphere, Cylinder, SafeExec


class WorldManager:
    """ワールドとオブジェクト管理クラス"""

    def __init__(self, app):
        self.app = app
        self.body_objects = []

        # 回転状態の初期化
        self.tilt_x = 0
        self.tilt_y = 0
        self.tilt_speed = 5
        self.target_tilt_x = 0
        self.target_tilt_y = 0
        self.tilt_step = 0
        self.max_tilt_frames = 10

        # ワールドのルートノード
        self.world_node = self.app.render.attachNewNode("world_node")

    def tilt_ground(self, dx, dy):
        """目標の傾きを設定し、徐々に傾ける"""
        self.target_tilt_x = self.tilt_x + dx * self.tilt_speed
        self.target_tilt_y = self.tilt_y + dy * self.tilt_speed
        print(f'Target Tilt: {self.target_tilt_x}, {self.target_tilt_y}')
        self.tilt_step = 0
        self.app.taskMgr.add(self.smooth_tilt_update, 'smooth_tilt_update')

    def smooth_tilt_update(self, task):
        """徐々に傾きを変更するタスク"""
        if self.tilt_step >= self.max_tilt_frames:
            # 重力の再設定
            self.app.change_gravity(1)
            return task.done

        # 徐々に目標角度に近づける
        alpha = (self.tilt_step + 1) / self.max_tilt_frames
        self.tilt_x = (1 - alpha) * self.tilt_x + alpha * self.target_tilt_x
        self.tilt_y = (1 - alpha) * self.tilt_y + alpha * self.target_tilt_y

        # ワールドの回転を適用
        self.world_node.setHpr(0, self.tilt_x, self.tilt_y)

        self.tilt_step += 1
        return task.cont

    def reset_rotation(self):
        """回転をリセット"""
        self.tilt_x = 0
        self.tilt_y = 0
        self.world_node.setHpr(0, 0, 0)

    def build_body_data(self, body_data):
        """オブジェクトデータからボディを構築"""
        for body in body_data:
            if body['type'] == 'box':
                body_object = Box(self.app, body)
            elif body['type'] == 'sphere':
                body_object = Sphere(self.app, body)
            elif body['type'] == 'cylinder':
                body_object = Cylinder(self.app, body)
            else:
                body_object = Box(self.app, body)
            self.body_objects.append({'type': body['type'], 'object': body_object})

    def build_world(self):
        """地面と建物を生成する"""
        safe_exec = SafeExec(self.app.code_file)
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
        self.app.physics.bullet_world.doPhysics(0)

    def rebuild(self):
        """ワールドを再構築"""
        # 既存のオブジェクトを削除
        for body in self.body_objects:
            body['object'].remove()

        self.body_objects = []

        # ワールドを再生成
        self.build_world()

    def get_world_node(self):
        """ワールドノードを取得"""
        return self.world_node

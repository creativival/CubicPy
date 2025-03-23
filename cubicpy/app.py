from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from panda3d.core import *
from . import (
    CameraControl, Axis, InputHandler,
    ModelManager, PhysicsEngine, WorldManager
)


class CubicPyApp(ShowBase):
    """CubicPy アプリケーションのメインクラス"""
    GRAVITY_VECTOR = Vec3(0, 0, -9.81)
    RESTITUTION = 0  # 反発係数
    FRICTION = 0.5  # 摩擦係数

    def __init__(self, code_file, gravity_factor=1):
        ShowBase.__init__(self)
        self.code_file = code_file
        self.gravity_factor = gravity_factor

        # ウィンドウ設定
        self.setup_window("CubicPy World", (1800, 1200))

        # カメラと座標軸
        CameraControl(self)
        Axis(self)

        # 各サブシステムの初期化
        self.model_manager = ModelManager(self)
        self.physics = PhysicsEngine(self, gravity_factor)

        # ワールド管理システムの初期化
        self.world_manager = WorldManager(self)

        # ワールド構築 - WorldManagerの初期化後に実行
        self.world_manager.build_world()

        # 入力ハンドラの設定
        self.input_handler = InputHandler(self)

        # 物理シミュレーションタスクの開始
        self.taskMgr.add(self.update_physics, 'update_physics')

    def setup_window(self, title, size):
        """ウィンドウ設定"""
        props = WindowProperties()
        props.setTitle(title)
        props.setSize(*size)
        self.win.requestProperties(props)

    def update_physics(self, task):
        """物理シミュレーションの更新"""
        dt = globalClock.getDt()
        self.physics.update(dt)
        return task.cont

    # 委譲メソッド - WorldManagerへ転送
    def tilt_ground(self, dx, dy):
        self.world_manager.tilt_ground(dx, dy)

    def toggle_debug(self):
        self.physics.toggle_debug()

    def change_gravity(self, value):
        # 物理エンジンの重力を変更
        self.physics.change_gravity(value)
        # そしてワールドを再構築
        self.world_manager.rebuild()

    def reset_all(self):
        """すべてをリセット"""
        self.physics.reset_gravity()
        self.world_manager.reset_rotation()
        self.world_manager.rebuild()

    @property
    def world_node(self):
        """ワールドノードへの参照を提供"""
        return self.world_manager.get_world_node()
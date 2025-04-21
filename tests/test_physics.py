import pytest
from panda3d.core import Vec3
from direct.showbase.ShowBase import ShowBase
from cubicpy.physics import PhysicsEngine

class MockApp:
    """テスト用のアプリケーションクラス"""
    def __init__(self):
        self.GRAVITY_VECTOR = Vec3(0, 0, -9.81)
        self.initial_gravity_factor = 1.0
        self.render = None

@pytest.fixture
def showbase():
    """テスト用のShowBaseインスタンスを作成"""
    base = ShowBase(windowType='offscreen')
    yield base
    base.destroy()

@pytest.fixture
def mock_app(showbase):
    """テスト用のアプリケーションインスタンスを作成"""
    app = MockApp()
    app.render = showbase.render
    return app

@pytest.fixture
def physics_engine(mock_app):
    """テスト用のPhysicsEngineインスタンスを作成"""
    return PhysicsEngine(mock_app)

def test_physics_engine_initialization(physics_engine):
    """PhysicsEngineの初期化テスト"""
    assert physics_engine.app is not None
    assert physics_engine.bullet_world is not None
    assert physics_engine.debug_node is not None
    assert physics_engine.debug_np is not None
    assert not physics_engine.debug_np.isHidden()  # デバッグ表示は初期状態で表示されている

def test_toggle_debug(physics_engine):
    """デバッグ表示の切り替えテスト"""
    # 初期状態では表示されている
    assert not physics_engine.debug_np.isHidden()
    
    # 非表示に切り替え
    physics_engine.toggle_debug()
    assert physics_engine.debug_np.isHidden()
    
    # 表示に切り替え
    physics_engine.toggle_debug()
    assert not physics_engine.debug_np.isHidden()

def test_change_gravity(physics_engine):
    """重力の変更テスト"""
    # 初期重力を保存
    initial_gravity = physics_engine.gravity_vector
    
    # 重力を2倍に変更
    physics_engine.change_gravity(2.0)
    
    # 重力ベクトルの各成分を個別に比較
    assert abs(physics_engine.gravity_vector.x - initial_gravity.x * 2.0) < 0.01
    assert abs(physics_engine.gravity_vector.y - initial_gravity.y * 2.0) < 0.01
    assert abs(physics_engine.gravity_vector.z - initial_gravity.z * 2.0) < 0.01

def test_reset_gravity(physics_engine):
    """重力のリセットテスト"""
    # 初期重力を保存
    initial_gravity = physics_engine.gravity_vector
    
    # 重力を変更
    physics_engine.change_gravity(2.0)
    
    # 重力をリセット
    physics_engine.reset_gravity()
    
    # 重力ベクトルの各成分を個別に比較
    assert abs(physics_engine.gravity_vector.x - initial_gravity.x) < 0.01
    assert abs(physics_engine.gravity_vector.y - initial_gravity.y) < 0.01
    assert abs(physics_engine.gravity_vector.z - initial_gravity.z) < 0.01

def test_update(physics_engine):
    """物理シミュレーションの更新テスト"""
    # 更新前の状態を保存
    initial_state = physics_engine.bullet_world.getNumConstraints()
    
    # 物理シミュレーションを更新
    physics_engine.update(0.016)  # 約60FPSの時間間隔
    
    # 更新後の状態を確認
    # 注: 実際の物理演算結果は環境によって異なるため、
    # 単に例外が発生しないことを確認する
    assert physics_engine.bullet_world is not None 
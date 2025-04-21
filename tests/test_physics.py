import pytest
from panda3d.core import Vec3
from direct.showbase.ShowBase import ShowBase
from cubicpy.physics import PhysicsEngine

@pytest.fixture
def showbase():
    """テスト用のShowBaseインスタンスを作成"""
    base = ShowBase(windowType='offscreen')
    base.GRAVITY_VECTOR = Vec3(0, 0, -9.81)
    base.initial_gravity_factor = 1.0
    yield base
    base.destroy()

@pytest.fixture
def physics(showbase):
    """テスト用の物理エンジンインスタンスを作成"""
    return PhysicsEngine(showbase)

def test_physics_initialization(physics):
    """物理エンジンの初期化テスト"""
    assert isinstance(physics, PhysicsEngine)
    assert physics.bullet_world is not None
    assert physics.debug_node is not None
    assert physics.debug_np is not None

def test_gravity_initialization(physics):
    """重力の初期化テスト"""
    expected_gravity = Vec3(0, 0, -9.81)
    assert physics.gravity_vector == expected_gravity

def test_gravity_change(physics):
    """重力の変更テスト"""
    physics.change_gravity(2.0)
    
    expected_gravity = Vec3(0, 0, -19.62)
    assert abs(physics.gravity_vector.z - expected_gravity.z) < 0.01

def test_gravity_reset(physics):
    """重力のリセットテスト"""
    physics.change_gravity(2.0)
    
    physics.reset_gravity()
    
    expected_gravity = Vec3(0, 0, -9.81)
    assert physics.gravity_vector == expected_gravity

def test_debug_toggle(physics):
    """デバッグ表示の切り替えテスト"""
    assert not physics.debug_np.isHidden()
    
    physics.toggle_debug()
    assert physics.debug_np.isHidden()
    
    physics.toggle_debug()
    assert not physics.debug_np.isHidden() 
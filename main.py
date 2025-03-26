from cubicpy.app import CubicPyApp


if __name__ == '__main__':
    # sample code file
    user_code_file = 'cubicpy/examples/cube_tower_sample.py'
    user_code_file = 'cubicpy/examples/sphere_tower_sample.py'
    user_code_file = 'cubicpy/examples/cylinder_tower_sample.py'
    user_code_file = 'cubicpy/examples/box_building_sample.py'
    user_code_file = 'cubicpy/examples/box_cylinder_sample.py'
    user_code_file = 'cubicpy/examples/column_building_2x2_sample.py'
    user_code_file = 'cubicpy/examples/column_building_3x3_sample.py'
    user_code_file = 'cubicpy/examples/falling_sphere_sample.py'
    user_code_file = 'cubicpy/examples/throwing_sphere_sample.py'

    # user code file
    # user_code_file = 'codes/box_twisted_tower.py'

    app = CubicPyApp(user_code_file, gravity_factor=1, window_size=(1800, 1200))
    app.run()

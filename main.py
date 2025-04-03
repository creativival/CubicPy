from cubicpy.app import CubicPyApp


if __name__ == '__main__':
    # sample code file
    user_code_file = 'cubicpy/examples/cube_tower_sample.py'
    user_code_file = 'cubicpy/examples/sphere_tower_sample.py'
    user_code_file = 'cubicpy/examples/cylinder_tower_sample.py'
    user_code_file = 'cubicpy/examples/box_building_sample.py'
    user_code_file = 'cubicpy/examples/box_cylinder_sample.py'
    user_code_file = 'cubicpy/examples/frame_building_2x2_sample.py'
    user_code_file = 'cubicpy/examples/frame_building_3x3_sample.py'
    user_code_file = 'cubicpy/examples/falling_sphere_sample.py'
    user_code_file = 'cubicpy/examples/throwing_sphere_sample.py'

    # user code file
    user_code_file = 'codes/cube_twisted_tower.py'
    user_code_file = 'codes/cube_cone.py'
    user_code_file = 'codes/cube_pyramid_frame.py'
    user_code_file = 'codes/cube_cylinder_shape_tower.py'
    user_code_file = 'codes/frame_building_2x2.py.py'
    user_code_file = 'codes/frame_building_2x2_resized.py'
    user_code_file = 'codes/five_random_buildings.py'
    user_code_file = 'codes/simple_district.py'
    user_code_file = 'codes/create_city_100x100.py'
    user_code_file = 'codes/create_city_100x100_with_meteor.py'
    user_code_file = 'codes/simple_domino.py'
    user_code_file = 'codes/circular_domino.py'
    user_code_file = 'codes/spiral_domino.py'
    user_code_file = 'codes/domino_patterns.py'
    user_code_file = 'codes/list_pattern_domino.py'
    # user_code_file = 'codes/fractal_tree.py'
    # user_code_file = 'codes/spiral_tower.py.py'

    app = CubicPyApp(user_code_file, gravity_factor=1, window_size=(1800, 1200))
    # app = CubicPyApp(user_code_file, gravity_factor=0.1, window_size=(900, 600))
    app.run()

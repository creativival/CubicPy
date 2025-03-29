from cubicpy.app import CubicPyApp


if __name__ == '__main__':
    user_code_file = 'cubicpy/examples/delete_cube_tower_sample.py'
    user_code_file = 'cubicpy/examples/delete_cube_building_sample.py'
    user_code_file = 'cubicpy/examples/delete_frame_building_2x2_sample.py'
    user_code_file = 'cubicpy/examples/delete_frame_building_3x3_sample.py'

    app = CubicPyApp(user_code_file, gravity_factor=1, window_size=(1800, 1200))
    app.run()

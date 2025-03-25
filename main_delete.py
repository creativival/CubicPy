from cubicpy.app import CubicPyApp


if __name__ == '__main__':
    user_code_file = 'cubicpy/examples/box_tower_delete_sample.py'

    app = CubicPyApp(user_code_file, gravity_factor=10, window_size=(1800, 1200))
    app.run()

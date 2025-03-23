from cubicpy.app import CubicPyApp


if __name__ == '__main__':
    user_code_file = 'cubicpy/examples/box_line_sample.py'

    app = CubicPyApp(user_code_file, gravity_factor=-4)
    app.run()

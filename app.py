from flask import Flask


def create_app():
    """
    This function will create the Flask app using Factory Pattren
    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_object("config.settings")
    # app.config.from_pyfile('settings.py', silent=True)

    @app.route("/")
    def index():
        return "Hello World"

    return app

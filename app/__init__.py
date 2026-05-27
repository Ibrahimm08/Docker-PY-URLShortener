from flask import Flask

def create_app():
    app = Flask(__name__)

    # To add more pages make sure we import and register them
    from .routes import main
    app.register_blueprint(main)

    return app

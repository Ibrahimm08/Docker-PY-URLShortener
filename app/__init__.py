from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # db and app connection
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
    db.init_app(app)
    
    from .scheduler import start_scheduler

    with app.app_context():
        db.create_all()
        start_scheduler()

    
    from .routes import main
    app.register_blueprint(main)

    return app

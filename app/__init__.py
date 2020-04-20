from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db, config_object.MIGRATIONS_DIR)

    from app.routes import bp
    app.register_blueprint(bp)

    return app


if __name__ == '__main__':
    create_app().run()

import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # turns SESSION_COOKIE_HTTPONLY off so that the XSS injection works
    app.config["SESSION_COOKIE_HTTPONLY"] = False

    from . import db
    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
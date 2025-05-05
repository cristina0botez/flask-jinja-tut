from flask import Flask
from flask_assets import Environment

from flask_jinja_tut.assets import compile_static_assets


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)
    with app.app_context():
        from flask_jinja_tut import routes
        from flask_jinja_tut.home import routes
        app.register_blueprint(routes.home_bp)
        compile_static_assets(assets)
        return app

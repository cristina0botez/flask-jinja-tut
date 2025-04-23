from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    with app.app_context():
        from flask_jinja_tut import routes
        return app

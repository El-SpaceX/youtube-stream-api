from flask import Flask
from .routes.play import play_bp
from .routes.search import search_bp
from .routes.search_and_play import search_and_play_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(play_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(search_and_play_bp)
    return app
from flask import Flask
from app.route import index, other


def create_app():

    app = Flask(__name__)

    app.add_url_rule('/index', 'index', index)

    app.add_url_rule('/other', 'other', other)

    return app

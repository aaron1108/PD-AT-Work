from flask import Flask
from app.route import index, other, get_wagerdiv, test_start


def create_app():

    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)

    app.add_url_rule('/other', 'other', other)

    app.add_url_rule('/get_wagerdiv', None, get_wagerdiv)

    app.add_url_rule('/start_test', None, test_start)

    return app

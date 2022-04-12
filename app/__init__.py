from app.db import init_db
from app.utils import filters
from app.routes import home, dashboard
# we import the Flask function and use the 'def' keyword to define what create_app() does
from flask import Flask 
# when Flask runs the app package it will be looking for create_app() function


def create_app(test_config=None):
    #set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='byrd_is_the_word'
    )
    

    @app.route('/hello')
    def hello():
        return 'hello world this is my first python app'

    # registering the routes!
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
 
    init_db(app)
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    return app
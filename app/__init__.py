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

    return app
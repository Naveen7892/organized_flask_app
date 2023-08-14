from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask Extensions (eg: Flask-SQLAlchemy)

    # Register Blueprints

    @app.route("/test")
    def test_page():
        return '<h1>Testing Factory Pattern in Flask app.</h1>'
    
    return app
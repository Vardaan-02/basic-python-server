from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-fallback')

    from .routes.core import core_bp
    app.register_blueprint(core_bp)

    return app

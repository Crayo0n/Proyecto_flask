from flask import Flask
from config import Config

def create_app(config_class=Config):
    """Factory para crear la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Registrar blueprints
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
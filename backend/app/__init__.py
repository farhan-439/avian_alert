from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config.Config')
    app.config.from_pyfile('config.py', silent=True)

    CORS(app)
    db.init_app(app)

    # Register Blueprints
    from .routes.audio import audio_bp
    from .routes.image import image_bp
    from .routes.simulate import simulate_bp
    from .routes.notifications import notif_bp

    app.register_blueprint(audio_bp, url_prefix='/api/audio')
    app.register_blueprint(image_bp, url_prefix='/api/image')
    app.register_blueprint(simulate_bp, url_prefix='/api/simulate')
    app.register_blueprint(notif_bp, url_prefix='/api/notify')

    return app

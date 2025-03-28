from flask import Flask
from app.models.user import db
from app.routes.auth_routes import auth_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app

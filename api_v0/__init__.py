# -*- coding:utf-8 -*-
from api.wallet import WalletClient
import config
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
wallet_client = WalletClient(config.client)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    db.init_app(app)
    login_manager.init_app(app)
    from .auth import auth
    app.register_blueprint(auth)
    return app


if __name__ == "__main__":
    create_app()

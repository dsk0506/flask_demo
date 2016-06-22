# coding: UTF-8
from flask import Flask
from config import load_config  # 绝对导入


def create_app():
    """创建Flask app"""
    app = Flask(__name__)
    # Load config
    config = load_config()
    app.config.from_object(config)

    return app


app = create_app()
from app.modules.user.controllers import *

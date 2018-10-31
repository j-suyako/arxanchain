# -*- coding:utf-8 -*-
import os
from api_v0 import create_app, db
from flask_script import Manager

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
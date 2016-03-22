from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from extensions import DB
from blueprints import blueprint
from models import TeamMember


def generate_application(config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    DB.init_app(app)
    # blueprint registration
    app.register_blueprint(blueprint)
    # admin registration below
    admin = Admin(app, name="IDB", template_mode='bootstrap3')
    admin.add_view(ModelView(TeamMember, DB.session))
    return app

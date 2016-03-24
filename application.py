import os.path as op

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin


from extensions import DB
from blueprints import blueprint
from models import TeamMember


def generate_application(config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    app.jinja_env.add_extension('jinja2.ext.do')
    DB.init_app(app)
    # blueprint registration
    app.register_blueprint(blueprint)
    # admin registration below
    admin = Admin(app, name="IDB", template_mode='bootstrap3')
    path1 = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path1, '/static/', name='Static Files'))
    admin.add_view(ModelView(TeamMember, DB.session))
    return app


if __name__ == "__main__":
    app = generate_application()
    app.run(host='0.0.0.0', port=8888)

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from extensions import DB
from blueprints import blueprint 
from models import TeamMember

app = Flask(__name__)
app.config.from_object('config')
DB = SQLAlchemy(app)
#blueprint registration
app.register_blueprint(blueprint)
#admin registration below
admin = Admin(app, name="IDB", template_mode='bootstrap3')
admin.add_view(ModelView(TeamMember, DB.session))
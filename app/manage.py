from app import app
from extensions import DB
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, DB)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

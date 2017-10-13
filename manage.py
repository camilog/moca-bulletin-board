from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import application, db

migrate = Migrate(application, db)
manager = Manager(application)

from manage_commands import DropTables

manager.add_command('db', MigrateCommand)
manager.add_command('drop', DropTables())

if __name__ == '__main__':
    manager.run()
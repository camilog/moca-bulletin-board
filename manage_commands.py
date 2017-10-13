from flask_script import Command

from app.data.populate_methods import drop_tables


class DropTables(Command):
    def run(self):
        drop_tables()
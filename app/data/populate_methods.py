from app import db


def drop_tables():
    db.drop_all()

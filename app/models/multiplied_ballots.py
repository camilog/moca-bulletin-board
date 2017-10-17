from app import db


class MultipliedBallots(db.Model):
    __tablename__ = 'multiplied_ballots'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __init__(self, value):
        self.value = value
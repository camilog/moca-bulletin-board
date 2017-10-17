from app import db


class Election(db.Model):
    __tablename__ = 'elections'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    number_of_candidates = db.Column(db.Integer)
    candidates = db.relationship("Candidate", backref="election", lazy="dynamic")

    def __init__(self, question, number_of_candidates):
        self.question = question
        self.number_of_candidates = number_of_candidates

from app import db


class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer)
    name = db.Column(db.String)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.id'))

    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name

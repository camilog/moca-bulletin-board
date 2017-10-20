from app import db


class FinalOutcome(db.Model):
    __tablename__ = 'final_outcome'
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.String)
    votes = db.Column(db.Integer)

    def __init__(self, candidate_id, votes):
        self.candidate_id = candidate_id
        self.votes = votes

    @property
    def serialize(self):
        return {
            "id": self.id,
            "candidate_id": self.candidate_id,
            "votes": self.votes
        }
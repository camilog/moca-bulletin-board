from app import db


class Ballot(db.Model):
    __tablename__ = 'ballots'
    id = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.String)
    encrypted_vote = db.Column(db.String)
    signature = db.Column(db.String)

    def __init__(self, voter_id, encrypted_vote, signature):
        self.voter_id = voter_id
        self.encrypted_vote = encrypted_vote
        self.signature = signature

    @property
    def serialize(self):
        return {
            "id": self.id,
            "voter_id": self.voter_id,
            "encrypted_vote": self.encrypted_vote,
            "signature": self.signature
        }
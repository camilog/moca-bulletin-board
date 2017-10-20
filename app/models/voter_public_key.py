from app import db


class VoterPublicKey(db.Model):
    __tablename__ = 'voter_public_keys'
    id = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.String)
    value = db.Column(db.String)

    def __init__(self, voter_id, value):
        self.voter_id = voter_id
        self.value = value

    @property
    def serialize(self):
        return {
            "id": self.id,
            "voter_id": self.voter_id,
            "value": self.value
        }
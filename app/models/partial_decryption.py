from app import db


class PartialDecryption(db.Model):
    __tablename__ = 'partial_decryptions'
    id = db.Column(db.Integer, primary_key=True)
    auth_id = db.Column(db.Integer)
    value = db.Column(db.String)

    def __init__(self, auth_id, value):
        self.auth_id = auth_id
        self.value = value

    @property
    def serialize(self):
        return {
            "id": self.id,
            "auth_id": self.auth_id,
            "value": self.value
        }
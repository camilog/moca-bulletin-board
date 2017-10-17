from app import db


class AuthorityPublicKey(db.Model):
    __tablename__ = 'authority_public_key'
    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.String)
    threshold = db.Column(db.Integer)
    nsplusone = db.Column(db.String)

    def __init__(self, n, threshold, nsplusone):
        self.n = n
        self.threshold = threshold
        self.nsplusone = nsplusone

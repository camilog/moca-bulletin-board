from app import db
from sqlalchemy import BIGINT


class DummyShareKey(db.Model):
    __tablename__ = "dummy_share_key"
    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.BigInteger)
    l = db.Column(db.BigInteger)
    w = db.Column(db.BigInteger)
    v = db.Column(db.BigInteger)
    si = db.Column(db.BigInteger)
    i = db.Column(db.BigInteger)
    vi = db.Column(db.ARRAY(item_type=BIGINT))

    def __init__(self, n, l, w, v, si, i, vi):
        self.n = n
        self.l = l
        self.w = w
        self.v = v
        self. si = si
        self.i = i
        self.vi = vi

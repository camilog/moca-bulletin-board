from app import db
from sqlalchemy import BIGINT


class DummyShareKey(db.Model):
    __tablename__ = "dummy_share_key"
    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.String)
    l = db.Column(db.Integer)
    w = db.Column(db.Integer)
    v = db.Column(db.String)
    si = db.Column(db.String)
    i = db.Column(db.String)
    vi = db.Column(db.ARRAY(item_type=db.String))

    def __init__(self, n, l, w, v, si, i, vi):
        self.n = n
        self.l = l
        self.w = w
        self.v = v
        self. si = si
        self.i = i
        self.vi = vi

    @property
    def serialize(self):
        return {
            "id": self.id,
            "n": self.n,
            "l": self.l,
            "w": self.w,
            "v": self.v,
            "si": self.si,
            "i": self.i,
            "vi": self.vi
        }

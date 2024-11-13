from app import db


class TMercancias(db.Model):
    __tablename__ = 'tmercancia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    mercancias = db.relationship('Mercancias', back_populates='tmercancias')
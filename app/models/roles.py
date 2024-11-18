from app import db


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(100), nullable=False)
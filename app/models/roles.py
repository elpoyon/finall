from app import db


class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(100), nullable=False)
    
    empleados = db.relationship('Empleados', back_populates='roles')
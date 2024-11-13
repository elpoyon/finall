from app import db


class Destinos(db.Model):
    __tablename__ = 'destino'
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(100) , nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    
    
    ordenes = db.relationship('Ordenes' , back_populates='destinos')    
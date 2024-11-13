from app import db

class Clientes(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    
    ordenes = db.relationship('Ordenes' , back_populates='clientes')
    
    #def get_id():
        
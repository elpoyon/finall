from app import db


class Vehiculos(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer , primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(100), nullable=False)
    conductores_id = db.Column(db.Integer, db.ForeignKey('conductor.id'))
    
    conductores = db.relationship('Conductores' , back_populates='vehiculos')
    ordenes = db.relationship('Ordenes' , back_populates='vehiculos')
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'placa': self.placa,
            'conductor': self.conductores_id
        }
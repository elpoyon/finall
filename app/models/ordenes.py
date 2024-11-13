from app import db


class Ordenes(db.Model):
    __tablename__ = 'orden'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Integer, nullable=False)
    fletes = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'))
    conductor_id = db.Column(db.Integer, db.ForeignKey('conductor.id'))
    mercancia_id = db.Column(db.Integer, db.ForeignKey('mercancia.id'))
    origen_id = db.Column(db.Integer, db.ForeignKey('origen.id'))
    destino_id = db.Column(db.Integer, db.ForeignKey('destino.id'))
    
    clientes = db.relationship('Clientes' , back_populates='ordenes')
    vehiculos = db.relationship('Vehiculos' , back_populates='ordenes')
    conductores = db.relationship('Conductores' , back_populates='ordenes')
    mercancias = db.relationship('Mercancias' , back_populates='ordenes')
    origenes = db.relationship('Origenes' , back_populates='ordenes')
    destinos = db.relationship('Destinos' , back_populates='ordenes')
    
    
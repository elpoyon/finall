from app import db


class Origenes(db.Model):
    __tablename__='origen'
    id = db.Column(db.Integer , primary_key=True)
    nombre = db.Column(db.String(110) , nullable=False)
    direccion = db.Column(db.String(100), nullable=False) 
    telefono = db.Column(db.String(100), nullable=False)
    
    
    ordenes = db.relationship('Ordenes' , back_populates='origenes')
    
    
    def to_dict(self):
        return{
            "id":self.id,
            "nombre" : self.nombre,
            "direccion" : self.direccion,
            "telefono" : self.telefono
        }
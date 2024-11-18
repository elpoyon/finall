from app import db


class Mercancias(db.Model):
    __tablename__ = 'mercancia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tmercancias_id = db.Column(db.Integer, db.ForeignKey('tmercancia.id'))
    
    
    tmercancias = db.relationship('TMercancias' , back_populates='mercancias')
    ordenes = db.relationship('Ordenes' , back_populates='mercancias')
    
    
    def to_dict(self):
        return{
            "id":self.id,
            "nombre" : self.nombre,
            "tipo de mercancias" : self.tmercancias_id,
        }
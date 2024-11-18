from app import db



class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable= False)
    salario = db.Column(db.Integer, nullable=False)
    horario = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
from flask_login import UserMixin
import qrcode.constants
from app import db
import json
from PIL import Image
import qrcode
import os
import base64
from flask import current_app
from io import BytesIO


class Conductores(db.Model):
    __tablename__ = 'conductor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(150), nullable=False)
    salud = db.Column(db.File)
    
    
    
    vehiculos = db.relationship('Vehiculos' , back_populates='conductores')
    ordenes = db.relationship('Ordenes' , back_populates='conductores')
    def to_dict(self):
        return{
            "id":self.id,
            "nombre" : self.nombre,
            "direccion" : self.direccion,
            "telefono" : self.telefono,
            "salud": self.salud
        }
    def generate_qr(self):
        from PIL import Image
        user_data = json.dumps({
            'ID' : self.id,
            'Name': self.username
        })
        print("Generando código QR para usuario: ", user_data)
        
        qr = qrcode.QRcode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add.add_data(user_data)
        qr.make(fit=True)
        
        img_qr = qr.make_image(fill='black', back_color='White').convert('RGB')
        
        logo_path = os.path.join(current_app.root_path, 'static', 'logo.ico')
        logo= Image.open(logo_path)
        
        logo_size = 50
        logo = logo.resize((logo_size, logo_size))
        
        pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)
        
        img_qr.paste(logo, pos)
        buffered = BytesIO()
        img_qr.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return img_str    
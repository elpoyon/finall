from flask import Blueprint, render_template, redirect, request, url_for, send_file
from app.models.conductores import Conductores
from app.models.vehiculos import Vehiculos
from app import db
from PIL import Image
import qrcode
import base64
from flask import current_app
from io import BytesIO


bp = Blueprint('conductores' , __name__)

@bp.route('/conductores')
def index():
    data = Conductores.query.all()
    
    return render_template('Conductores/index.html', data = data)

@bp.route('/conductores/add', methods = ['GET' , 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        new_conductores = Conductores(nombre=nombre, direccion=direccion, telefono= telefono)
        db.session.add(new_conductores)
        db.session.commit()
        
        return redirect(url_for('conductores.index'))
    data = Vehiculos.query.all()
    return render_template('Conductores/add.html', data = data)

@bp.route('/conductores/edit<int:id>', methods = ['GET' , 'POST'])
def edit(id):
    conductores = Conductores.query.get_or_404(id)
    
    if request.method =='POST':
        conductores.nombre = request.form['nombre']
        conductores.direccion = request.form['direccion']
        conductores.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('conductores.index'))
    
    return render_template('Conductores/edit.html', conductores=conductores)

@bp.route('/conductores/delete/<int:id>')
def delete(id):
    conductores = Conductores.query.get_or_404(id)
    
    db.session.delete(conductores)
    db.session.commit()
    
    return redirect(url_for('conductores.index'))


@bp.route('/conductores/qr/<int:id>')
def generate_qr(id):
    print("Entrando a la ruta de generación de QR para el usuario con ID:", id)
    user = Conductores.query.get_or_404(id)
    qr_code_base64 = user.generate_qr()
    # Decodificar la imagen del QR desde base64
    qr_code_img = base64.b64decode(qr_code_base64)
    return send_file(BytesIO(qr_code_img), mimetype='image/png')


@bp.route('/conductores/read_qr', methods=['POST'])
def read_qr():
    from pyzbar.pyzbar import decode
    from PIL import Image
    import json

    if 'qr_image' not in request.files:
        return "No se ha proporcionado una imagen de QR", 400

    qr_image = request.files['qr_image']
    img = Image.open(qr_image)
    decoded_objects = decode(img)

    if not decoded_objects:
        return "No se pudo leer el código QR", 400

    qr_data = decoded_objects[0].data.decode('utf-8')
    user_data = json.loads(qr_data)
    user_id = user_data.get('ID')

    if not user_id:
        return "El código QR no contiene un ID de usuario válido", 400

    user = Conductores.query.get(user_id)
    if not user:
        return "Conductor no encontrado", 404

    return render_template('Conductores/index.html', user=user)

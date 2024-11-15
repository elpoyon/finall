from flask import Blueprint, request, jsonify
from app.models.origenes import Origenes
from app import db

bp = Blueprint('OrigenesAsync', __name__)


@bp.route('/OrigenesAsync/index')
def index():
    origins = Origenes.query.all()
    return jsonify([origins.to_dict() for origins in origins])

@bp.route('/OrigenesAsync/add')
def created_origin():
    data = request.json
    new_origin = Origenes(nombre=data['nombre'], direccion=data['direccion'], telefono=data['telefono'])
    db.session.add(new_origin)
    db.session.commit()
    return jsonify({'mesagge':'Origin created successful'}), 201
@bp.route('/OrigenesAsync/update/<int:id>', methods=['PUT'])
def update_origin(id):
    origin = Origenes.query.get_or_404(id)
    if origin:
        data = request.json
        origin.nombre = data['nombre']
        origin.direccion = data['direccion']
        origin.telefono = data['telefono']
        db.session.commit()
        return jsonify({'mesagge': 'Origin update successful'}), 201
    return jsonify({'mesagge':'Origin not found'}), 404
@bp.route('/Origenes/delete/<int:id>', methods =['DELETE'])
def delete(id):
    origin = Origenes.query.get_or_404(id)
    if origin:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'mesagge': 'Origin deleted successful'}), 201
    return jsonify({'mesagge':'Origin not found'}), 404

from flask import Blueprint, redirect, jsonify, request
from app.models.destinos import Destinos
from app import db

bp = Blueprint('DestinosAsync', __name__)

@bp.route('/DestinosAsync/index')
def listar():
    destinos = Destinos.query,all()
    return jsonify([destino.to_dict() for destino in destinos])

@bp.route('/DestinosAsync/create', methods = 'POST')
def create_destination():
    data = request.json
    
    new_destino = Destinos(nombre=data['nombre'], direccion =data['direccion'], telefono=data['telefono'])
    db.session.add(new_destino)
    db.session.commit()
    return jsonify({'message': 'Destino created successful'}),201

@bp.route('/DestinoAsync/update/<int:id>', methods=['PUT'])
def update_destination(id):
    destination = Destinos.query.get_or_404(id)
    if destination:
        data = request.json
        destination.nombre = data['nombre']
        destination.direccion = data['direccion']
        destination.telefono = data['telefono']
        db.session.commit()
        return jsonify({'message':' Destination update successful'}), 201
    return jsonify({'mesagge': 'Destination not found'}), 404

@bp.route('/DestinoAsync/delete/<int:id>', methods = [])
def delete_destination(id):
    destination = Destinos.query.get_or_404(id)
    if destination:
        db.session.delete(id)
        db.session.coommit()
        return jsonify({'message': 'Destination deleted successful'}), 201
    return jsonify({'mesagge': 'Destination not found'}), 404
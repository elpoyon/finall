from flask import Blueprint, request, jsonify
from app.models.vehiculos import Vehiculos
from app import db

bp= Blueprint('VehiculoAsync', __name__)

@bp.route('/VehiculoAsync/index')
def listar():
    vehiculos = Vehiculos.query.all()
    return jsonify([ vehiculo.to_dict() for vehiculo in vehiculos])

@bp.route('/VehiculoAsync/add', methods=['POST'])
def create_vehicle():
    data = request.json 
    new_vehiculo = Vehiculos(marca=data['marca'], placa=data['placa'])
    db.session.add(new_vehiculo)
    db.session.commit()
    return jsonify({'message': 'Vehicle created successful'}),201

@bp.route('/VehiculoAsync/update/<int:id>', methods= ['PUT'])
def update_vehicle(id):
    vehiculo = Vehiculos.query.get(id)
    if vehiculo:
        data = request.json
        vehiculo.marca = data['marca']
        vehiculo.placa = data['placa']
        db.session.commit()
        return jsonify({'message':'Vehicle updated successfull'})
    return jsonify({'message':'Vehicle not found'}), 404
@bp.route('/VehiculoAsync/delete/<int:id>',methods=['DELETE'])
def delete_vehicle(id):
    vehiculo = Vehiculos.query.get(id)
    if vehiculo:
        db.session.delete(id)
        db.session.commit()
        return jsonify ({'message':'Vehicle deleted successfull'})
    return jsonify({'message':'Vehicle not found'}), 404
from flask import Blueprint, request, jsonify
from app.models.conductores import Conductores
from app import db


bp = Blueprint('ConductoresAsync', __name__)

@bp.route('/ConductoresAsync/index')
def listar():
    conductores = Conductores.query.all()
    return jsonify([conductor.to_dict() for conductor in conductores])

@bp.route('/ConductoresAsync/add', methods=['POST'])
def create_driver():
    data = request.json
    new_driver = Conductores(nombre=data['Username'], direccion=data['direccion'], telefono=data['celphone'])
    db.session.add(new_driver)
    db.session.commit()
    return jsonify({'mesagge':'Driver created successful'}),201
@bp.route('/ConductoresAsync/update/<int:id>', methods=['PUT'])
def update_driver(id):
    driver = Conductores.query.get(id)
    if driver:
        data = request.json
        driver.nombre = data['Username']
        driver.direccion = data['pass']
        driver.telefono = data['telefono']
        db.session.commit()
        return jsonify({'message':'Driver updated successful'})
    return jsonify({'message':'Driver not found'}), 404
@bp.route('/ConductoresAsync/delete/<int:id>', methods=['DELETE'])
def delete_driver(id):
    drivers = Conductores.query.get(id)
    if drivers:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'message' : 'Driver deleted successful'})
    return jsonify({'message':'Driver not found'}), 404
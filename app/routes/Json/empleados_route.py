from flask import Blueprint, request, jsonify
from app.models.empleados import Empleados
from app import db


bp = Blueprint('EmpleadosAsync', __name__)

@bp.route('/EmpleadosAsync/index')
def listar():
    employee = Empleados.query.all()
    return jsonify([Empleados.to_dict() for Empleados in employee])

@bp.route('/EmpleadosAsync/add', methods=['POST'])
def create_employee():
    data = request.json
    new_employee = Empleados(nombre=data['Username'], direccion=data['direccion'], telefono=data['celphone'], salario=data['salario'], horario=data['horario'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'mesagge':'Employee created successful'}),201
@bp.route('/EmpleadosAsync/update/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Empleados.query.get(id)
    if employee:
        data = request.json
        employee.nombre = data['Username']
        employee.direccion = data['pass']
        employee.telefono = data['telefono']
        employee.salario=data['salario']
        employee.horario=data['horario']
        db.session.commit()
        return jsonify({'message':'Driver updated successful'})
    return jsonify({'message':'Driver not found'}), 404
@bp.route('/EmpleadosAsync/delete/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Empleados.query.get(id)
    if employee:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'message' : 'Driver deleted successful'})
    return jsonify({'message':'Driver not found'}), 404
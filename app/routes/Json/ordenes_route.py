from flask import request, jsonify, Blueprint
from app.models.ordenes import Ordenes
from app import db


bp= Blueprint('OrdenesAsync', __name__)

@bp.route('/OrdenesAsync/index')
def index():
    order = Ordenes.query.all()
    return jsonify([Ordenes.to_dict() for Ordenes in order])

@bp.route('/Ordenes/add', methods=['POST'])
def create_order():
    data = request.json
    new_order = Ordenes(fecha=data['fecha'], fletes=data['fletes'], cliente_id=data['cliente_id'], vehiculo_id=data['vehiculo_id'],conductor_id=data['conductor_id'], mercancia_id=data['mercancia_id'],origen_id=data['origen_id'],destino_id=data['destino_id'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'mesagge':'Order created successful'}),201

@bp.route('/OrigenesAsync/update/<int:id>')
def update_order(id):
    order = Ordenes.query.get_or_404(id)
    if order:
        data= request.json
        order.fecha=data['fehca']
        order.fletes=data['fletes']
        order.cliente_id = data['cliente_id']
        order.vehiculo_id = data['vehiculo_id']
        order.conductor_id = data['conductor_id']
        order.mercancia_id = data['mercancia_id']
        order.origen_id = data['origen_id']
        order.destino_id = data['destino_id']   
        db.session.commit()
        return jsonify({'mesagge':'Order updated successful'}),201
    return jsonify({'mesagge':'Order not found'}),404

@bp.route('/OrigenesAsync/delete/<int:id>')
def delete(id):
    order = Ordenes.query.get_or_404(id)
    if order:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'mesagge':'Order deleted successful'}),201
    return jsonify({'mesagge':'Order not found'}), 404
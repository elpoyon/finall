from flask import Blueprint, request, jsonify
from app.models.tmercancias import TMercancias
from app import db


bp = Blueprint('TMercanciasAsync', __name__)

@bp.route('/TMercanciasAsync/index')
def index():
    tmercancias = TMercancias.query.all()
    return jsonify([TMercancias.to_dict() for TMercancias in tmercancias])

@bp.route('/TMercanciasAsync/add', methods=['POST'])
def create_tcommodity():
    data = request.json
    new_tcommodity = TMercancias(nombre=data['nombre'])
    db.session.add(new_tcommodity)
    db.session.commit()
    return jsonify({'mesagge':'Type Commodity created successful'}),201
@bp.route('/TMercanciasAsync/update/<int:id>', methods=['PUT'])
def update_tcommodity(id):
    tcommodity = TMercancias.query.get(id)
    if tcommodity:
        data = request.json
        tcommodity.nombre = data['nombre']
        db.session.commit()
        return jsonify({'message':'Type Commodity updated successful'})
    return jsonify({'message':'Type Commodity not found'}), 404
@bp.route('/TMercanciasAsync/delete/<int:id>', methods=['DELETE'])
def delete_tcommodity(id):
    tcommodity = TMercancias.query.get(id)
    if tcommodity:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'message' : 'Type Commodity deleted successful'})
    return jsonify({'message':'Type Commodity not found'}), 404
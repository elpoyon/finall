from flask import Blueprint, request, jsonify
from app.models.mercancias import Mercancias
from app import db


bp = Blueprint('MercanciasAsync', __name__)

@bp.route('/MercanciasAsync/index')
def index():
    commodity = Mercancias.query.all()
    return jsonify({Mercancias.to_dict() for Mercancias in commodity})

@bp.route('/MercanciasAsync/add', methods =['POST'])
def create_commodity():
    data = request.json
    new_commodity = Mercancias(nombre=data['nombre'], tmercancia =data['tmercancias'])
    db.session.add(new_commodity)
    db.session.commit()
    return jsonify({'mesagge' : 'Commodity created successful'}), 201

@bp.route('/MercanciasAsync/update/<int:id>', methods =['PUT'])
def update_commodity(id):
    commodity = Mercancias.query.get_or_404(id)
    if commodity:
        data = request.json
        commodity.nombre = data['nombre']
        commodity.tmercancias = data['tmercancias']
        db.session.commit()
        return jsonify({'mesagge': 'Commodity updated successful'}),201
    return jsonify({'mesagge':'Commodity not found'}), 404
@bp.route('/MercanciasAsync/delete/<int:id>', methods=['DELETE'])
def delete_commodity(id) :
    commodity = Mercancias.query.get_or_404(id)
    if commodity:
        db.session.delete(id)
        db.session.commit()
        return jsonify({'mesagge': 'Commodity deleted successful'}), 201
    return jsonify({'mesagge': 'Commodity not found'}), 404

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
    
from flask import Blueprint, jsonify, request
from app.models.user import Usuario
from app import db

bp = Blueprint('UserAsync', __name__)

@bp.route('/UserAsync/index')
def index():
    users = Usuario.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/UserAsync/add', methods=['POST'])   
def create_user():
    data = request.json
    if 'username' not in data or 'password' not in data:
        return jsonify ({'message':'usernameand password are required'}),400
    new_user = Usuario(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/UserAsync/update/<int:id>', methods=['PUT'])
def update_user(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.json
        usuario.username = data['username']
        usuario.password = data['password']
        db.session.commit()
        return jsonify({'message': 'Usuario updated successfully'})
    return jsonify({'message': 'Usuario not found'}), 404

@bp.route('/UserAsync/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario deleted successfully'})
    return jsonify({'message': 'Usuario not found'}), 404

    
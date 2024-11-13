from flask import Blueprint, render_template, request, redirect, url_for
from app.models.clientes import Clientes
from app import db

bp = Blueprint('clientes' , __name__)

@bp.route('/clientes')
def index():
    data = Clientes.query.all()
    
    return render_template('Clientes/index.html' , data = data)

@bp.route('/clientes/add', methods=[ 'GET' , 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        new_clientes = Clientes(nombre = nombre , direccion=direccion, telefono=telefono)
        db.session.add(new_clientes)
        db.session.commit()
        
        return redirect(url_for('clientes.index'))
    
    return render_template('Clientes/add.html')

@bp.route('/clientes/edit/<int:id>' , methods=['GET' , 'POST'])
def edit(id):
    cliente = Clientes.query.get_or_404(id)
    
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.direccion = request.form['direccion']
        cliente.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('clientes.index'))
    
    return render_template('Clientes/edit.html', cliente=cliente)

@bp.route('/clientes/delete/<int:id>')
def delete(id):
    clientes = Clientes.query.get_or_404(id)
    
    db.session.delete(clientes)
    db.session.commit()
    
    return redirect(url_for('clientes.index'))


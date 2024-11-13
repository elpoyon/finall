from flask import Blueprint, render_template, redirect, request, url_for
from app.models.destinos import Destinos
from app import db

bp = Blueprint('destinos', __name__)

@bp.route('/destinos')
def index():
    data = Destinos.query.all()
    
    return render_template('Destinos/index.html' , data = data)

@bp.route('/destinos/add' , methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
        new_destinos = Destinos(nombre=nombre, direccion=direccion, telefono=telefono)
        db.session.add(new_destinos)
        db.session.commit()
        
        return redirect(url_for('destinos.index'))
    return render_template('Destinos/add.html')

@bp.route('/destinos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    destinos = Destinos.query.get_or_404(id)
    
    if request.method == 'POST':
        destinos.nombre = request.form['nombre']
        destinos.direccion = request.form['direccion']
        destinos.telefono = request.form['telefono']
        db.session.commit()
        
        return redirect(url_for('destinos.index'))
    
    return render_template('Destinos/edit.html' , destinos=destinos)
@bp.route('/destinos/delete/<int:id>')
def delete(id):
    destino = Destinos.query.get_or_404(id)
    
    db.session.delete(destino)
    db.session.commit()
    
    return redirect(url_for('destinos.index'))
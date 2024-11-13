from flask import Blueprint, render_template, redirect, request, url_for
from app.models.origenes import Origenes
from app import db

bp = Blueprint('origenes' , __name__)

@bp.route('/origenes')
def index():
    data = Origenes.query.all()
    
    return render_template ('origenes/index.html', data = data)

@bp.route('/origenes/add' , methods = ['GET' ,'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form ['nombre']
        direccion = request.form ['direccion']
        telefono = request.form['telefono']
        
        new_origenes = Origenes(nombre=nombre , direccion=direccion, telefono=telefono)
        db.session.add(new_origenes)
        db.session.commit()
        
        return redirect(url_for('origenes.index'))
    return render_template('Origenes/add.html')
@bp.route('/origenes/edit/<int:id>', methods = ['GET' ,'POST'])
def edit(id):
    origenes = Origenes.query.get_or_404(id)
    
    if request.method == 'POST':
        origenes.nombre = request.form['nombre']
        origenes.direccion = request.form['direccion']
        origenes.telefono = request.form['telefono']
        
        db.session.commit()
        return redirect(url_for('origenes.index')) 
    return render_template('Origenes/edit.html' , origenes=origenes)

@bp.route('/origenes/delete/<int:id>')
def delete(id):
    origenes = Origenes.query.get_or_404(id)
    
    db.session.delete(origenes)
    db.session.commit()
    
    return redirect(url_for('origenes.index'))
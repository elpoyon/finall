from flask import Blueprint, request, redirect, render_template, url_for
from app.models.vehiculos import Vehiculos
from app.models.conductores import Conductores
from app import db

bp = Blueprint('vehiculos', __name__)

@bp.route('/vehiculos')
def index():
    data = Vehiculos.query.all()
    
    return render_template('/Vehiculos/index.html', data=data)

@bp.route('/vehiculos/add', methods = ['GET' , 'POST'])
def add():
    if request.method == 'POST':
        marca = request.form['marca']
        placa = request.form['placa']
        conductores = int(request.form['conductores'])
        
        new_vehiculo = Vehiculos(marca=marca, placa=placa, conductores_id=conductores)
        db.session.add(new_vehiculo)
        db.session.commit()
    
        return redirect(url_for('vehiculos.index'))
    data= Conductores.query.all()   
    return render_template('Vehiculos/add.html', data=data)

@bp.route('/vehiculos/edit/<int:id>', methods= ['GET', 'POST'])
def edit(id):
    vehiculo = Vehiculos.query.get_or_404(id)
    if request.method == 'POST':
        vehiculo.marca = request.form['marca']
        vehiculo.placa = request.form['placa']
        vehiculo.conductores_id = int(request.form['conductores'])
        
        db.session.commit()
        
        return redirect(url_for('vehiculos.index'))
    data = Conductores.query.all()
    return render_template('Vehiculos/edit.html', vehiculo=vehiculo , data=data)

@bp.route('/vehiculo/delete/<int:id>')
def delete(id):
    vehiculo = Vehiculos.query.get_or_404(id)
    
    db.session.delete(vehiculo)
    db.session.commit()
    
    return redirect(url_for('vehiculos.index'))
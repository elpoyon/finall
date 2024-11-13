from flask import Blueprint, redirect, render_template, url_for, request
from app.models.conductores import Conductores
from app.models.clientes import Clientes
from app.models.destinos import Destinos
from app.models.mercancias import Mercancias 
from app.models.ordenes import Ordenes
from app.models.vehiculos import Vehiculos
from app.models.origenes import Origenes
from app import db

bp = Blueprint('ordenes', __name__)
@bp.route('/ordenes')
def index():
    data = Ordenes.query.all()
    
    return render_template('Ordenes/index.html' , data=data)

@bp.route('/ordenes/add' , methods = ['GET' , 'POST'])
def add():
    if request.method == 'POST':
        fecha= request.form['fecha']
        fletes= request.form['fletes']
        cliente = int(request.form['clientes'])
        vehiculo = int(request.form['vehiculos'])
        mercancia = int(request.form['mercancias'])
        conductor = int(request.form['conductores'])   
        destino = int(request.form['destinos']) 
        origen = int(request.form['origenes'])

        new_ordenes = Ordenes(id=id , fecha=fecha, cliente_id=cliente,vehiculo_id=vehiculo, conductor_id=conductor, mercancia_id=mercancia,  origen_id=origen, destino_id=destino, fletes=fletes)
        db.session.add(new_ordenes)
        db.session.commit()
        
        return redirect(url_for('ordenes.index'))
    data = Clientes.query.all()
    data1 = Conductores.query.all()
    data2 = Destinos.query.all()
    data3 = Mercancias.query.all()
    data5 = Vehiculos.query.all() 
    data6 = Origenes.query.all()
    return render_template('Ordenes/add.html' , data=data, data1=data1, data2=data2 , data3=data3 , data5=data5, data6=data6)

@bp.route('/ordenes/edit/<int:id>' , methods = ['GET' , 'POST'])
def edit(id):
    ordenes = Ordenes.query.get_or_404(id)
    
    if request.method == 'POST':
        ordenes.fecha = request.form['fecha']
        ordenes.fletes = request.form['fletes']
        ordenes.clientes_id = int(request.form['clientes'])
        ordenes.vehiculos_id = int(request.form['vehiculos'])
        ordenes.conductor_id = int(request.form['conductores'])
        ordenes.mercancia_id = int(request.form['mercancias'])
        ordenes.origen_id = int(request.form['origenes'])
        ordenes.destino_id = int(request.form['destinos'])
        db.session.commit()
        return redirect(url_for('ordenes.index'))
    data = Clientes.query.all()
    data1 = Conductores.query.all()
    data2 = Destinos.query.all()
    data3 = Mercancias.query.all()
    datas = Vehiculos.query.all() 
    data6 = Origenes.query.all()
    return render_template('Ordenes/edit.html', ordenes=ordenes, data=data, data1=data1, data2=data2 , data3=data3 , datas=datas, data6=data6 )
@bp.route('/ordenes/delete/<int:id>')
def delete(id):
    ordenes = Ordenes.query.get_or_404(id)
    
    db.session.delete(ordenes)
    db.session.commit()
    
    return redirect(url_for('ordenes.index'))        


        
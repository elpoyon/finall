from flask import Blueprint, render_template, request, redirect, url_for
from app.models.empleados import Empleados
from app.models.roles import Roles
from app import db

bp = Blueprint('empleados' , __name__)

@bp.route('/empleados')
def index():
    data = Empleados.query.all()
    
    return render_template('Empleados/index.html' , data = data)

@bp.route('/empleados/add', methods=[ 'GET' , 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        salario = request.form['salario']
        horario = request.form['horario']
        rol_id = request.form['rol_id']
        
        new_empleado = Empleados(nombre = nombre , direccion=direccion, telefono=telefono, salario=salario, horario=horario, rol_id = rol_id)
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('empleados.index'))
    data = Roles.query.all()
    return render_template('Empleados/add.html', data=data)

@bp.route('/empleados/edit/<int:id>' , methods=['GET' , 'POST'])
def edit(id):
    empleado = Empleados.query.get_or_404(id)
    
    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.direccion = request.form['direccion']
        empleado.telefono = request.form['telefono']
        empleado.salario = request.form['salario']
        empleado.horario = request.form['horario']
        empleado.rol_id = request.form['rol_id']
        db.session.commit()
        return redirect(url_for('empleados.index'))
    data = Roles.query.all()
    return render_template('Empleados/edit.html', empleado = empleado, data=data)

@bp.route('/empleados/delete/<int:id>')
def delete(id):
    Empleados = Empleados.query.get_or_404(id)
    
    db.session.delete(Empleados)
    db.session.commit()
    
    return redirect(url_for('empleados.index'))


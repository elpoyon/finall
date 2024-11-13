from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.mercancias import Mercancias
from app.models.tmercancias import TMercancias
from app import db

bp = Blueprint('mercancias', __name__)

@bp.route('/mercancias')
def index():
    data = Mercancias.query.all()
    
    return render_template('Mercancias/index.html', data=data)
@bp.route('/mercancias/add', methods = ['GET' , 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tmercancias = int(request.form['tmercancias'])
        
        new_mercancias = Mercancias(nombre=nombre , tmercancias_id=tmercancias)
        db.session.add(new_mercancias)
        db.session.commit()
        
        return redirect(url_for('mercancias.index'))
    data = TMercancias.query.all()
    return render_template('Mercancias/add.html', data=data)

@bp.route('/mercancias/edit/<int:id>', methods =['GET' , 'POST'])
def edit(id):
    mercancias = Mercancias.query.get_or_404(id)
    if request.method == 'POST':
        mercancias.nombre = request.form['nombre']
        mercancias.tmercancias= int(request.form['tmercancias'])
        db.session.commit()
        
        return redirect(url_for('mercancias.index'))
    data = TMercancias.query.all()
    return render_template('Mercancias/edit.html' , mercancias = mercancias , data = data)
@bp.route('/mercancias/delete/<int:id>')
def delete(id):
    mercancias = Mercancias.query.get_or_404(id)
    
    db.session.delete(mercancias)
    db.session.commit()
    
    return redirect(url_for('mercancias.index'))
    
    
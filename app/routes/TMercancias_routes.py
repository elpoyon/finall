from flask import Blueprint, redirect, render_template, request, url_for
from app.models.tmercancias import TMercancias
from app import db

bp = Blueprint('tmercancias', __name__)

@bp.route('/tmercancias')
def index():
    data = TMercancias.query.all()
    
    return render_template('TMercancias/index.html' , data = data )

@bp.route('/tmercancias/add', methods =['GET' , 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        
        new_tmercancias = TMercancias(nombre=nombre)
        db.session.add(new_tmercancias)
        db.session.commit()
        
        return redirect(url_for('tmercancias.index'))
    return render_template('TMercancias/add.html')

@bp.route('/tmercancias/edit/<int:id>' , methods = ['GET' , 'POST'])
def edit(id):
    
    tmercancias = TMercancias.query.get_or_404(id)
    if request.method == 'POST':
        TMercancias.nombre = request.form['nombre']
        
        db.session.commit()
        
        return redirect(url_for('tmercancias.index'))
    return render_template('TMercancias/edit.html' , tmercancias=tmercancias)
@bp.route('/tmercancias/delete/<int:id>')
def delete(id):
    tmercancias = TMercancias.query.get_or_404(id)
    
    db.session.delete(tmercancias)
    db.session.commit()
    
    return redirect(url_for('tmercancias.index'))
    
from flask import Blueprint, render_template

bp = Blueprint('Indice1',__name__)

@bp.route('/')
def index():
    
    return render_template('Indice/Index5.html')
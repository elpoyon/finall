from flask import Blueprint, render_template

bp = Blueprint('Indice',__name__)

@bp.route('/indice')
def index():
    
    return render_template('Indice/index.html')
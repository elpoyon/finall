from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash
from app.models.user import Usuario
from app import db


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['GET', 'POST'])
def login():
    print("Ingresa al login")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Ingresa al if {username}")
        
        user = Usuario.query.filter_by(username=username,password=password).first()
        
        if user:
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('Indice1.index'))  
        
        flash('Invalid credentials. Please try again.', 'danger')
        
    if current_user.is_authenticated:
        return redirect(url_for('Indice1.index')) 
    
    return render_template('login/login.html')
    
@auth_bp.route('/add', methods= ['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        new_user = Usuario(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    return render_template('login/add.html')
@auth_bp.route('/dashboard')    
@login_required
def dashboard():
    return f'Welcome, {current_user.username}! This is your dashboard.'

@auth_bp.route('/logout')
@login_required
def logout(): 
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login')) 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager= LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view ='auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        from.models.user import Usuario
        return Usuario.query.get(int(user_id))
    
    from app.routes import clientes_routes , conductores_routes, destinos_routes, origenes_routes, mercancias_routes, TMercancias_routes, vehiculos_routes, ordenes_routes, index_routes, index1_routes, auth_routes, empleados_routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(clientes_routes.bp)
    app.register_blueprint(conductores_routes.bp)
    app.register_blueprint(destinos_routes.bp)
    app.register_blueprint(origenes_routes.bp)
    app.register_blueprint(mercancias_routes.bp)
    app.register_blueprint(TMercancias_routes.bp)
    app.register_blueprint(vehiculos_routes.bp)
    app.register_blueprint(ordenes_routes.bp)
    app.register_blueprint(index_routes.bp)
    app.register_blueprint(index1_routes.bp)
    app.register_blueprint(empleados_routes.bp)
    
    from app.routes.Json import users_route, vehiculos_route, conductores_route, destinos_route, origenes_route,mercancias_route, tmercancias_route, ordenes_route, empleados_route
    app.register_blueprint(users_route.bp)
    app.register_blueprint(vehiculos_route.bp)
    app.register_blueprint(conductores_route.bp)
    app.register_blueprint(destinos_route.bp)
    app.register_blueprint(origenes_route.bp)
    app.register_blueprint(ordenes_route.bp)
    app.register_blueprint(mercancias_route.bp)
    app.register_blueprint(tmercancias_route.bp)
    app.register_blueprint(empleados_route.bp)
    return app
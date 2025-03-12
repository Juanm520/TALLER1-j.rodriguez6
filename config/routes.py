from controllers.index_controller import index_blueprint
from controllers.login_controller import login_blueprint, auth_blueprint

def register_routes(app):
    app.register_blueprint(index_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(auth_blueprint)
    
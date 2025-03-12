import os
from flask import Flask
from flask_login import LoginManager
from config.routes import register_routes
from models.user import User, users

app = Flask(__name__, template_folder='views')
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager(app)
register_routes(app)

@login_manager.user_loader
def load_user(user):
    return users.get(user)

if __name__ == '__main__':
    app.run(debug = True)

#test con:
 #antonitor Tonito123 user_dashboard
 #mengano_cruz C284y9)Pgb3P admin_dashboard

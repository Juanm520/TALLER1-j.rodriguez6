from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__, url_prefix = '/')

@index_blueprint.route('/')
def index_controller():
    return render_template('index.html')
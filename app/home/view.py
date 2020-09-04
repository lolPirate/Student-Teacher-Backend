from flask import Blueprint

view = Blueprint('home', __name__)


@view.route('/home', methods=['GET'])
@view.route('/', methods=['GET'])
def index():
    return "App Running"

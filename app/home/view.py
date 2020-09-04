from flask import Blueprint
from app.middleware.middleware import api_key_required

view = Blueprint('home', __name__)


@view.route('/home', methods=['GET'])
@view.route('/', methods=['GET'])
@api_key_required
def index():
    return "App Running"

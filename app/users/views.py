from flask import Blueprint, request, jsonify, current_app
from app.middleware.middleware import api_key_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import db, Person
import uuid
import jwt
import datetime
from flask_cors import CORS

view = Blueprint('users', __name__)

CORS(view, supports_credentials=True)


@view.route('/api/user', methods=['POST'])
@api_key_required
def create_user():
    data = request.get_json()
    """first_name = request.form.get('first_name', "") 
    middle_name = request.form.get('middle_name', "")
    last_name = request.form.get('last_name', "")
    email_primary = request.form.get('email_primary', "")
    phone_primary = request.form.get('phone_primary', "")
    password = generate_password_hash(request.form.get('password', ""))"""

    first_name = data['first_name'] if data['first_name'] else ""
    middle_name = data['middle_name'] if data['middle_name'] else ""
    last_name = data['last_name'] if data['last_name'] else ""
    email_primary = data['email_primary'] if data['email_primary'] else ""
    phone_primary = data['phone_primary'] if data['phone_primary'] else ""
    password = generate_password_hash(data['password']) if data["password"] else ""
    public_id = str(uuid.uuid4())

    if Person.query.filter_by(email_primary=email_primary).first() is not None:
        return jsonify({
            "error": "Invalid primary email",
            "code": "IPE"
        }), 406
    if Person.query.filter_by(phone_primary=phone_primary).first() is not None:
        return jsonify({
            "error": "Invalid primary phone number",
            "code": "IPPN"
        }), 406
    user = Person(
        public_id=public_id,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        email_primary=email_primary,
        phone_primary=phone_primary,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "info": "New user created",
        "code": "SUCCESS"
    }), 201


@view.route('/api/user/login', methods=['POST'])
@api_key_required
def authenticate_user():
    email_primary = request.form.get('email_primary', "")
    password = request.form.get('password', "")
    user = Person.query.filter_by(email_primary=email_primary).first()
    stored_password = user.password
    if check_password_hash(stored_password, password):
        auth_token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }, current_app.config['SECRET_KEY'])
        return jsonify({
            "auth": auth_token.decode('UTF-8')
        }), 200
    else:
        return jsonify({
            "auth": "Unable to authorize"
        }), 401


@view.route('/api/user/view-all', methods=['GET'])
@api_key_required
def view_all_users():
    users = Person.query.all()
    output = list(map(lambda user: {
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "email_primary": user.email_primary,
        "phone_primary": user.phone_primary,
        "password": user.password,
        "public_id": user.public_id
    }, users))
    return jsonify({
        "Current-Users": output
    })

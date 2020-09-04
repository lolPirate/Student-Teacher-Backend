from flask import Blueprint, request, jsonify
from app.middleware.middleware import api_key_required
from werkzeug.security import generate_password_hash
from app.models.models import db, Person
import uuid

view = Blueprint('users', __name__)


@view.route('/api/user', methods=['POST'])
@api_key_required
def create_user():
    data = request.get_json()
    first_name = data['first_name'] if data['first_name'] else ""
    middle_name = data['middle_name'] if data['middle_name'] else ""
    last_name = data['last_name'] if data['last_name'] else ""
    email_primary = data['email_primary'] if data['email_primary'] else ""
    phone_primary = data['phone_primary'] if data['phone_primary'] else ""
    password = generate_password_hash(data['password']) if data['password'] else ""
    public_id = str(uuid.uuid4())
    if Person.query.filter_by(email_primary=email_primary).first() is not None:
        return jsonify({
            "error": "Invalid primary email",
            "code": "IPE"
        })
    if Person.query.filter_by(phone_primary=phone_primary).first() is not None:
        return jsonify({
            "error": "Invalid primary phone number",
            "code": "IPPN"
        })
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
    })


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

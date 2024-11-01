from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.user import User
from app import db, bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(
        username=data['username'],
        password=bcrypt.generate_password_hash(data['password']).decode('utf-8'),
    )

    if User.query.filter_by(username=user.username).first():
        return jsonify({"msg": "Username already exists"}), 400

    db.session.add(user)
    db.session.commit()
    return {'message': 'User created successfully'}


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = db.session.query(User).filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid username or password"}), 401
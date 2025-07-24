from flask import Blueprint, request, jsonify
from models import user_model
from utils.validators import validate_user_input
from utils.security import hash_password, verify_password

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_model.get_all_users()
    return jsonify(users), 200

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    valid, error = validate_user_input(data, ['name', 'email', 'password'])
    if not valid:
        return jsonify({"error": error}), 400
    password_hash = hash_password(data['password'])
    user_model.create_user(data['name'], data['email'], password_hash)
    return jsonify({"message": "User created"}), 201

@user_bp.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    valid, error = validate_user_input(data, ['name', 'email'])
    if not valid:
        return jsonify({"error": error}), 400
    user_model.update_user(user_id, data['name'], data['email'])
    return jsonify({"message": "User updated"}), 200

@user_bp.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_model.delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"}), 200

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    users = user_model.search_users_by_name(name)
    return jsonify(users), 200

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    valid, error = validate_user_input(data, ['email', 'password'])
    if not valid:
        return jsonify({"error": error}), 400

    user = user_model.login_user(data['email'], data['password'])
    if user and verify_password(data['password'], user['password']):
        return jsonify({"status": "success", "user_id": user['id']}), 200
    return jsonify({"status": "failed"}), 401

from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    user_name = data.get('user_name')
    pwd = data.get('pwd')
    
    if not user_name or not pwd:
        return jsonify({"message": "Username and password are required"}), 400  # Bad Request
    
    response, status_code = user_service.register_user(user_name, pwd)
    return jsonify(response), status_code

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    user_name = data.get('user_name')
    pwd = data.get('pwd')
    
    if not user_name or not pwd:
        return jsonify({"message": "Username and password are required"}), 400  # Bad Request
    
    response, status_code = user_service.login_user(user_name, pwd)
    return jsonify(response), status_code

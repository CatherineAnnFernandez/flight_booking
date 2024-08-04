from models.user_model import UserModel
import hashlib

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, user_name, pwd):
        # Hash the password for security
        hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
        
        # Check if the user already exists
        user = self.user_model.get_user_by_username(user_name)
        if user:
            return {"message": "User already exists"}, 409  # Conflict
        
        # Create the new user
        self.user_model.create_user(user_name, hashed_pwd)
        return {"message": "User registered successfully"}, 201  # Created

    def login_user(self, user_name, pwd):
        hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
        
        # Retrieve the user from the database
        user = self.user_model.get_user_by_username(user_name)
        if user and user[2] == hashed_pwd:  # Assuming pwd is the third column
            return {"message": "Login successful"}, 200  # OK
        
        return {"message": "Invalid username or password"}, 401  # Unauthorized

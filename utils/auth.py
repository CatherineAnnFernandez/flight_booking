from werkzeug.security import generate_password_hash, check_password_hash

def generate_hash(password):
    return generate_password_hash(password)

def verify_hash(password, hashed):
    return check_password_hash(hashed, password)


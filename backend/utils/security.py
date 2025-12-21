import bcrypt 

def password_hash(password: str) -> str:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    bytes_password = password.encode('utf-8')
    bytes_hash = hashed.encode('utf-8')

    return bcrypt.checkpw(bytes_password, bytes_hash)
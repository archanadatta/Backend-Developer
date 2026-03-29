from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import hashlib

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str):
    # Step 1: Pre-hash using SHA256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    # Step 2: Then bcrypt
    print(hashed)
    return pwd_context.hash(hashed)

def verify_password(plain, hashed):
    hashed_plain = hashlib.sha256(plain.encode()).hexdigest()
    return pwd_context.verify(hashed_plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
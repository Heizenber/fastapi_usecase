from jose import JWTError, jwt
from datetime import datetime, timedelta



SECRET_KEY = "hafiuefh982hofi239f02y930hgerghed8g92g83794034t934jtjgerhdh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded



from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from Base.models import User
from Base.database import SessionLocal

rour = APIRouter(
    prefix='/api/book',
    tags=['Authentication']
)
security = HTTPBearer()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
SECRET_KEY = 'voodoo'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@rour.post('/Authentication/register')
def Authentication_register(username: str, email: str, password: str):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='This user already exists in the database!')
    else:
        new_user = User(username=username, email=email, password=pwd_context.hash(password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {'detail': 'Welcome!'}

@rour.post('/Authentication/login')
def Authentication_login(email: str, password: str):
    db = SessionLocal()
    login_user = db.query(User).filter(User.email == email).first()
    if not login_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid username or password')
    if not pwd_context.verify(password, login_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid username or password')
    else:
        access_token = create_access_token(login_user.email)
        return {'token': access_token, 'token_type': 'bearer'}

def create_access_token(email: str):
    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {'email': email, 'exp': expire_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload['email']
        user = db.query(user).filter(user.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid token')
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid token')

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = verify_access_token(token)
    return user

@rour.get('/protected')
def protected_route(user: User = Depends(get_current_user)):
    return {'message': 'This endpoint is protected'}
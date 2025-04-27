from fastapi import FastAPI, HTTPException, Depends
from models import User, UserLogin
from auth import get_password_hash, verify_password, create_access_token
from auth import get_current_user

app = FastAPI()

# Base de datos simulada
fake_db = {}

@app.post("/register/")
def register(user: User):
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_password = get_password_hash(user.password)
    fake_db[user.username] = hashed_password
    return {"message": "Usuario registrado correctamente"}

@app.post("/login/")
def login(user: UserLogin):
    stored_password = fake_db.get(user.username)
    if not stored_password:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    
    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected/")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hola {current_user}, accediste a una ruta protegida!"}

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}
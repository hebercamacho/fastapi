from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nome: str 
    senha: str

usuarios = [
    Usuario(id = 1, nome = "Heber", senha = "heber123"),
    Usuario(id=2, nome="Gabriela", senha="gabi123")
]

app = FastAPI()

@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

@app.get("/usuarios")
def getAllUsers():
    return usuarios

@app.get("/usuarios/{id}")
def getUserById(id: int):
    return usuarios[id+1]

@app.post("/usuarios")
def insertUser(user: Usuario):
    usuarios.append(user)
    return bool(1)
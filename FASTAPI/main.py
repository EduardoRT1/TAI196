from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares import BearerJWT

from DB.conexion import Session, engine, Base
from models.modelsDB import User


app = FastAPI(
    title="Mi primera API-196",
    description="Eduardo Rojas Trejo",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

usuarios = [
    {"id": 1, "nombre": "Eduardo", "edad": 21, "correo": "lalojr@example.com"},
    {"id": 2, "nombre": "Chucho", "edad": 22, "correo": "cucho@gmail.com"},
    {"id": 3, "nombre": "Estrella", "edad": 23, "correo": "estre@abcd.com"},
    {"id": 4, "nombre": "Lucero", "edad": 24, "correo": "lu@xd.com"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}


#dependencies=[Depends(BearerJWT())],
#endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible", "Excepción": str(x)})       
    finally:
        db.close()
        
#endpoint consulta por id
@app.get("/usuarios/{id}", tags=["Operaciones CRUD"])
def ConsultarUno(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible", "Excepción": str(x)})
    finally:
        db.close()
        
#Endpoint para agregar usuarios
@app.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarioNuevo: modelUsuario):
    db = Session()
    try:
        db.add(User(**usuarioNuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje": "Usuario guardado", "usuario": usuarioNuevo.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=201, content={"mensaje": "No se guardó", "Excepción": str(e)})
    
    finally:
        db.close()

""" #endpoint para actualizar un usuario por su id
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#endpoint para eliminar un usuario por su id
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"Usuario eliminado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado") """


#Endpoint para generar un token de autentificacion
@app.post('/auth', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == "lu@xd.com" and autorizado.passw == "12345678":
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso":"Usuario o contraseña incorrectos"}


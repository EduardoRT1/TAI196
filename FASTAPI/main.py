from fastapi import FastAPI, HTTPException
from typing import List, Optional
from modelsPydantic import modelUsuario


app = FastAPI(
    title="Mi primera API-196",
    description="Eduardo Rojas Trejo",
    version="1.0.1"
)


usuarios = [
    {"id": 1, "nombre": "Eduardo", "edad": 21, "correo": "lalojr@example.com"},
    {"id": 2, "nombre": "Chucho", "edad": 22, "correo": "cucho@gmail.com"},
    {"id": 3, "nombre": "Estrella", "edad": 23, "correo": "estre@abcd.com"},
    {"id": 4, "nombre": "Lucero", "edad": 24, "correo": "lu@xd.com"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}

#endpoint para consultar todos los usuarios
@app.get("/usuarios", response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def ConsultarTodos():
    return usuarios

#endpoint para agregar un usuario por su id
@app.post("/usuarios/", response_model=modelUsuario,tags=["Operaciones CRUD"])
def AgregarUsuario(usuario: modelUsuario):  
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario)  
    return usuario

#endpoint para actualizar un usuario por su id
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
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


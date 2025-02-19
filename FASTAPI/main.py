from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(
    title="Mi primera API-196",
    description="Eduardo Rojas Trejo",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "Eduardo", "edad": 21},
    {"id": 2, "nombre": "Chucho", "edad": 22},
    {"id": 3, "nombre": "Estrella", "edad": 23},
    {"id": 4, "nombre": "Lucero", "edad": 24},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}

#endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todos los usuarios registrados": usuarios}

#endpoint para agregar
# un usuario por su id
@app.post("/usuarios/", tags=["Operaciones CRUD"])
def AgregarUsuario(usuario: dict):  
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario)  
    return usuario
#endpoint para actualizar un usuario por su id
@app.put("/usuarios/{id}", tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, usuario: dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario)
            return {"Usuario actualizado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuarios.append(usuario)
    return usuario
#endpoint para eliminar un usuario por su id
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"Usuario eliminado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

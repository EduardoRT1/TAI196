from fastapi import FastAPI, HTTPException
from typing import List
from typing import Optional

app = FastAPI(
    title="Administrador de tareas",
    description="Eduardo Rojas Trejo",
    version="1.0.1"
)

#Lista de tareas
tareas = [
    {"id": 1, "tarea": "Estudiar", "descripcion": "Estudiar para el examen", "vencimiento": "2021-10-10", "estado": "Pendiente"},
    {"id": 2, "tarea": "Hacer ejercicio", "descripcion": "Hacer ejercicio por 30 minutos", "vencimiento": "2021-10-10", "estado": "Pendiente"},
    {"id": 3, "tarea": "Comprar comida", "descripcion": "Comprar comida para la semana", "vencimiento": "2021-10-10", "estado": "Pendiente"}
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}

#endpoint para consultar todas las tareas
@app.get("/tareas", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todas las tareas registradas": tareas}

#endpoint para agregar tarea
@app.post("/tareas/", tags=["Operaciones CRUD"])
def AgregarTarea(tarea: dict):  
    for tar in tareas:
        if tar["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    
    tareas.append(tarea)  
    return tarea

#endpoint para encontrar una tarea en especifico por su id
@app.get("/tareas/{id}", tags=["Operaciones CRUD"])
def ConsultarTarea(id: int):
    for tar in tareas:
        if tar["id"] == id:
            return {"Tarea encontrada": tar}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#endpoint para actualizar una tarea
@app.put("/tareas/{id}", tags=["Operaciones CRUD"])
def ActualizarTarea(id: int, tarea: dict):
    for tar in tareas:
        if tar["id"] == id:
            tar.update(tarea)
            return {"Tarea actualizada": tar}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#endpoint para eliminar una tarea
@app.delete("/tareas/{id}", tags=["Operaciones CRUD"])
def EliminarTarea(id: int):
    for tar in tareas:
        if tar["id"] == id:
            tareas.remove(tar)
            return {"Tarea eliminada": tar}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


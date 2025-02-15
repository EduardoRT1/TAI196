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


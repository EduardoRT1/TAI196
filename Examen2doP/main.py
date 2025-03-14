from fastapi import FastAPI, HTTPException
from typing import List
from typing import List, Optional
from pydantic import BaseModel 
from pydantic import BaseModel, Field

#from modelsPydantic import ModelEnvio


app = FastAPI(
    title = "API DE ENVIOS",
    version = "1.1"
)
 
class ModelEnvio(BaseModel):
    Codigo_postal: str = Field(..., min_length=5, max_length=5, description="Código postal")
    Destino: str = Field(..., min_length=6, max_length=50, description="Destino")
    Peso: int = Field(..., gt=0, lt=500, description="Peso del envío")
#Lista de envios   
envios = [
    {"Codigo_postal": "76709", "Destino": "Pedro Escobodrio", "Peso": 20},
    {"Codigo_postal": "76708", "Destino": "El muerto", "Peso": 30},
    {"Codigo_postal": "76707", "Destino": "El ahorcado", "Peso": 40}
]

#inicio
@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}

#consultar todos los envios
@app.get("/envios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todos los envios": envios}

#conusltar envio por su codigo postal y validacion de pydantic
@app.get("/envios/{codigo_postal}", tags=["Operaciones CRUD"])
def ConsultarEnvio(codigo_postal: str):
    for env in envios:
        if env["Codigo_postal"] == codigo_postal:
            return {"Envio encontrado": env}
    raise HTTPException(status_code=404, detail="Envio no encontrado")

#actualizar un envio a traves de su codigo postal y pydantic
@app.put("/envios/{codigo_postal}", tags=["Operaciones CRUD"])
def ActualizarEnvio(codigo_postal: str, envio: ModelEnvio):
    for env in envios:
        if env["Codigo_postal"] == codigo_postal:
            env.update(envio)
            return {"Envio actualizado": env}
    raise HTTPException(status_code=404, detail="Envio no encontrado")
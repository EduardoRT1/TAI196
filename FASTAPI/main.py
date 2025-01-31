from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title='Mi primer API 196', 
    description='Eduardo Rojas Trejo',
    version= '1.0.1'
)

usuarios=[
    {"id":1, "nombre":"ivan", "edad": 37},
    {"id":2, "nombre":"gerardo", "edad": 18},
    {"id":3, "nombre":"estrella", "edad": 19},
    {"id":4, "nombre":"lucero", "edad": 20},
]

@app.get('/', tags=['Inicio'])
def main():
    return {'Hola FastAPI':'Eduardo'}

@app.get('/promedio', tags=['Promedio'])
def promedio():
    return 213212.212

@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultaUsuario(id: int):
    #conectamos a bdd
    #hacemos conosulta y retornamos resultset
    return{"Se encontró el usuario"}

#endpoint parametro opcional
@app.get('/usuariox/', tags=['Parametro Opcional'])
def consultaUsuario2(id :Optional[int]= None):
    if id is not None:
        for usuario in usuarios:
            if usuario['id'] == id:
                return {"mensaje":"Usuario encontrado","usuario":usuario}
        return {"mensaje":f"No se encontró el usuario {id}"}
    else: 
        return{"mensaje": "No se proporcionó un id"}

#endpoint con varios parametro opcionales
@app.get("/usuarioss/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
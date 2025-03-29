from modelsPydantic import modelAuth
from tokenGen import createToken
from fastapi.responses import JSONResponse
from fastapi import APIRouter

routerAuth = APIRouter()
    
#Endpoint para generar un token de autentificacion
@routerAuth.post('/auth', tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == "lu@xd.com" and autorizado.passw == "12345678":
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso":"Usuario o contraseña incorrectos"}
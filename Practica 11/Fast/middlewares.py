from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from tokenGen import validateToken

# Middleware para validar el token de autentificacion
class BearerJWT(HTTPBearer):
    async def __call__(self, request:Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if not isinstance(data, dict):
            raise HTTPException(status_code=401, detail="Formato de token no valido")
        
        if data.get('correo')!= 'lu@xd.com':
            raise HTTPException(status_code=403, detail="Credenciales no validas")
        
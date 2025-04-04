import jwt # PyJWT
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='gorgojo', algorithm='HS256')
    return token

#
def validateToken(token:str): 
    try:
        data:dict = jwt.decode(token, key='gorgojo', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token Expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")
    
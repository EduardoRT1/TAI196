import jwt # PyJWT

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos, key='gorgojo', algorithm='HS256')
    return token



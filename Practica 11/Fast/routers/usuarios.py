from fastapi import HTTPException, Depends
from modelsPydantic import modelUsuario
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

#endpoint para consultar todos los usuarios
@routerUsuario.get("/usuarios", tags=["Operaciones CRUD"]) #dependencies=[Depends(BearerJWT())],
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible", "Excepción": str(x)})       
    finally:
        db.close()
        
#endpoint consulta por id
@routerUsuario.get("/usuarios/{id}", tags=["Operaciones CRUD"])
def ConsultarUno(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible", "Excepción": str(x)})
    finally:
        db.close()
        
#Endpoint para agregar usuarios
@routerUsuario.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarioNuevo: modelUsuario):
    db = Session()
    try:
        db.add(User(**usuarioNuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje": "Usuario guardado", "usuario": usuarioNuevo.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=201, content={"mensaje": "No se guardó", "Excepción": str(e)})
    
    finally:
        db.close()
        
from fastapi.responses import JSONResponse

#Endpoint para actualizar usuarios
@routerUsuario.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, usuarioActualizado: modelUsuario):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        for key, value in usuarioActualizado.model_dump().items():
            setattr(consulta, key, value) 
        
        db.commit()
        
        return JSONResponse(status_code=200, content={"mensaje": "Usuario actualizado", "usuario": usuarioActualizado.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al actualizar usuario", "excepción": str(e)})
    
    finally:
        db.close()

#Endpoint para eliminar usuarios
@routerUsuario.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def EliminarUsuario(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        usuario_eliminado = jsonable_encoder(consulta)  # Convertimos el objeto a JSON válido
        
        db.delete(consulta)
        db.commit()
        
        return JSONResponse(status_code=200, content={"mensaje": "Usuario eliminado", "usuario": usuario_eliminado})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al eliminar usuario", "excepción": str(e)})
    
    finally:
        db.close()
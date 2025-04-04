from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Usuario FastAPI",
    description="API para gestionar usuarios, ERT 196",
    version="1.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
    
)












Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)
app.include_router(routerAuth)

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Eduardo Rojas Trejo"}
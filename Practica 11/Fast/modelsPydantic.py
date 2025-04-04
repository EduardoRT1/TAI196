from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    name: str = Field(..., min_length=3, max_length=15, description="Nombre, solo letras y espacios")
    age: int = Field(..., gt=0, lt=150, description="Edad, solo números positivos")
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", description="Correo electrónico", example="lalo@gmail.com")

class modelAuth(BaseModel):
    correo: str  
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña mínimo 8 caracteres")

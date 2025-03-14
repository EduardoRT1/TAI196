from pydantic import BaseModel, Field

class ModelEnvio(BaseModel):
    codigo_postal: str = Field(..., min_length=5, max_length=5, description="Código postal")
    destino: str = Field(..., min_length=6, max_length=50, description="Destino")
    peso: int = Field(..., gt=0, ge=500, description="Peso del envío")
    
    
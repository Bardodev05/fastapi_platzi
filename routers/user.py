# Importa APIRouter de fastapi para definir rutas de API.
from fastapi import APIRouter

# Importa BaseModel de pydantic para definir modelos de datos.
from pydantic import BaseModel

# Importa create_token de un módulo de utilidades personalizado para crear tokens JWT.
from utils.jwt_manager import create_token

# Importa JSONResponse de fastapi.responses para enviar respuestas JSON personalizadas.
from fastapi.responses import JSONResponse

# Importa el esquema de usuario de un módulo de esquemas personalizado.
from schemas.user import User


user_router = APIRouter()

# Define un modelo de datos para los usuarios usando Pydantic.
class User(BaseModel):
    email: str
    password: str

# Ruta POST para iniciar sesión.
@user_router.post('/login', tags=['auth'])
def login(user: User):
    # Verifica si el correo electrónico y la contraseña coinciden con los valores esperados.
    if user.email == "admin@gmail.com" and user.password == "admin":
        # Genera un token JWT para el usuario.
        token: str = create_token(user.dict())
        # Retorna el token como una respuesta JSON.
        return JSONResponse(status_code=200, content=token)

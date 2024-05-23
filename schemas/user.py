from pydantic import BaseModel

class User(BaseModel):
    email: str  # Campo para almacenar el correo electrónico del usuario. Espera un string.
    password: str  # Campo para almacenar la contraseña del usuario. Espera un string.

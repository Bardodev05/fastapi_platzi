# Importa HTTPBearer de fastapi.security para crear un middleware de autenticación basado en tokens JWT.
from fastapi.security import HTTPBearer

# Importa Request y HTTPException de fastapi para trabajar con solicitudes HTTP y lanzar excepciones HTTP específicas.
from fastapi import Request, HTTPException

# Importa las funciones create_token y validate_token desde un módulo de utilidades personalizado llamado jwt_manager.
# Estas funciones se utilizan para crear y validar tokens JWT.
from utils.jwt_manager import create_token, validate_token


class JWTBearer(HTTPBearer):
    # La función __call__ es sobrescrita para agregar lógica adicional durante el proceso de autenticación.
    async def __call__(self, request: Request):
        # Llama al método __call__ de la superclase para obtener los datos de autenticación de la solicitud.
        auth = await super().__call__(request)
        
        # Valida el token JWT utilizando la función validate_token, pasando los credenciales obtenidas.
        data = validate_token(auth.credentials)
        
        # Comprueba si el correo electrónico asociado al token es "admin@gmail.com".
        # Si no coincide, se lanza una excepción HTTP con código de estado 403 (Forbidden) y un mensaje indicando que las credenciales son inválidas.
        if data['email']!= "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")

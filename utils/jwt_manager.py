# Importa las funciones encode y decode de la biblioteca jwt para trabajar con tokens JWT
from jwt import encode, decode

# Función para crear un nuevo token JWT
def create_token(data: dict) -> str:
    # Utiliza la función encode para generar un token JWT a partir de los datos proporcionados
    # Los parámetros son: payload (datos a incluir en el token), clave secreta utilizada para firmar el token,
    # y el algoritmo de firma ('HS256' indica HMAC SHA-256).
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    # Retorna el token generado
    return token

# Función para validar un token JWT
def validate_token(token: str) -> dict:
    # Utiliza la función decode para verificar y decodificar el token JWT
    # Los parámetros son: el token a validar, la clave secreta utilizada para verificar la firma del token,
    # y los algoritmos permitidos para la firma ('HS256').
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    # Retorna los datos contenidos en el token después de su validación
    return data

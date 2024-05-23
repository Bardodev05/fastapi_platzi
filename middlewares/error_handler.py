# Importando BaseHTTPMiddleware de Starlette, que es un middleware base para aplicaciones web.
from starlette.middleware.base import BaseHTTPMiddleware
# Importando FastAPI, que es un marco moderno y rápido (high-performance) para construir APIs con Python 3.7+.
from fastapi import FastAPI, Request, Response
# Importando JSONResponse de FastAPI, que es una respuesta HTTP que devuelve contenido en formato JSON.
from fastapi.responses import JSONResponse

# Definiendo una clase ErrorHandler que hereda de BaseHTTPMiddleware.
# Esta clase actúa como un middleware global en una aplicación FastAPI, capturando excepciones y devolviendo respuestas JSON personalizadas.
class ErrorHandler(BaseHTTPMiddleware):
    # Constructor de la clase, inicializando el middleware con la aplicación FastAPI.
    def __init__(self, app: FastAPI) -> None:
        # Llamando al constructor de la clase padre para inicializar el middleware con la aplicación FastAPI.
        super().__init__(app)

    # Método async que se llama para cada solicitud entrante.
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        # Intenta procesar la solicitud y llamar a la siguiente función en el pipeline de middleware.
        try:
            # Si todo va bien, retorna la respuesta de la próxima función en el pipeline.
            return await call_next(request)
        # Captura cualquier excepción que ocurra durante el procesamiento de la solicitud.
        except Exception as e:
            # En caso de excepción, retorna una respuesta JSON con un código de estado 500 y el mensaje de error.
            return JSONResponse(status_code=500, content={'error': str(e)})

# Importa APIRouter de fastapi para definir rutas de API.
from fastapi import APIRouter

# Importa Dependencias, Path y Query de fastapi para definir parámetros de ruta y consulta.
from fastapi import Depends, Path, Query

# Importa JSONResponse de fastapi.responses para enviar respuestas JSON personalizadas.
from fastapi.responses import JSONResponse

# Importa BaseModel y Field de pydantic para definir modelos de datos.
from pydantic import BaseModel, Field

# Importa Optional y List de typing para definir tipos de datos opcionales y listas.
from typing import Optional, List

# Importa Session de un módulo de configuración de base de datos personalizado.
from config.database import Session

# Importa el modelo de película de un módulo de modelos personalizado.
from models.movies import Movie as MovieModel

# Importa jsonable_encoder de fastapi.encoders para convertir objetos Python en JSON.
from fastapi.encoders import jsonable_encoder

# Importa JWTBearer de un módulo de middlewares personalizado para la autenticación basada en tokens JWT.
from middlewares.jwt_bearer import JWTBearer

# Importa MovieService de un módulo de servicios personalizado para interactuar con la base de datos.
from services.movie import MovieService

# Importa Movie de un módulo de esquemas personalizado para definir el esquema de respuesta de la API.
from schemas.movie import Movie


movie_router = APIRouter()

# Ruta GET para obtener todas las películas.
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    # Crea una sesión de base de datos y obtiene todas las películas.
    db = Session()
    result = MovieService(db).get_movies()
    # Retorna las películas como una respuesta JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Ruta GET para obtener una película por ID.
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    # Crea una sesión de base de datos y obtiene la película por ID.
    db = Session()
    result = MovieService(db).get_movie(id)
    # Si la película no existe, retorna un error 404.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    # Retorna la película como una respuesta JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Ruta GET para obtener películas por categoría.
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    # Crea una sesión de base de datos y obtiene las películas por categoría.
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    # Retorna las películas como una respuesta JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Ruta POST para crear una nueva película.
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    # Crea una sesión de base de datos y crea la película.
    db = Session()
    MovieService(db).create_movie(movie)
    # Retorna un mensaje de éxito como una respuesta JSON.
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

# Ruta PUT para actualizar una película existente.
@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    # Crea una sesión de base de datos y actualiza la película.
    db = Session()
    result = MovieService(db).get_movie(id)
    # Si la película no existe, retorna un error 404.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    # Actualiza la película y retorna un mensaje de éxito.
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})

# Ruta DELETE para eliminar una película existente.
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    # Crea una sesión de base de datos y elimina la película.
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    # Si la película no existe, retorna un error 404.
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    # Elimina la película y retorna un mensaje de éxito.
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})

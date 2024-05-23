# Importa FastAPI para crear la aplicación web.
from fastapi import FastAPI

# Importa HTMLResponse para devolver respuestas en formato HTML.
from fastapi.responses import HTMLResponse

# Importa el motor de la base de datos y la clase Base de SQLAlchemy.
from config.database import engine, Base

# Importa un middleware personalizado para manejar errores.
from middlewares.error_handler import ErrorHandler

# Importa los routers de películas y usuarios.
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()  # Inicializa una nueva instancia de FastAPI. Esta instancia será el núcleo de tu aplicación web.

app.title = "Mi aplicación con FastAPI"  # Establece el título de la aplicación, que aparecerá en la documentación de OpenAPI.
app.version = "0.0.1"  # Establece la versión de la aplicación, también visible en la documentación de OpenAPI.

app.add_middleware(ErrorHandler)  # Agrega un middleware personalizado para manejar errores de manera centralizada. Esto ayuda a mantener el código limpio y a evitar la repetición de la lógica de manejo de errores en diferentes partes de la aplicación.

app.include_router(movie_router)  # Incluye un router de películas, agregando todas las rutas definidas en ese archivo a la aplicación.
app.include_router(user_router)  # Incluye un router de usuarios, agregando todas las rutas definidas en ese archivo a la aplicación.

Base.metadata.create_all(bind=engine)  # Crea todas las tablas necesarias en la base de datos basándose en los modelos definidos en SQLAlchemy. Esto es necesario antes de ejecutar la aplicación para asegurar que la estructura de la base de datos esté correctamente configurada.


# py -m uvicorn main:app --reload *-*para iniciar la aplicacion 

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


'''@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)'''

# Definiendo un middleware personalizado para verificar tokens JWT.
# Clase JWTBearer que hereda de HTTPBearer para manejar la autenticación basada en tokens JWT.
'''class JWTBearer(HTTPBearer):
    # Método especial "__call__" que se invoca cuando se realiza una solicitud.
    async def __call__(self, request: Request):
        # Llamada al método "__call__" de la superclase para verificar el token.
        auth = await super().__call__(request)
        # Validación del token JWT.
        data = validate_token(auth.credentials)
        # Verificación si el correo electrónico asociado al token coincide con uno permitido.
        # En este caso, solo se permite el acceso si el correo electrónico es "admin@gmail.com".
        if data['email']!= "admin@gmail.com":
            # Si el correo electrónico no coincide, se genera una excepción HTTP con código de estado 403.
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")'''

# Definiendo un modelo Pydantic para películas.
# Clase Movie que hereda de Pydantic.BaseModel para la validación y serialización de datos.
'''class Movie(BaseModel):
    # Campo opcional para el ID de la película.
    id: Optional[int] = None
    # Título de la película, con restricciones mínimas y máximas de longitud.
    title: str = Field(min_length=5, max_length=15)
    # Resumen o descripción de la película, con restricciones mínimas y máximas de longitud.
    overview: str = Field(min_length=15, max_length=50)
    # Año de lanzamiento de la película, limitado a años hasta 2022.
    year: int = Field(le=2022)
    # Calificación de la película, entre 1 y 10.
    rating: float = Field(ge=1, le=10)
    # Categoría de la película, con restricciones mínimas y máximas de longitud.
    category: str = Field(min_length=5, max_length=15)

    # Configuración adicional para el modelo.
    class Config:
        # Ejemplo de cómo se debe estructurar un objeto Movie.
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category" : "Acción"
            }
        }
'''

# Ruta para crear una nueva película.
# Definición de la ruta POST para crear una nueva película.
'''@app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Creación de un nuevo objeto MovieModel a partir de los datos recibidos.
    new_movie = MovieModel(**movie.dict())
    # Añadir el nuevo objeto MovieModel a la sesión de la base de datos.
    db.add(new_movie)
    # Confirmación de la transacción para hacer efectivos los cambios en la base de datos.
    db.commit()
    # Devolución de un mensaje de éxito indicando que la película se ha registrado correctamente.
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})'''

# Ruta para iniciar sesión.
# Ruta GET para obtener todos los detalles de las películas disponibles.
'''@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para obtener todos los registros de películas.
    result = db.query(MovieModel).all()
    # Codificación del resultado para que sea compatible con JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))'''

# Ruta para obtener todas las películas.
# Ruta GET para obtener todos los detalles de las películas disponibles.
'''@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para obtener todos los registros de películas.
    result = db.query(MovieModel).all()
    # Codificación del resultado para que sea compatible con JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))'''

# Ruta para obtener una película por ID.
# Ruta GET para obtener detalles de una película específica por su ID.
'''@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para encontrar la película por su ID.
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    # Comprobación si la película fue encontrada.
    if not result:
        # Si no se encontró la película, se devuelve un mensaje de error 404.
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    # Devolución de la película encontrada en formato JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))'''

# Ruta para obtener películas por categoría.
# Ruta GET para obtener películas filtradas por categoría.
'''@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para encontrar todas las películas que coincidan con la categoría especificada.
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    # Codificación del resultado para que sea compatible con JSON.
    return JSONResponse(status_code=200, content=jsonable_encoder(result))'''
    
# Ruta para actualizar una película existente.
# Definición de la ruta PUT para actualizar una película por su ID.
'''@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para encontrar la película por su ID.
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    # Comprobación si la película fue encontrada.
    if not result:
        # Si no se encontró la película, se devuelve un mensaje de error 404.
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    # Actualización de los campos de la película con los nuevos valores recibidos.
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    # Confirmación de la transacción para hacer efectivos los cambios en la base de datos.
    db.commit()
    # Devolución de un mensaje de éxito indicando que la película se ha modificado correctamente.
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})'''
    
# Ruta para eliminar una película.
# Definición de la ruta DELETE para eliminar una película por su ID.
'''@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    # Inicialización de una nueva sesión de la base de datos.
    db = Session()
    # Consulta a la base de datos para encontrar la película por su ID.
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    # Comprobación si la película fue encontrada.
    if not result:
        # Si no se encontró la película, se devuelve un mensaje de error 404.
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    # Procedimiento para eliminar la película de la base de datos.
    db.delete(result)
    # Confirmación de la transacción para hacer efectivos los cambios en la base de datos.
    db.commit()
    # Devolución de un mensaje de éxito indicando que la película se ha eliminado correctamente.
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})'''
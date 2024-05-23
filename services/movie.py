# Importa el modelo de película de un módulo de modelos personalizados.
from models.movies import Movie as MovieModel

# Importa el esquema de película de un módulo de esquemas personalizados.
from schemas.movie import Movie



class MovieService():

    def __init__(self, db) -> None:
        # Inicializa el servicio con una instancia de la base de datos.
        self.db = db

    def get_movies(self):
        # Obtiene todas las películas de la base de datos.
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id):
        # Obtiene una película específica por su ID.
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category):
        # Obtiene todas las películas filtradas por categoría.
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movie(self, movie: Movie):
        # Crea una nueva película en la base de datos.
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, data: Movie):
        # Actualiza una película existente en la base de datos.
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
       # Elimina una película específica de la base de datos.
       self.db.query(MovieModel).filter(MovieModel.id == id).delete()
       self.db.commit()
       return

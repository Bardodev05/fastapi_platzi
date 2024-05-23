# Importando Base de SQLAlchemy, que será utilizada como metaclass para definir modelos de la base de datos.
from config.database import Base
# Importando varios tipos de columnas de SQLAlchemy para definir las columnas de la tabla.
from sqlalchemy import Column, Integer, String, Float

# Definiendo una clase Movie que hereda de Base, lo que significa que SQLAlchemy creará automáticamente una tabla en la base de datos basada en esta definición.
class Movie(Base):
    # Especificando el nombre de la tabla en la base de datos a la que se mapeará esta clase.
    __tablename__ = "movies"
    
    # Definición de la columna 'id' como clave primaria (primary key), lo que significa que cada valor en esta columna debe ser único y no puede ser nulo.
    id = Column(Integer, primary_key=True)
    # Definición de la columna 'title', que almacenará el título de la película como una cadena de texto.
    title = Column(String)
    # Definición de la columna 'overview', que contendrá una descripción de la película también como una cadena de texto.
    overview = Column(String)
    # Definición de la columna 'year', que almacenará el año de lanzamiento de la película como un número entero.
    year = Column(Integer)
    # Definición de la columna 'rating', que almacenará la calificación de la película como un número flotante.
    rating = Column(Float)
    # Definición de la columna 'category', que indicará la categoría de la película como una cadena de texto.
    category = Column(String)

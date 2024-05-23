# Importando el módulo os para trabajar con rutas de archivos y directorios.
import os
# Importando create_engine de SQLAlchemy para crear una conexión a la base de datos.
from sqlalchemy import create_engine
# Importando sessionmaker de SQLAlchemy para crear sesiones de la base de datos.
from sqlalchemy.orm.session import sessionmaker
# Importando declarative_base de SQLAlchemy para definir modelos de la base de datos.
from sqlalchemy.ext.declarative import declarative_base

# Definiendo el nombre del archivo de la base de datos SQLite.
sqlite_file_name = "../database.sqlite"

# Obteniendo el directorio base donde se encuentra el script actual.
base_dir = os.path.dirname(os.path.realpath(__file__))

# Construyendo la URL de la base de datos utilizando el nombre del archivo y el directorio base.
# La URL sigue el formato "sqlite:///ruta/al/archivo", donde "sqlite://" indica que se utiliza SQLite.
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Creando el motor de la base de datos (engine) con la URL construida anteriormente.
# El parámetro echo=True habilita la impresión de mensajes de depuración sobre la operación de la base de datos.
engine = create_engine(database_url, echo=True)

# Creando una sesión de la base de datos vinculada al motor creado.
# Las sesiones son objetos que permiten interactuar con la base de datos.
Session = sessionmaker(bind=engine)

# Definiendo la base declarativa de SQLAlchemy, que servirá como metaclass para las clases que representan tablas en la base de datos.
Base = declarative_base()

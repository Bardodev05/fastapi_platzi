# Importa BaseModel y Field de pydantic para definir modelos de datos con validaciones.
from pydantic import BaseModel, Field

# Importa Optional y List de typing para definir tipos de datos opcionales.
from typing import Optional, List



class Movie(BaseModel):
    # Campos de la clase Movie con validaciones específicas:
    id: Optional[int] = None  # Identificador único de la película, opcional y puede ser None.
    title: str = Field(min_length=5, max_length=15)  # Título de la película, mínimo 5 caracteres, máximo 15.
    overview: str = Field(min_length=15, max_length=50)  # Descripción de la película, mínimo 15 caracteres, máximo 50.
    year: int = Field(le=2022)  # Año de lanzamiento de la película, no mayor a 2022.
    rating: float = Field(ge=1, le=10)  # Calificación de la película, entre 1 y 10.
    category: str = Field(min_length=5, max_length=15)  # Categoría de la película, mínimo 5 caracteres, máximo 15.

    # Subclase Config para añadir información adicional sobre el modelo:
    class Config:
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

from pydantic import BaseModel
from typing import List

class StackItem(BaseModel):
    value: float
# Définition d'un modèle de données pour représenter un élément dans une pile, avec une valeur de type float

class StackResponse(BaseModel):
    stack_id: int
    stack: List[float]
# Définition d'un modèle de réponse pour représenter le contenu d'une pile avec son ID et la liste des valeurs de la pile

class StackListResponse(BaseModel):
    stacks: dict
# Définition d'un modèle de réponse pour représenter une liste de piles disponibles avec leur contenu

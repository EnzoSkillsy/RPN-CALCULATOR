from fastapi import FastAPI, HTTPException
from models import StackItem, StackResponse, StackListResponse
from services import RPNCalculator

# Création d'une instance de l'application FastAPI
app = FastAPI()

# Création d'une instance de RPNCalculator
calculator = RPNCalculator()

# Endpoint pour lister les opérandes disponibles
@app.get("/rpn/op")
def list_operands():
    return {"operands": ["+", "-", "*", "divide"]}

# Endpoint pour appliquer un opérande à une pile spécifiée
@app.post("/rpn/op/{op}/stack/{stack_id}", response_model=StackResponse)
def apply_operand_to_stack(stack_id: int, op: str):
    if op not in ["+", "-", "*", "divide"]:
        raise HTTPException(status_code=400, detail="Invalid operand")
    try:
        calculator.apply_operation(stack_id, op)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"stack_id": stack_id, "stack": calculator.get_stack(stack_id)}

# Endpoint pour créer une nouvelle pile
@app.post("/rpn/stack", response_model=StackResponse)
def create_stack():
    stack_id = calculator.create_stack()
    return {"stack_id": stack_id, "stack": calculator.get_stack(stack_id)}
    # Crée une nouvelle pile et renvoie son ID et son contenu

# Endpoint pour lister toutes les piles disponibles
@app.get("/rpn/stack", response_model=StackListResponse)
def list_stacks():
    return {"stacks": calculator.list_stacks()}
    # Renvoie une liste de toutes les piles disponibles et leur contenu

# Endpoint pour supprimer une pile spécifiée
@app.delete("/rpn/stack/{stack_id}")
def delete_stack(stack_id: int):
    calculator.delete_stack(stack_id)
    return {"detail": "Stack deleted"}
    # Supprime la pile spécifiée par son ID et renvoie un message de confirmation

# Endpoint pour ajouter une valeur à une pile spécifiée
@app.post("/rpn/stack/{stack_id}", response_model=StackResponse)
def push_value_to_stack(stack_id: int, item: StackItem):
    calculator.push(stack_id, item.value)
    return {"stack_id": stack_id, "stack": calculator.get_stack(stack_id)}
    # Ajoute une valeur à la pile spécifiée et renvoie l'état mis à jour de la pile

# Endpoint pour récupérer le contenu d'une pile spécifiée
@app.get("/rpn/stack/{stack_id}", response_model=StackResponse)
def get_stack(stack_id: int):
    return {"stack_id": stack_id, "stack": calculator.get_stack(stack_id)}
    # Renvoie le contenu de la pile spécifiée par son ID

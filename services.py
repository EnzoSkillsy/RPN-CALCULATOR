class RPNCalculator:
    # Initialisation de la classe RPNCalculator avec un dictionnaire pour stocker les piles et un compteur pour les IDs des piles
    def __init__(self):
        self.stacks = {}
        self.next_id = 1
    # Méthode privée pour s'assurer qu'une pile existe, sinon, elle en crée une nouvelle
    def _ensure_stack_exists(self, stack_id):
        if stack_id not in self.stacks:
            self.stacks[stack_id] = []

    # Crée une nouvelle pile avec un ID unique et retourne cet ID
    def create_stack(self) -> int:
        stack_id = self.next_id
        self.next_id += 1
        self.stacks[stack_id] = []
        return stack_id

    # Retourne une liste de toutes les piles disponibles et leur contenu
    def list_stacks(self) -> dict:
        return {stack_id: stack for stack_id, stack in self.stacks.items()}

    # Supprime une pile spécifiée par son ID si elle existe
    def delete_stack(self, stack_id: int):
        if stack_id in self.stacks:
            del self.stacks[stack_id]

    # Ajoute une valeur à la pile spécifiée par son ID
    def push(self, stack_id: int, value: float):
        self._ensure_stack_exists(stack_id)
        self.stacks[stack_id].append(value)

    # Retourne le contenu de la pile spécifiée par son ID
    def get_stack(self, stack_id: int) -> list:
        self._ensure_stack_exists(stack_id)
        return self.stacks[stack_id]

    # Applique une opération sur la pile spécifiée par son ID, lève une exception si la pile ne contient pas assez d'opérandes
    def apply_operation(self, stack_id: int, operation: str):
        self._ensure_stack_exists(stack_id)
        stack = self.stacks[stack_id]
        if len(stack) < 2:
            raise ValueError("Not enough operands")

        b = stack.pop()
        a = stack.pop()
    # Récupère les deux derniers éléments de la pile pour l'opération

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                raise ValueError("Division by zero")
            result = a / b
    # Effectue l'opération spécifiée (addition, soustraction, multiplication, division) et lève une exception pour la division par zéro

        stack.append(result)
    # Ajoute le résultat de l'opération à la pile

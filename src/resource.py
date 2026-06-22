from abc import ABC

class Resource(ABC):
    name: str
    quantity: int
    moisture: int
    nutrition: int

    def __init__(self, name: str, quantity: int, moisture: int, nutrition: int):
        self.name = name
        self.quantity = quantity
        self.moisture = moisture
        self.nutrition = nutrition

    # Uma criatura tenta consumir um ou mais recursos disponíveis na área
    # por padrão, todo tipo de recurso fornece um valor de umidade
    # enquanto a nutrição fica a depender da instância específica de um recurso (planta ou carne)
#    @abstractmethod
#    def consume(self, creature: Creature, quantity: int) -> None:
#        if (quantity <= 0):
#            raise ValueError("Quantity <= 0")
#
#        if (quantity > self.quantity):
#            creature.thirst -= self.moisture
#
#        self.quantity -= quantity
#        creature.thirst -= self.moisture

    def request(self, quantity_requested: int) -> int:
        if (quantity_requested > self.quantity):
            quantity = self.quantity
            self.quantity = 0
            return quantity

        self.quantity -= quantity_requested
        return quantity_requested

class Plant(Resource):
    def __init__(self, name: str, quantity: int, moisture: int, nutrition: int):
        super().__init__(name, quantity, moisture, nutrition)
#    @override
#    def consume(self, creature: Creature, quantity: int) -> None:
#        super().consume(creature, quantity)
#        creature.hunger -= self.nutrition

class Meat(Resource):
    def __init__(self, name: str, quantity: int, moisture: int, nutrition: int):
        super().__init__(name, quantity, moisture, nutrition)
#    @override
#    def consume(self, creature: Creature, quantity: int) -> None:
#        super().consume(creature, quantity)
#        creature.hunger -= self.nutrition

class Water(Resource):
    def __init__(self, name: str, quantity: int, moisture: int, nutrition: int):
        super().__init__(name, quantity, moisture, nutrition)
#    @override
#    def consume(self, creature: Creature, quantity: int) -> None:
#        super().consume(creature, quantity)

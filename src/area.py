from .resource import Water, Plant
from .creature import Creature, Species

class Area:
    squareKm: float
    maxPopulation: int

    water: Water
    plants: list[Plant]
    creatures: list[Creature]

    species: set[Species]

    def __init__(self, kmQuadrado, populacao, agua, plantas, criaturas):
        self.squareKm: float = kmQuadrado
        self.maxPopulation: int = populacao
        self.water: Water = agua
        self.plants: list[Plant] = plantas
        self.creatures: list[Creature] = criaturas
        self.species: set[Species] = set()

    def is_full(self) -> bool:
        if len(self.creatures) >= self.maxPopulation:
            return True

        return False

    def available_space(self) -> int:
        return self.maxPopulation - len(self.creatures)

    def remove_creature(self, creature: Creature):
        self.creatures.remove(creature)

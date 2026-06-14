from .resource import Water, Plant
from .creature import Creature

class Area:
    kmQuadrado: float
    populacaoMaxima: int

    agua: Water
    plantas: list[Plant]
    criaturas: list[Creature]

    # clima: Weather
    # estacao: Season

    def __init__(self, kmQuadrado, populacao, agua, plantas, criaturas):
        self.kmQuadrado: float = kmQuadrado
        self.populacaoMaxima: int = populacao
        self.agua: Water = agua
        self.plants: list[Plant] = plantas
        self.criaturas: list[Creature] = criaturas

    def is_full(self) -> bool:
        if len(self.criaturas) >= self.populacaoMaxima:
            return True

        return False

    def available_space(self) -> int:
        return self.populacaoMaxima - len(self.criaturas)

    def remove_creature(self, creature: Creature):
        self.criaturas.remove(creature)

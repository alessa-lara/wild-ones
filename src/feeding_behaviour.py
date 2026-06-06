from collections.abc import Set
from abc import ABC

from .resource import Meat, Plant, Resource

# utilizando Set no lugar de set pois precisamos de uma estrutura que abrigue dados covariant

class FeedingBehaviour(ABC):
    canEat: Set[Resource]

class Carnivore(FeedingBehaviour):
    def __init__(self, meats: Set[Meat]) -> None:
        self.canEat = meats

class Onivore(FeedingBehaviour):
    def __init__(self, meats: Set[Meat], plants: Set[Plant]) -> None:
        self.canEat = meats | plants # uniao entre os conjuntos meats e plants

class Herbivore(FeedingBehaviour):
    def __init__(self, plants: Set[Plant]) -> None:
        self.canEat = plants

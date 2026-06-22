from collections.abc import Set
from abc import ABC, abstractmethod
from typing import override

from src.area import Area
from src.creature import Creature

from .resource import Meat, Plant, Resource

# utilizando Set no lugar de set pois precisamos de uma estrutura que abrigue dados covariant

class FeedingBehaviour(ABC):
    canEat: Set[Resource]

    # we visit an area and see if there's an available food
    @abstractmethod
    def find_food(self, area: Area) -> Creature | Plant | None:
        pass

class Carnivore(FeedingBehaviour):
    def __init__(self, meats: Set[Meat]) -> None:
        self.canEat = meats

    @override
    def find_food(self, area: Area):
        for creature in area.creatures:
            if creature.species.meat in self.canEat:
                return creature

        return None

class Onivore(FeedingBehaviour):
    def __init__(self, meats: Set[Meat], plants: Set[Plant]) -> None:
        self.canEat = meats | plants # uniao entre os conjuntos meats e plants

    @override
    def find_food(self, area: Area):
        for creature in area.creatures:
            if creature.species.meat in self.canEat:
                return creature

        for plant in area.plants:
            if plant in self.canEat and plant.quantity != 0:
                return plant

        return None

class Herbivore(FeedingBehaviour):
    def __init__(self, plants: Set[Plant]) -> None:
        self.canEat = plants

    @override
    def find_food(self, area: Area):
        for plant in area.plants:
            if plant in self.canEat and plant.quantity != 0:
                return plant

        return None

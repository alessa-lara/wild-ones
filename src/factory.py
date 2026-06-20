from types import MethodType
from typing import AbstractSet

from creature import Creature, Species
from area import Area
from state_ages import StateYoung
from feeding_behaviour import Carnivore, Herbivore, Onivore

from .resource import Plant, Meat, Water

class Factory_Area():
    def area(self, kmQuadrado: float, plantas: list[Plant], criaturas: list[Creature]) -> Area:
        populacao_maxima: int = int(kmQuadrado * 10)
        agua = Water("agua", 5000, 5,  0)

        area = Area(kmQuadrado, populacao_maxima, agua, plantas, criaturas)
        return area

    def plant(self, name, quantity, moisture, nutrition):
        plant = Plant(name, quantity, moisture, nutrition)
        return plant

    def meat(self, name, quantity, moisture, nutrition):
        meat = Meat(name, quantity, moisture, nutrition)
        return meat

class FactoryCreature():
    def __init__(self) -> None:
        self.__state_young = StateYoung()

    def creature(self, species: Species):
        creature = Creature(species, self.__state_young)
        return creature

class FactorySpecies():
    def __init__(self):
        self.available = { "sheep": self.sheep, "wolf": self.wolf }

    def wolf(self, area: Area, factory_area: Factory_Area) -> Species:
        name = "wolf"
        thirst_rate = 1
        hunger_rate = 1

        # TODO! need a way to specify that a wolf eats sheep meat
        meat = factory_area.meat("", 0, 0, 0)
        meats: AbstractSet = { meat }

        feeding = Carnivore(meats)
        max_offspring = 5

        wolf = Species(name, thirst_rate, hunger_rate, feeding, area, max_offspring)
        return wolf

    def sheep(self, area: Area, factory_area: Factory_Area) -> Species:
        name = "sheep"
        thirst_rate = 1
        hunger_rate = 1

        grass = factory_area.plant("grama", 0, 0.5, 1)
        plants: AbstractSet = { grass }
        area.plants.append(grass)

        feeding = Herbivore(plants)
        max_offspring = 2

        sheep = Species(name, thirst_rate, hunger_rate, feeding, area, max_offspring)

        return sheep

    def list_available(self):
        for species in self.available:
            print(species)

    def select_available(self) -> MethodType:
        inp = input("What species you want to create? ")

        if inp not in self.available:
            print(inp, " is not a valid species")
            return self.select_available()

        return self.available[inp]

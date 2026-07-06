from types import MethodType
from typing import AbstractSet

from .creature import Creature, Species
from .area import Area
from .state_ages import StateYoung
from .feeding_behaviour import Carnivore, Herbivore
from .factory_area_resources import Factory_Resource

class FactoryCreature():
    def __init__(self) -> None:
        self.__state_young = StateYoung()

    def creature(self, species: Species):
        creature = Creature(species, self.__state_young)
        species.creature_counter += 1
        return creature

class FactorySpecies():
    def __init__(self):
        self.available = { "sheep": self.sheep, "wolf": self.wolf }

    def wolf(self, area: Area, factory_resource: Factory_Resource) -> Species:
        name = "wolf"
        thirst_rate = 1
        hunger_rate = 1

        meat = factory_resource.sheep_meat()
        meats: AbstractSet = { meat }

        feeding = Carnivore(meats)
        max_offspring = 5

        on_death_meat = factory_resource.wolf_meat()

        wolf = Species(name, thirst_rate, hunger_rate, feeding, area, max_offspring, on_death_meat)
        return wolf

    def sheep(self, area: Area, factory_resource: factory_resource) -> Species:
        name = "sheep"
        thirst_rate = 1
        hunger_rate = 1

        grass = factory_resource.grass(1)
        plants: AbstractSet = { grass }
        area.plants.append(grass)

        feeding = Herbivore(plants)
        max_offspring = 2

        on_death_meat = factory_resource.sheep_meat()

        sheep = Species(name, thirst_rate, hunger_rate, feeding, area, max_offspring, on_death_meat)

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

from __future__ import annotations
from collections.abc import Set
import random

from .area import Area
from .resource import Resource, Water
from .state_ages import StateAge, StateDead, StateYoung
from .feeding_behaviour import FeedingBehaviour
from .factory import Factory_Area

class Species():
    def __init__(self, name: str, thirst_rate: int, hunger_rate: int, feeding_behaviour: FeedingBehaviour, area: Area, max_offspring: int):
        self.__species_name: str = name
        self.__thirst_rate: int = thirst_rate
        self.__hunger_rate: int = hunger_rate
        self.__feeding_behaviour = feeding_behaviour
        self.__area = area
        self.__max_offspring = max_offspring
        self.__id_count = 0
        self.meat = Factory_Area().meat(self.species_name, 1, 0.5, 2) # dunno what to do, keep this while i think

    @property
    def species_name(self):
        return self.__species_name

    @property
    def thirst_rate(self):
        return self.__thirst_rate

    @property
    def hunger_rate(self):
        return self.__hunger_rate

    @property
    def feeding_behaviour(self):
        return self.__feeding_behaviour

    @property
    def area(self):
        return self.__area

    @property
    def max_offspring(self):
        return self.__max_offspring

    @property
    def id_count(self):
        self.__id_count += 1
        return self.id_count

class Creature():
    species: Species

    thirst: int # maybe bool?
    hunger: int # maybe bool?

    age: StateAge

    def __init__(self, species: Species, age: StateAge):
        self.id = species.id_count
        self.species = species
        self.age = age

        self.thirst = 0
        self.hunger = 0

    def consume(self, resource: Resource, quantity: int):
        is_water: bool = isinstance(resource, Water)
        can_eat: Set[Resource] = self.species.feeding_behaviour.canEat

        if resource not in can_eat and not is_water:
            raise ValueError(f"{self} não aceita {resource} em sua dieta")

        resource.consume(self, quantity)

    def multiply(self) -> list[Creature] | None:
        if self.species.area.is_full():
            return

        if self.species.area.available_space() >= self.species.max_offspring:
            n = random.randrange(1, self.species.max_offspring + 1) # randrange is exclusive
        else:
            n = random.randrange(1, self.species.area.available_space())

        offspring: list[Creature] = []
        for _ in range(n):
            creature = Creature(self.species, StateYoung())

            offspring.append(creature)

        return offspring

    def advance_age(self):
        new_age = self.age.advance_age()

        if new_age is None:
            return

        if new_age is StateDead:
            self.species.area.remove_creature(self)
            return

        self.age = new_age

        self.hunger_rate *= new_age.resource_comsumption
        self.thirst_rate *= new_age.resource_comsumption

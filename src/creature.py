from __future__ import annotations
import random

from .state_ages import StateAge, StateDead, StateYoung

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .area import Area
    from .resource import Meat
    from .feeding_behaviour import FeedingBehaviour

class Species():
    def __init__(self, name: str, thirst_rate: int, hunger_rate: int, feeding_behaviour: FeedingBehaviour, area: Area, max_offspring: int, species_meat: Meat):
        self.__name: str = name
        self.__thirst_rate: int = thirst_rate
        self.__hunger_rate: int = hunger_rate
        self.__feeding_behaviour = feeding_behaviour
        self.__area = area
        self.__max_offspring = max_offspring
        self.__id_count = 0
        self.creature_counter = 0
        self.meat = species_meat # dunno what to do, keep this while i think

    @property
    def name(self):
        return self.__name

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
        return self.__id_count

class Creature():
    species: Species

    thirst: float # maybe bool?
    hunger: float # maybe bool?

    age: StateAge

    def __init__(self, species: Species, age: StateAge):
        self.id = species.id_count
        self.species = species
        self.age = age

        self.thirst = 0
        self.hunger = 0

    def eat(self):
        food = self.species.feeding_behaviour.find_food(self.species.area)

        if food is None:
            return

        nutrition: int = 0
        moisture: int = 0
        quantity: int = 1

        request: int = 0

        if isinstance(food, Creature):
            nutrition = food.species.meat.nutrition
            moisture = food.species.meat.moisture

            request = 1
            request = food.species.meat.request(request)

            food.die()
        else:
            nutrition = food.nutrition
            moisture = food.moisture

            request = self.hunger // food.nutrition
            quantity = food.request(request)

        while quantity > 0:
            self.hunger -= nutrition
            self.thirst -= moisture
            quantity -= 1

            if self.hunger < 0: # a criatura esta satisfeita
                self.hunger = 0
                break

            if self.thirst < 0:
                self.thirst = 0

    def drink(self):
        request = int(self.thirst)
        water = self.species.area.water
        n = water.request(request)

        for _ in range(0, n):
            self.thirst -= water.moisture

        if self.thirst < 0:
            self.thirst = 0

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

        self.species.creature_counter += n

        return offspring

    def advance_age(self):
        new_age = self.age.advance_age()

        if new_age is None:
            return

        if isinstance(new_age, StateDead):
            self.species.area.remove_creature(self)
            self.species.creature_counter -= 1
            return

        self.age = new_age

        # self.hunger_rate *= new_age.resource_comsumption # cant do this anymore
        # self.thirst_rate *= new_age.resource_comsumption # cant do this anymore

    def die(self):
        self.species.area.remove_creature(self)
        self.species.creature_counter -= 1

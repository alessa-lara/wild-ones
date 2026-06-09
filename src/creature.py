from __future__ import annotations
from collections.abc import Set
import random

from .area import Area
from .resource import Resource, Water
from .state_ages import StateAge, StateYoung
from .feeding_behaviour import FeedingBehaviour

class Creature():
    creature: str
    thirst: int
    thirst_rate: int

    hunger: int
    hunger_rate: int

    feeding_behaviour: FeedingBehaviour
    age: StateAge

    max_offspring: int

    def __init__(self, creature: str, thirst_rate: int, hunger_rate: int, feeding_behaviour: FeedingBehaviour, age: StateAge) -> None:
        self.creature = creature
        self.thirst_rate = thirst_rate
        self.hunger_rate = hunger_rate
        self.feeding_behaviour = feeding_behaviour
        self.age = age

    def consume(self, resource: Resource, quantity: int):
        is_water: bool = isinstance(resource, Water)
        can_eat: Set[Resource] = self.feeding_behaviour.canEat

        if resource not in can_eat and not is_water:
            raise ValueError(f"{self} não aceita {resource} em sua dieta")

        resource.consume(self, quantity)

    def multiply(self, area: Area) -> list[Creature] | None:
        if area.is_full():
            return

        if area.available_space() >= self.max_offspring:
            n = random.randrange(1, self.max_offspring)
        else:
            n = random.randrange(1, area.available_space())

        offspring: list[Creature] = []
        for _ in range(n):
            creature = Creature(
                self.creature, self.thirst_rate, self.hunger_rate, self.feeding_behaviour, age = StateYoung()
            )
            offspring.append(creature)

        return offspring

    def advance_age(self):
        new_age = self.age.advance_age()

        if new_age is None:
            return

        self.age = new_age

        self.hunger_rate *= new_age.resource_comsumption
        self.thirst_rate *= new_age.resource_comsumption

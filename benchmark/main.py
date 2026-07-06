from pympler import asizeof

from src.factory_area_resources import Factory_Area
from src.factory_area_resources import Factory_Resource
from src.factory_species_creatures import FactoryCreature
from src.factory_species_creatures import FactorySpecies

from .no_flyweight import Creature_No_Flyweight

def flyweight(area, n):
    species = fact_spec.wolf(area, fact_resource) 
    creature = fact_creat.creature(species)

    size_s = asizeof.asizeof(species)
    size_c = asizeof.asizeof(creature)
    print(f"Species: {size_s} bytes")
    print(f"Creature: {size_c} bytes")
    print(f"Size per creature: {size_c - size_s} bytes")
    calc = size_s + (n * (size_c - size_s))
    print(f"Total for {n} creatures: {size_s} + ({n} * {size_c - size_s}) = {calc} bytes\n")

    return calc

def no_flyweight(area, n):
    from src.resource import Meat
    from src.feeding_behaviour import Carnivore
    from src.state_ages import StateYoung

    name = "no_flyweight" 
    tr = 1 
    hr = 1
    a = area
    mx_o = 1
    id = 0
    meat = Meat("", 0, 0, 0)
    fb = Carnivore({meat})
    t = 0
    h = 0
    cm = 1
    age = StateYoung()

    creature = Creature_No_Flyweight(name, tr, hr, fb, a, mx_o, id, meat, t, h, cm, age)
    size_c = asizeof.asizeof(creature)

    calc = n * size_c
    print(f"Creature without flyweight: {size_c} bytes")
    print(f"Total for {n} creatures: {n} * {size_c} = {calc}\n")

    return calc

fact_area = Factory_Area()
fact_resource = Factory_Resource()
fact_spec = FactorySpecies()
fact_creat = FactoryCreature()

plants = []
creatures = []
area = fact_area.area(100, plants, creatures)

fl = flyweight(area, 1000)
nfl = no_flyweight(area, 1000)

after_pattern = (fl / nfl) * 100
print(f"memory reduction: {100 - after_pattern}%")

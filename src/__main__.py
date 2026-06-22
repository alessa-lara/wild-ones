from types import MethodType

from .factory_area_resources import Factory_Area
from .factory_species_creatures import FactoryCreature, FactorySpecies

from .state_ages import StateMature

from .area import Area

def main():
    fact_area = Factory_Area()
    fact_spec = FactorySpecies()
    fact_creat = FactoryCreature()

    plants = []
    creatures = []
    area = fact_area.area(100, plants, creatures)

    inp: int = 0
    while (inp != 2):
        area_populate(fact_area, fact_spec, fact_creat, area)

        print("You wish to create another species?")
        print("[1] Yes")
        print("[2] No")
        inp = int( input() )

    days = 0
    while True:
        print(f"day {days}: there are {len(area.creatures)} creatures in the area.")
        print("area resources:")
        print(f"- water: {area.water.quantity}")

        for plant in area.plants:
            print(f"{plant.name}: {plant.quantity}")

        game(area)
        days += 1
        input("Press any character to advance the day")
        clear_screen()

def game(area: Area):
    for creature in area.creatures:
        if creature.hunger > 1:
            creature.eat()
        else:
            creature.hunger += creature.species.hunger_rate

        if creature.thirst > 1:
            creature.drink()
        else:
            creature.thirst += creature.species.thirst_rate

        if not isinstance(creature.age, StateMature):
            continue

        if creature.thirst <= 0.5 and creature.hunger <= 0.5:
            offspring = creature.multiply()

            if offspring is None:
                continue

            for child in offspring:
                area.creatures.append(child)

# creates an ansi escape sequence
def clear_screen():
    print("\033[H\033[J", end="")

def area_populate(fact_area, fact_spec, fact_creat, area):
    fact_spec.list_available()

    spec_func: MethodType = fact_spec.select_available() # we received a function to create a valid species
    species = spec_func(area, fact_area) 

    inp: int = 0
    while (inp <= 0):
        print(f"How many creatures of the type {species.name} you want to create? ")
        inp = int( input() )

    for _ in range(0, inp):
        creature = fact_creat.creature(species)
        area.creatures.append(creature)

if __name__ == "__main__":
    main()

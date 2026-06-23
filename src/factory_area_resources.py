from .resource import Resource, Meat, Plant, Water
from .area import Area
from .creature import Creature

class factory_resource():
    def __init__(self):
        self.__registry: dict[str, Resource] = {}

    def __plant(self, name, quantity, moisture, nutrition):
        plant = Plant(name, quantity, moisture, nutrition)
        return plant

    def __meat(self, name, quantity, moisture, nutrition):
        meat = Meat(name, quantity, moisture, nutrition)
        return meat

    def sheep_meat(self) -> Meat:
        if "sheep" in self.__registry:
            return self.__registry.get("sheep") # type: ignore

        meat = self.__meat("sheep meat", 1, moisture=0.5, nutrition=1)
        self.__registry["sheep"] = meat

        return meat

    def wolf_meat(self) -> Meat:
        if "wolf" in self.__registry:
            return self.__registry.get("wolf") # type: ignore

        meat = self.__meat("wolf meat", 1, moisture=0.5, nutrition=1)
        self.__registry["wolf"] = meat

        return meat

    def grass(self, quantity: int) -> Plant:
        if "grass" in self.__registry:
            return self.__registry.get("grass") # type: ignore

        plant = self.__plant("grass", quantity, moisture=0.2, nutrition=0.4)
        self.__registry["grass"] = plant

        return plant

    def mushroom(self, quantity: int) -> Plant:
        if "mushroom" in self.__registry:
            return self.__registry.get("mushroom") # type: ignore

        plant = self.__plant("mushroom", quantity, moisture=0.1, nutrition=0.6)
        self.__registry["mushroom"] = plant

        return plant

class Factory_Area():
    def area(self, kmQuadrado: float, plantas: list[Plant], criaturas: list[Creature]) -> Area:
        populacao_maxima: int = int(kmQuadrado * 10)
        agua = Water("agua", 5000, 5,  0)

        area = Area(kmQuadrado, populacao_maxima, agua, plantas, criaturas)
        return area

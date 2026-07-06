class Creature_No_Flyweight():
    def __init__(self, name, tr, hr, fb, a, mx_o, id, meat, t, h, cm, age):
        self.__name: str = name
        self.__thirst_rate: int = tr
        self.__hunger_rate: int = hr
        self.__feeding_behaviour = fb
        self.__area = a
        self.__max_offspring = mx_o
        self.__id_count = id
        self.creature_counter = 0
        self.meat = meat
        self.thirst: float = t
        self.hunger: float = h

        self.comsumption_modifier: int = cm

        self.age = age

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import override

class StateAge(ABC):
    resource_comsumption: int

    @abstractmethod
    def advance_age(self) -> StateAge | None:
        pass

class StateYoung(StateAge):
    def __init__(self) -> None:
        self.resource_comsumption: int = 1

    @override
    def advance_age(self) -> StateMature:
        return StateMature()

class StateMature(StateAge):
    def __init__(self) -> None:
        self.resource_comsumption: int = 2

    @override
    def advance_age(self) -> StateDead:
        return StateDead()

class StateDead(StateAge):
    def __init__(self) -> None:
        self.resource_comsumption: int = 0

    @override
    def advance_age(self) -> None:
        return

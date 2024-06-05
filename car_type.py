from vehicle import Vehicle
from abc import ABC, abstractmethod


class Sedan(Vehicle):
    def __init__(self, length: float, width: float, seats: int, fuel_type, steering_wheel):
        super().__init__(fuel_type, steering_wheel)
        self.length = length.__round__(2)
        self.width = width.__round__(2)
        self.seats = seats

    @abstractmethod
    def voice_of_horn(self):
        pass


class Suv(Vehicle):
    def __init__(self, length: float, width: float, seats: int, fuel_type: str, steering_wheel: str, AWD: bool):
        super().__init__(fuel_type, steering_wheel)
        self.length = length
        self.width = width
        self.seats = seats
        self.AWD = AWD

    @abstractmethod
    def voice_of_horn(self):
        pass

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel: str, steering_wheel: str):
        self.fuel = fuel.lower()
        self.steering_wheel = steering_wheel.lower()

    @property
    def steering_wheel(self):
        return self._steering_wheel

    @steering_wheel.setter
    def steering_wheel(self, side):
        if side not in ["left", "right", "middle"]:
            raise ValueError("Invalid steering wheel side")
        return side

    def start_engine(self):
        if self.fuel == 'electric':
            print('electric engine started quietly')
        else:
            print('engine started with some sound')

    @abstractmethod
    def voice_of_horn(self):
        pass



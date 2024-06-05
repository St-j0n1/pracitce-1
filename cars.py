from abc import ABC

from car_type import Suv, Sedan
from vehicle import Vehicle
from parts import Engine, Gearbox


class Car(Vehicle, ABC):
    def __init__(self, model:str, color:str, price:int, fuel:str, steering_wheel:str):
        self.model = model
        self.color = color
        self.price = price
        self.engine = Engine
        self.Gearbox = Gearbox
        super().__init__(fuel, steering_wheel)

    def voice_of_horn(self):
        return "beep-beep"


if __name__ == "__main__":
    c1 = Car("model", "color", 1000, "gasoline", "left")
    c1.engine = Engine(1000, 100)
    c1.Gearbox = Gearbox(8)
    print(c1.engine.is_economy())
    print(c1.Gearbox.gearbox_type())
    c1.start_engine()
    c1.steering_wheel = "left"
    print(c1.__dict__)

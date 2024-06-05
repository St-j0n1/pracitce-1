class Engine:
    def __init__(self, cc, hp):
        self.cc = cc
        self.hp = hp

    def is_economy(self):
        if self.cc < 1000:
            return True
        else:
            return False


class Gearbox:
    def __init__(self, gears: int):
        self.gears = gears

    def gearbox_type(self):
        if self.gears == 1:
            return "Variation"

        elif self.gears <= 5:
            return "Manual"

        else:
            return "Automatic"

    def __str__(self):
        return f"{self.gears} gears, {self.gearbox_type()}"

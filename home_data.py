from datetime import datetime
import random

from time_generator import generate_temp_and_humidity, generate_tv, generate_is_broken, \
    generate_temp_and_humidity_outdoor


class Room:
    def __init__(self):
        self.temp, self.humidity = generate_temp_and_humidity()


class Kitchen(Room):
    def __init__(self):
        super().__init__()
        self.is_smoke = False


class Bedroom(Room):
    def __init__(self):
        super().__init__()
        self.is_tv_on = generate_tv(20, 22)


class Bathroom(Room):
    def __init__(self):
        super().__init__()
        self.is_smoke = False


class LivingRoom(Room):
    def __init__(self):
        super().__init__()
        self.is_tv_on = generate_tv(18, 20)


class Hall(Room):
    pass


class Entrance(Room):
    def __init__(self):
        super().__init__()
        self.is_broken = False


class Balcony(Room):

    def __init__(self):
        super().__init__()
        self.is_broken = generate_is_broken()
        self.temp, self.humidity = generate_temp_and_humidity_outdoor()


class Garage(Room):
    def __init__(self):
        super().__init__()
        self.is_smoke = False


class House:

    def __init__(self):
        self.kitchen = Kitchen()
        self.bedroom = Bedroom()
        self.bathroom = Bathroom()
        self.living_room = LivingRoom()
        self.hall = Hall()
        self.balcony = Balcony()
        self.garage = Garage()

    def to_dict(self):
        result = {}
        for k, v in self.__dict__.items():
            if hasattr(v, '__dict__'):
                result[k] = v.__dict__
            else:
                result[k] = v
        return result

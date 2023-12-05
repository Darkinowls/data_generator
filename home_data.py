

class Room:
    def __init__(self):
        self.temp = 20
        self.humidity = 40


class Kitchen(Room):
    def __init__(self):
        super().__init__()
        self.is_smoke = False


class Bedroom(Room):
    def __init__(self):
        super().__init__()
        self.is_tv_on = False


class Bathroom(Room):
    def __init__(self):
        super().__init__()
        self.is_smoke = False


class LivingRoom(Room):
    def __init__(self):
        super().__init__()
        self.is_tv_on = False


class Hall(Room):
    pass


class Balcony(Room):
    pass


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

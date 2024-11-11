class Transport():
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed
    def print_info(self):
        print(self.model, self.year, self.speed)
    def fun_1(self, distance):
        self.distance =  distance
        print(self.distance * self.speed)

class Cars(Transport):
    def __init__(self, model, year, speed, places):
        super().__init__(model, year, speed)
        self.places = places


class Helicopter(Transport):
    def __init__(self, model, year, speed):
        super().__init__(model, year, speed)
    def rise(self):
        print('брбрбрбрбррбрб')

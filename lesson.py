class Test():
    def __init__(self, name):
        self.n1 = 1000
        self.n2 = 999
        self.n3 = 990
    def run(self):
        print([self.n1, self.n2, self.n3])

# ------------------------------------------------------------------------------------------


class Cars():
    def __init__(self, producer, model, year, speed):
        self.producer = producer
        self.model = model
        self.year = year
        self.speed = speed
    def info_car(self):
        print('Это машина', self.producer, self.model, self.year, 'года выпуска, имеющая среднюю скорость', self.speed, 'км/час')
    def speed_car(self, dist):
        print(dist/self.speed)


cars_p911 = Cars('Porche', '911 992 Carera 4s cabrio', 2024, 100)

# ------------------------------------------------------------------------------------------

class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        print(self.num1 + self.num2)

    def subtraction(self):
        print(self.num1 - self.num2)

    def multiplication(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num1 / self.num2)


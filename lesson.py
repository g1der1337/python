class Cars():
    def __int__(self, producer, model, year, speed):
        self.producer = producer
        self.model = model
        self.year = year
        self.speed = speed
    def info_car(self):
        print('Это машина', self.producer, self.model, self.year, 'года выпуска, имеющая среднюю скорость', self.speed, 'км/час')
    def speed_car(self, dist):
        print(dist/self.speed)


cars_p911 = Cars('Porche', '911 992 Carera 4s cabrio', 2024, 100)
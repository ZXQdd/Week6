class Car:

    def __init__(self, fuel=0, name=""):

        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):

        self.fuel += amount

    def drive(self, distance):

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        return("Car = {}, fuel = {}, odometer = {}".format(self.name,str(self.fuel),str(self.odometer)))
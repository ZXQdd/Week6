from prac_06.car import Car


def main():

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()
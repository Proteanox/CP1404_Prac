"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    limo = Car("limo:", 100)  # adding the limo object
    limo.add_fuel(20)  # adding fuel
    print("limo fuel: ", limo.fuel)  # output
    limo.drive(115)  # using drive function
    print("limo odo: ", limo.odometer)


main()

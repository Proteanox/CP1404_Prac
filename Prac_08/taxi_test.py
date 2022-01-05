from Prac_08.taxi import Taxi


def main():
    """ Taxi test case"""
    Prius1 = Taxi("Prius1", 100)
    Prius1.drive(40)
    print(Prius1)
    print(f"{Prius1.get_fare()} $ is the fare.")
    Prius1.start_fare()
    Prius1.drive(100)
    print(Prius1)
    print(f"{Prius1.get_fare()} $ is the Fare.")


main()

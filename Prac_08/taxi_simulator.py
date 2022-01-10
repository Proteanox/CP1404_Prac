from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import ServiceServiceTaxi


def main():
    print("Let's Drive!")
    taxi = [Taxi("Prius", 100), ServiceServiceTaxi("Limo", 100, 2), ServiceServiceTaxi("Hummer", 200, 4)]
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        ans = input(">>>")
        if ans == 'q':
            print("\n Goodbye")
            print("Total trip cost: ${:.2f}".format(total_bill))
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))

        elif ans == 'c':
            print("Taxis available: ")


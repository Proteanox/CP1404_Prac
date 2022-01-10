from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi
from Prac_06.car import Car


def main():
    total = 0
    print("Let's Drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print(f"Bill to date: {total}")

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        ans = input(">>>")
        if ans == 'q':
            print("\n Goodbye")
            print("Total trip cost: ${:.2f}".format(total))
            print("Taxis are now:")
            for count, taxi in enumerate(taxis):
                print("{} - {}".format(count, taxi))
            break
        elif ans == 'c':
            print("Taxis available: ")
            for count, taxi in enumerate(taxis):
                print("{} - {}".format(count, taxi))
            choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[choice]
            except IndexError:
                print("Invalid taxi choice")

        elif ans == 'd':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive How far"))
                current_taxi.drive(drive_distance)

                print(f"Your {current_taxi.name} trip costs you {current_taxi.get_fare()}")
                total += current_taxi.get_fare()
            else:
                print(' YOU NEED TO CHOOSE A TAXI FIRST')
        else:
            print("Invalid Option")


main()

from Prac_08.unreliable_car import UnreliableCar


def main():
    """ main() opening function"""
    taxi_1 = UnreliableCar("Prius1", 100, 44)
    print(taxi_1)
    taxi_1.drive(34)
    print(taxi_1)

main()

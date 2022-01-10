from Prac_08.car import Car
from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi


def taxi_sim_test():
    trip = Taxi("Prius", 100)
    trip.start_fare()
    trip.drive(40)
    print(trip.get_fare())
    print(trip)

    trip_1 = SilverServiceTaxi("Ferrari", 150, 2.4)
    trip_1.start_fare()
    trip_1.drive(55)
    print(trip_1.get_fare())
    print(trip_1)

    trip_2 = SilverServiceTaxi("Gallias", 195, 3.2)
    trip_2.start_fare()
    trip_2.drive(37)
    print(trip_2.get_fare())
    print(trip_2)


taxi_sim_test()

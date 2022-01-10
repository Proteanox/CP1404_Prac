from Prac_08.silver_service_taxi import ServiceServiceTaxi


def main():
    taxi_1 = ServiceServiceTaxi("Pruis1", 100, 2.2)
    print(taxi_1)
    taxi_1.drive(45)
    print(taxi_1)
    print(taxi_1.get_fare())


main()

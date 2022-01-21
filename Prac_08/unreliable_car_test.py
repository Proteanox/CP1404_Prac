"""Name: Siddhant Kumar Jha
   Date: 09/01/2022
Github Url:https://github.com/Proteanox/CP1404_Prac/tree/master/Prac_08"""
from Prac_08.unreliable_car import UnreliableCar


def main():
    """ main() opening function"""
    taxi_1 = UnreliableCar("Prius1", 100, 44)
    print(taxi_1)
    taxi_1.drive(34)
    print(taxi_1)

main()

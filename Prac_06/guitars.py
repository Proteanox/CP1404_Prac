from Prac_06.guitar import Guitar


def main():
    guitar_list = []
    print("My Guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitar_list.append(add_guitar)
        print(f"{add_guitar} is added")
        name = input("Name: ")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    for guitar in guitar_list:
        print(f"Guitar {guitar_list.index(guitar) + 1}: {guitar}")


main()

from Prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035)
another = Guitar("Another Guitar", 2013, 14000)

guitars = [gibson, another]

for guitar in guitars:
    print(f"{guitar.name} get_age()- Expected {guitar.get_age()} Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage()- Expected {guitar.is_vintage()} Got {guitar.is_vintage()}")
import random

PICK_LENGTH = 6
MIN = 1
MAX = 45


def main():
    """Display the Quick pick lines as a matrix"""
    no_quick_picks = int(input("How many Picks? "))
    while no_quick_picks < 0:
        print("Invalid Input")
        no_quick_picks = int(input("How many Picks? "))
    generate_matrix(no_quick_picks)


def generate_matrix(no_quick_picks):
    """generate the random number matrix without repetition"""
    for i in range(no_quick_picks):
        quick_list = []
        for j in range(PICK_LENGTH):
            # This checks to see if there are duplicate numbers
            r = random.randint(MIN, MAX)
            if r not in quick_list:
                quick_list.append(r)
            j += 1
        print(*quick_list, sep=" ")


main()

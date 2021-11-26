"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



def main():
    score = float(input("Enter score: "))
    check_score(score)


def check_score(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif 90 > score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    elif score < 50:
        print("Bad")


main()

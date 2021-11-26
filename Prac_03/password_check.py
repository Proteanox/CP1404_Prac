MIN_LENGTH = 10


def main():
    password = get_password()
    output_password(password)


def get_password():
    password = input("Enter Your Password")
    while len(password) < MIN_LENGTH:
        print("Invalid Password")
        password = input("Enter Your Password")
    return password


def output_password(length):
    with open('password.txt', 'w') as f:
        f.write(len(length) * '*')

main()
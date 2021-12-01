def main():
    iterations = int(input("Enter no of iterations: "))
    num_list = create_num_list(iterations)
    output_statements(iterations, num_list)
    username = input(" Enter Your Username: ")
    check_username(username)


def create_num_list(iterations):
    num_list = []
    for i in range(iterations):
        numbers = float(input("Number: "))
        num_list.append(numbers)
    return num_list


def output_statements(iterations, num_list):
    print(
        f"The first number is {num_list[0]} \nThe last number is {num_list[len(num_list) - 1]} \n The smallest number "
        f"is {min(num_list)}\nThe largest "
        f"number is {max(num_list)}\nThe average of the numbers is {sum(num_list) / iterations}")


def check_username(username):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    while username not in usernames:
        print("Invalid Username")
        username = input(" Enter Your Username")
    print("Access Granted")


main()

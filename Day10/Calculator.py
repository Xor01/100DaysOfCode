# Calculator
from art import logo


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


operations = {
    "+": add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    n1 = float(input("What is the first number: "))
    program_continue = 'y'

    for key in operations:
        print(key)

    while program_continue == 'y':
        operation = input("Pick an operation: ")

        n2 = float(input("What is the next number: "))

        answer = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {answer}")
        program_continue = input("Would you like to continue calculating 'y' or 'n' to new start or 'e' to exit: ")
        n1 = answer

    if program_continue == 'n':
        calculator()
    elif program_continue == 'e':
        return


calculator()

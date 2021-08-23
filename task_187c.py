import sys
import math

print("Task 187c: count how many numbers are squares of even number in input list of natural numbers")


def continue_or_not():
    """
    Asks a user whether he/she wants to continue using program or not,
    if not program is terminated, else program continues its work
    """
    print("Do you want to continue?(yes/no)")
    answer = input()
    if answer == "yes":
        main()
    else:
        print("Thank you! Program has ended its work")
        sys.exit()


def input_natural_numbers():
    """
    Asks user to enter list of natural numbers, if input is wrong, output alert message
    and asks user whether he wants to try again
    """
    print("Enter list of natural numbers divided by space: ")
    numbers_in_string = input().split(" ")
    if not numbers_in_string:
        print("Wrong input! Enter natural numbers(1, 2, 3, 4...)")
        return continue_or_not()
    try:
        numbers = [int(i) for i in numbers_in_string]
    except ValueError:
        print("Wrong input! Enter natural numbers(1, 2, 3, 4...)")
        return continue_or_not()
    else:
        for i in numbers:
            if i < 1:
                print("Wrong input! Natural number must be greater than zero(1, 2, 3, 4...)")
                return continue_or_not()

        return numbers


def count_squares_of_even_number(numbers):
    """
    Takes a list of numbers as arguments and returns quantity of numbers that are
    squares of even number
    """
    if not numbers:
        return continue_or_not()
    counter = len([i for i in numbers if math.sqrt(i) % 2 == 0])
    return counter


def main():
    numbers = input_natural_numbers()
    counter = count_squares_of_even_number(numbers)
    print(f"There is {counter} numbers that are squares of even number in {numbers}")
    continue_or_not()


main()

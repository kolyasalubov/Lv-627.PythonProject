import sys

print("Task 554: find all pythagorean triples that lower than input number n")


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


def input_natural_number():
    """
    Asks user to enter natural number, if input is wrong, output alert message
    and asks user whether he wants to try again
    """
    print("Enter natural number: ")
    try:
        number = int(input())
    except ValueError:
        print("Wrong input! Enter natural numbers(1, 2, 3, 4...)")
        return continue_or_not()
    else:
        if number < 1:
            print("Wrong input! Natural number must be greater than zero(1, 2, 3, 4...)")
            return continue_or_not()

        return number


def count_pythagorean_triples(number):
    """
    Takes an integer as arguments and returns all pythagorean triples
    lower than given number
    """
    pythagorean_triples = []
    for c in range(number):
        for b in range(c):
            for a in range(b):
                if a ** 2 + b ** 2 == c ** 2:
                    pythagorean_triples.append((a, b, c))
    return pythagorean_triples


def main():
    number = input_natural_number()
    pythagorean_triples = count_pythagorean_triples(number)
    print(f"List of all pythagorean triples lower than {number}:\n{pythagorean_triples} ")
    continue_or_not()


main()

"""Task 323. Given natural n. Get all natural coprime numbers less than n."""

from math import gcd


def check_input(number):
    """Check if input is natural number."""
    if number.isdigit() is True:
        return int(number)
    print("Your input wasn't correct.")


def task_323():
    """Check if numbers are coprime and returns list of all less than n."""
    number = check_input(input("Input natural n\n"))
    if number is not None:
        return [i for i in range(1, number) if gcd(i, number) == 1]
    return "Try again."


if __name__ == "__main__":
    print(task_323())

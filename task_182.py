"""Task 182. Given natural n, integer from 1 to n.
Find number and sum of those members of a given sequence that are divisible by 5 and not divisible by 7."""


def check_input(number):
    """Check if input is natural number."""
    if number.isdigit() is True:
        return int(number)
    print("Your input wasn't correct.")


def task_182():
    """Check members of a given sequence if they are divisible by 5 and not divisible by 7.
    Returns their number and sum."""
    number = check_input(input("Input natural n\n"))
    sum_of_numbers = 0
    count_of_numbers = 0
    if number is not None:
        for i in range(number):
            if i % 5 == 0 and i % 7 != 0:
                sum_of_numbers += i
                count_of_numbers += 1
        return ("In sequence 1...{0} is {1} members that are divisible by 5 "
                "and not divisible by 7 and their sum is {2}").format(number, count_of_numbers, sum_of_numbers)
    return "Try again."


if __name__ == "__main__":
    print(task_182())

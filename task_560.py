"""Task 560. Find all pairs of friendly numbers between 200 and 300"""


def find_sum_of_divisors(number):
    """Returns sum of all divisors of the number."""
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors


def task_560():
    """Finds sum of divisors of given number and the sum of divisors of first sum.
    If second sum == number returns this pair."""
    for i in range(200, 300):
        first_sum = find_sum_of_divisors(i)
        second_sum = find_sum_of_divisors(first_sum)
        if i == second_sum and i != first_sum and i == min(i, first_sum):
            return i, first_sum


if __name__ == "__main__":
    print(task_560())

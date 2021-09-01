from task import Task


def find_sum_of_divisors(number: int) -> int:
    """
    Finds sum of all divisors of the number."
    :param number: int
    :return: sum: int
    """""
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors


def _task() -> tuple:
    """
    Finds sum of divisors of given number and the sum of divisors of first sum.
    If second sum == number returns this pair.
    :return: tuple
    """
    for i in range(200, 300):
        first_sum = find_sum_of_divisors(i)
        second_sum = find_sum_of_divisors(first_sum)
        if i == second_sum and i != first_sum and i == min(i, first_sum):
            return i, first_sum


task_560 = Task(
    name="task_560",
    description=
    """
    Finds sum of divisors of given number and the sum of divisors of first sum.
    If second sum == number returns this pair.
    """,
    body=_task,
    test="Tasks/test_task_560.py"
)

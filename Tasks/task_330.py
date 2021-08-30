from task import Task
from task_error import TaskError


def is_prime(number: int) -> bool:
    """
    This function checks if the number is prime
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    divider = 5
    while divider * divider <= number:
        if number % divider == 0 or number % (divider + 2) == 0:
            return False
        divider += 6
    return True


def is_prime_m(mers: int, degree: int) -> bool:
    """
    This function checks if the Mersenne number is prime.
    According to Luca-Lehmer test.
    """

    mod = 4
    for index in range(degree - 2):
        l = mod**2 - 2
        mod = l % mers
    return not mod


def _task(number: int) -> list:
    if number < 1:
        raise TaskError("The 'number' argument should be greater or equal to 1")

    if number < 7:
        return []
    degree = 0
    perfect_numbers = [6]
    while True:
        degree += 1
        if not is_prime(degree):
            continue
        mers = 2**degree - 1
        suggested_perfect = 2**(degree-1) * mers
        if suggested_perfect >= number:
            break
        if is_prime_m(mers, degree):
            perfect_numbers.append(suggested_perfect)

    return perfect_numbers


task_330 = Task(
    name="task_330",
    description=
    """
    Given a natural number n, calculate all perfect numbers less it.
    """,
    body=_task,
    test="Tasks/test_task_330.py"
)
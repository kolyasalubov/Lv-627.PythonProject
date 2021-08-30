from task import Task
from task_error import TaskError

def _factorial(number: int) -> int:
    factorial = 1
    for factor in range(1, number + 1, 1):
        factorial *= factor
    return factorial


def _representable_as_product_of_three_subsequent_naturals(number: int) -> bool:
    if number % 6 != 0:
        return False
    if number < 6:
        return False
    for assumption in range(1, int(number ** (1/3)) + 3, 1):
        if assumption ** 3 - assumption == number:
            return True
    return False


def _task(number: int) -> bool:
    if number < 1:
        raise TaskError("The 'number' argument should be greater or equal to 1")
    return _representable_as_product_of_three_subsequent_naturals(_factorial(number))


task_567 = Task(
    name="task_567",
    description=
    """
    Given a natural number n, check whether it can be represented as a product of three subsequent
    natural numbers.
    """,
    body=_task,
    test=""
)

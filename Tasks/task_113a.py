from task import Task
from task_error import TaskError


def _task(number: int) -> int:
    if number < 1:
        raise TaskError("The 'number' argument should greater or equal to 1")
    factorial = 1
    for factor in range(1, number + 1, 1):
        if (number % 2 == 0 and factor % 2 == 0) or\
                (number % 2 == 1 and factor % 2 == 1):
            factorial *= factor
    return factorial


task_113a = Task(
    name="task_113a",
    description=
    """
    Given a natural number n, calculate n!!, which is defined as the product of all natural numbers
    that are less or equal n, and have same parity as n.
    """,
    body=_task,
    test="Tasks/test_task_113a.py"
)

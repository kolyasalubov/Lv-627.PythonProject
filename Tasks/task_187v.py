from task import Task
from math import sqrt
from task_error import TaskError


def _task(number: int) -> int:
    """
    Calculate quantity of numbers that are squares of even numbers in list given by number n(a1, ..., an).
    """
    if number < 1:
        raise TaskError
    numbers = [i for i in range(1, number + 1)]
    counter = len([i for i in numbers if sqrt(i) % 2 == 0 and i >= 1])
    return counter


task_187v = Task(
    name="task_187v",
    description=
    """
    Calculate quantity of numbers that are squares of even numbers in list given by number n(a1, ..., an).
    """,
    body=_task,
    test="Tasks/test_task_187v.py"
)

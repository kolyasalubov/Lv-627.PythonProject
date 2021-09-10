from task import Task
from typing import List
from math import sqrt


def _task(numbers: List[int]) -> int:
    """
    Calculate quantity of numbers that are squares of even numbers in given list of natural number.
    """
    counter = len([i for i in numbers if sqrt(i) % 2 == 0 and i >= 1])
    return counter


task_187v = Task(
    name="task_187v",
    description=
    """
    Calculate quantity of numbers that are squares of even numbers in given list of natural number.
    """,
    body=_task,
    test="Tasks/test_task_187v.py"
)

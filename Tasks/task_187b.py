from task import Task
from typing import List


def _task(numbers: List[int]) -> int:
    """
    Calculate quantity of numbers that are divisible by 3 and 5 in given list of natural number.
    """
    counter = len([i for i in numbers if i % 3 == 0 and i % 5 == 0 and i >= 1])
    return counter


task_187b = Task(
    name="task_187b",
    description=
    """
    Calculate quantity of numbers that are divisible by 3 and 5 in given list of natural number.
    """,
    body=_task,
    test="Tasks/test_task_187b.py"
)

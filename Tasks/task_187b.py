from task import Task
from task_error import TaskError


def _task(number: int) -> int:
    """
    Calculate quantity of numbers that are divisible by 3 and 5 in list given by number n(a1, ..., an).
    """
    if number < 1:
        raise TaskError
    numbers = [i for i in range(1, number + 1)]
    counter = len([i for i in numbers if i % 3 == 0 and i % 5 == 0])
    return counter


task_187b = Task(
    name="task_187b",
    description=
    """
    Calculate quantity of numbers that are divisible by 3 and 5 in list given by number n(a1, ..., an).
    """,
    body=_task,
    test="Tasks/test_task_187b.py"
)


from task import Task
from math import gcd
from task_error import TaskError


def _task(number: int) -> list:
    """
    Check if numbers are coprime.
    :param number: int
    :return: list of all coprime numbers less than n
    """
    if number is not None:
        return [i for i in range(1, number) if gcd(i, number) == 1]
    raise TaskError("Try again.")


task_323 = Task(
    name="task_323",
    description=
    """
    Check if numbers are coprime and returns list of all less than n.
    """,
    body=_task,
    test="Tasks/test_task_323.py"
)

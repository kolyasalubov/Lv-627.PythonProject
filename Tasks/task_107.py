from math import log
from task_error import TaskError

from task import Task


def _task(m: int) -> int:
    """
    Given integer m > 1. Find the greatest integer k, that inequality 4^k < m is right.
    """
    if m <= 1:
        raise TaskError("m should be greater than 1")
    k = int(log(m, 4))
    if pow(4, k) == m:
        k -= 1

    return k


task_107 = Task(
    name="task_107",
    body=_task,
    description="""
        Given integer m > 1. Find the greatest integer k, that inequality 4^k < m is right.
        """,
    test="Tasks/test_task_107.py"
)

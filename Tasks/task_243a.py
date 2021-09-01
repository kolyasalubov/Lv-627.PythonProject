from math import sqrt
from task_error import TaskError

from task import Task


def _task(n: int) -> str:
    """
    Given natural number n. Can we represent it as the sum of two squares of natural numbers?
    If possible, then find a pair x, y of such natural numbers that n = x^2 + y^2
    """

    if n < 1:
        raise TaskError("n should be greater or equal to 1")

    n_sqrt = sqrt(n)

    for y in range(1, int(n_sqrt) + 1):
        x = sqrt((n_sqrt + y) * (n_sqrt - y))

        if int(x) == x:
            if int(x) > 0:
                return f"Pair of x, y: {int(x), y}"

        elif abs(round(x) - x) < 0.0000000001:
            if round(x) > 0:
                return f"Pair of x, y: {round(x), y}"

    return "There is no pair of such x, y"


task_243a = Task(
    name="task_243a",
    body=_task,
    description=
    """Given natural number n. Can we represent it as the sum of two squares of natural numbers?
    If possible, then find a pair x, y of such natural numbers that n = x^2 + y^2""",
    test="Tasks/test_task_243a.py"
)

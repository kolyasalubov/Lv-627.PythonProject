from math import sqrt
from task_error import TaskError

from task import Task


def _task(n: int) -> str:
    """
    Given natural number n. Can we represent it as the sum of two squares of natural numbers?
    If possible, then find all pairs x, y of such natural numbers that n = x^2 + y^2, x >= y.
    """

    if n < 1:
        raise TaskError("n should be greater or equal to 1")

    n_sqrt = sqrt(n)

    squares = []

    for y in range(1, int(n_sqrt) + 1):
        x = sqrt((n_sqrt + y) * (n_sqrt - y))

        if int(x) == x:
            if int(x) >= y:
                squares.append((int(x), y))

        elif abs(round(x) - x) < 0.0000000001:
            if round(x) >= y:
                squares.append((round(x), y))

    if len(squares) == 0:
        return "There is no pairs of such x, y"

    return f"Pair(s) of x,y: {squares}"


task_243b = Task(
    name="task_243b",
    body=_task,
    description=
    """
    Given natural number n. Can we represent it as the sum of two squares of natural numbers?
    If possible, then find all pairs x, y of such natural numbers that n = x^2 + y^2, x >= y.
    """,
    test="Tasks/test_task_243b.py"
)

from task import Task
from task_error import TaskError


def _task(n: int, m: int) -> list:
    if n < 1 or m < 1:
        raise TaskError("The arguments must be greater or equal to 1")
    lg, sm = max(n, m), min(n, m)
    return [i for i in range(lg, n * m, lg) if i % sm == 0 and i < m * n]


task_226 = Task(
    name="task_226",
    description=
    """
    Task 226. Given two natural numbers m and n. Find all less than mn natural common multiples.
    """,
    body=_task,
    test="Tasks/test_task_226.py"
)

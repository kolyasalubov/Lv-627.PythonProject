from task import Task
from task_error import TaskError


def _task(n: int, m: int) -> int:
    if n < 1 or m < 1:
        raise TaskError("The arguments must be greater or equal to 1")
    s = str(n)
    return sum([int(s[len(s) - i - 1]) for i in range(m)]) if len(s) >= m else sum([int(str(i)) for i in s])


task_087 = Task(
    name="task_087",
    description=
    """
    Task 87. Given natural n, m. Calculate the sum of m last digits of the number n.
    """,
    body=_task,
    test="Tasks/test_task_87.py"
)

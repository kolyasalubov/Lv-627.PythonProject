from Tasks.task_331a import quadratic_sum
from task import Task


def _task(n: int) -> str:
    """
    Given a natural number n, find all possible combinations of a, b and c such that a^2 + b^2 + c^2 = n, if there is
    any.
    """
    return "\n".join(quadratic_sum(n))


task_331b = Task(
    name="task_331b",
    description=
    """
    Given a natural number n, find all possible combinations of a, b and c such that a^2 + b^2 + c^2 = n, if there is 
    any.
    """,
    body=_task,
    test="Tasks/test_task_331b.py"
)

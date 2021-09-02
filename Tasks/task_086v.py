from task import Task
from task_error import TaskError


def _task(value : int) -> int:
    if value < 1:
        raise TaskError("The 'number' argument should be greater or equal to 1")
    return int(value.__str__()[0])


task_086v = Task(
    name="task_086v",
    description=
    """
    Given a natural number n, find first digit of number n
    """,
    body=_task,
    test="Tasks/test_task_086v.py"
)
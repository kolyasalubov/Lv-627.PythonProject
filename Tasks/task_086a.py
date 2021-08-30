from task import Task
from task_error import TaskError


def _task(number: int) -> int:
    if number < 1:
        raise TaskError(
            "The 'number' argument should be greater or equal to 1")
    return len(str(number))


task_086a = Task(
    name="task_086a",
    description=
    """
    Given a natural number, calculate the number of digits in number.
    """,
    body=_task,
    test="Tasks/test_task_086a.py"
)

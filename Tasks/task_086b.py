from task import Task
from task_error import TaskError


def _task(number: int) -> int:
    if number < 1:
        raise TaskError(
            "The 'number' argument should be greater or equal to 1")
    return sum(int(digit) for digit in str(number))


task_086b = Task(
    name='task_086b',
    description=
    """
    Given a natural number, calculate the sum of all digits in number.
    """,
    body=_task,
    test="Tasks/test_task_086b.py"
)

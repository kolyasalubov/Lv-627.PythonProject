from task import Task

def _task(n: int) -> int:
    """
    Given a natural number n, find smallest possible number k, that is k^4 > n.
    """
    binary_n = f"{n:b}"
    return int(f'1{"0" * len(binary_n)}', 2)


task_108 = Task(
    name="task_108",
    description=
    """
    Given a natural number n, find smallest possible number k, that is k^4 > n.
    """,
    body=_task,
    test="Tasks/test_task_108.py"
)

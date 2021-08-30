from task import Task


def _task(n: int) -> str:
    """"
    Given a natural number n. Find is 3 a digit of number n^2.
    """
    m = n * n  # number n^2
    if str(m).find('3') > -1:
        return f"3 is a digit of number {n}^2 = {m}"
    return f"3 is not a digit of number {n}^2 = {m}"


task_088a = Task(
    name="task_088a",
    body=_task,
    description="""
    Given a natural number n. Find is 3 a digit of number n^2.
    """,
    test="Tasks/test_task_088a.py"
)

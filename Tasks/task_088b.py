from task import Task


def _task(n: int) -> str:
    """
    Given a natural number n. Change the order of digits of n by reversing its digits.
    """
    n = str(n)
    return f"Reversed number = {int(n[::-1])} "


task_088b = Task(
    name="task_088b",
    body=_task,
    description = """
Given a natural number n. Change the order of digits of n by reversing its digits.
Enter natural number (0 < natural number <= +∞): """,
    test="Tasks/test_task_088b.py"
)

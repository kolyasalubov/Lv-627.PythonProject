from task import Task


def _task(n: int, m: int) -> int:
    """Task 87. Given natural n, m. Calculate the sum of m last digits of the number n."""
    print("Task 87. Given natural n, m. Calculate the sum of m last digits of the number n.")
    s = str(n)
    return sum([int(s[len(s) - i - 1]) for i in range(m)]) if len(s) >= m else sum([int(str(i)) for i in s])


task_87 = Task(
    name="task_87",
    body=_task,
    test="Tasks/test_task_87.py"
)

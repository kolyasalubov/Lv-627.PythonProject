from task import Task


def _task(n: int, m: int) -> list:
    """Task 226. Given two natural numbers m and n. Find all less than mn natural common multiples."""
    print("Task 226. Given two natural numbers m and n. Find all less than mn natural common multiples.")
    lg, sm = max(n, m), min(n, m)
    return [i for i in range(lg, n * m, lg) if i % sm == 0 and i < m * n]


task_226 = Task(
    name="task_226",
    body=_task,
    test="Tasks/test_task_226.py"
)

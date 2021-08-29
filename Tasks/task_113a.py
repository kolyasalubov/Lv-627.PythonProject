from task import Task


def _task(number: int) -> int:
    factorial = 1
    for factor in range(1, number + 1, 1):
        if (number % 2 == 0 and factor % 2 == 0) or\
                (number % 2 == 1 and factor % 2 == 1):
            factorial *= factor
    return factorial


task_113a = Task(
    name="task_113a",
    body=_task,
    test="Tasks/test_task_113a.py"
)

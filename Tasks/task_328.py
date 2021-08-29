from typing import List
from task import Task


def _is_prime(number: int) -> bool:
    for factor in range(2, int(number ** (1/2)) + 1, 1):
        if number % factor == 0:
            return False
    return True


def _find_first_count_prime(count: int) -> List[int]:
    result = []
    current = 2
    while len(result) < count:
        if _is_prime(current):
            result.append(current)
        current += 1
    return result


def _task() -> List[int]:
    return _find_first_count_prime(100)


task_328 = Task(
    name="task_328",
    body=_task,
    test="Tasks/test_task_328.py"
)

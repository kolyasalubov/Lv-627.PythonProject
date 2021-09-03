from task import Task
from typing import List
from task_error import TaskError

def prime_number(num : int) -> bool:
    if num > int(num ** 0.5) + 1:
        return False
    count = 0
    for x in range(1, num + 1):
        if num % x == 0:
            count += 1
    if count <= 2:
        return True
    else:
        return False

def _task(n : int) -> List[int]:
    if n < 1:
        raise TaskError("The 'number' argument should be greater or equal to 1")
    list_values = []
    for x in range(1, n + 1):
        if n % x == 0 and prime_number(x) == True:
            list_values.append(x)

    return list_values


task_325 = Task(
    name="task_325",
    description=
    """
    Given a natural number n, find all Prime number divisors of number n
    """,
    body=_task,
    test="Tasks/test_task_325.py"
)

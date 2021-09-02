from task import Task
from typing import List
from typing import Tuple


def _task(number: int) -> List[Tuple[int, int, int]]:
    pythagorean_triples = []
    for c in range(number):
        for b in range(c):
            for a in range(b):
                if a ** 2 + b ** 2 == c ** 2:
                    pythagorean_triples.append((a, b, c))
    return pythagorean_triples


task_554 = Task(
    name="task_554",
    description=
    """
    Find all pythagorean triple that are lower than given natural number.
    """,
    body=_task,
    test="Tasks/test_task_554.py"
)

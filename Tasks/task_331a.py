from task import Task

def quadratic_sum(n: int) -> tuple:
    for i in range(int(n**0.5)):
        for j in range(i, int(n**0.5)):
            for k in range(j, int(n**0.5)):
                if i**2 + j**2 + k**2 == n:
                    yield i, j, k


def _task(n: int) -> str:
    """
    Given a natural number n, find a, b and c such that a^2 + b^2 + c^2 = n, if there is any.
    """
    result = quadratic_sum(n)
    if len(result) == 3:
        return f"a={result[1]}, b={result[2]}, c={result[3]}"
    else:
        return "There is no such a, b and c"


task_331a = Task(
    name="task_331a",
    description=
    """
    Given a natural number n, find a, b and c such that a^2 + b^2 + c^2 = n, if there is any.
    """,
    body=_task,
    test="Tasks/test_task_331a.py"
)

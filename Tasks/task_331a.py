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
    try:
        result = next(quadratic_sum(n))
    except StopIteration:
        return "There is no such a, b and c"
    else:
        return f"a={result[0]}, b={result[1]}, c={result[2]}"



task_331a = Task(
    name="task_331a",
    description=
    """
    Given a natural number n, find a, b and c such that a^2 + b^2 + c^2 = n, if there is any.
    """,
    body=_task,
    test="Tasks/test_task_331a.py"
)

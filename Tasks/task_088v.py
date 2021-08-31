from task import Task

def _task(n: int) -> int:
    """
    Given a natural number n, swap first and last digits of this number
    """
    n = str(n)
    answer = f"{n[-1]}{n[1:-1]}{n[0]}" if len(n) > 1 else n
    return int(answer)


task_088v = Task(
    name="task_088v",
    body=_task,
    description="""
    Given a natural number n, swap first and last digits of this number 
    """,
    test="Tasks/test_task_088v.py"
)
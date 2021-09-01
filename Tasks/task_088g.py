from task import Task

def _task(n: int) -> int:
    """
    Given a natural number n, assign ones to the beginning and the end of this number
    """
    return int(f'1{n}1')


task_088g = Task(
    name="task_088g",
    body=_task,
    description="""
    Given a natural number n, assign ones to the beginning and the end of this number
    """,
    test="Tasks/test_task_088g.py"
)
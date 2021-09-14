from task import Task
from task_error import TaskError


def _task(number: int) -> str:
    """Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition ak < (ak-1 + ak+1)/2"""

    n = []
    if number is not None and number > 1:
        for i in range(1, number + 1):
            n.append(i)
        result = len([1 for i in range(1, len(n) - 1) if n[i] < (n[i - 1] + n[i + 1]) / 2])
        return result
    elif number == 1:
        return "You sequence contains only 1 element"
    else:
        raise TaskError


task_178d = Task(
    name="task_178d",
    description="""Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition ak < (ak-1 + ak+1)/2""",
    body=_task,
    test="Tasks/test_task_178d.py"
)

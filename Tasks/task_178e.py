from task import Task
from task_error import TaskError


def _task(number:int) -> str:
    """Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition 2**k < ak-1 < k!"""
    n = []
    if number > 1:
        for i in range(1, number+1):
            n.append(i)
        result = len([1 for i in range(1, len(n) - 1) if 2 ** int(n[i]) < n[i - 1] < factorial([i])])
        return f"There is {result} numbers in row which satisfy the condition 2**k < ak-1 < k!"
    elif number == 1:
        return "You sequence contains only 1 element"
    else:
        raise TaskError

task_178e = Task(
    name="task_178e",
    description="""Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition 2**k < ak-1 < k!""",
    body=_task,
    test="Tasks/test_task_178e.py"
)

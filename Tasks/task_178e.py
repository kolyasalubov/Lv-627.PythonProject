from task import Task

def _task(*args) -> str:
    """Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition 2**k < ak-1 < k!"""
    n = args
    result = len([1 for i in range(1, len(n) - 1) if 2 ** int(n[i]) < n[i - 1] < factorial([i])])
    return f"There is {result} numbers in row {n} which satisfy the condition"

task_178e = Task(
    name="task_178e",
    description="""Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition 2**k < ak-1 < k!""",
    body=_task,
    test="Tasks/test_task_182.py"
)


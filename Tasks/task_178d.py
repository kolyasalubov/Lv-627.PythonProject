from task import Task

def _task(*args) -> str:
    """Given list n: a1, ..., an. Get a quantity
                               of numbers ak of the sequence a1, ..., an,
                               which satisfy the condition 2**k < ak-1 < k!"""
    n = args
    result = len([1 for i in range(1, len(n) - 1) if n[i] < (n[i - 1] + n[i + 1]) / 2])
    return f"There is {result} digits in sequence {n} which satisfy this condition"

task_178d = Task(
    name="task_178d",
    description="""Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition 2**k < ak-1 < k!
                """,
    body=_task,
    test="Tasks/test_task_182.py"
)

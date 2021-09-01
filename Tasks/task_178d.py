from task import Task


def _task(number: int) -> str:
    """Given list n: a1, ..., an. Get a quantity
                           of numbers ak of the sequence a1, ..., an,
                           which satisfy the condition ak < (ak-1 + ak+1)/2"""
    n = []
    for i in range(1, number + 1):
        n.append(i)
    if len(n) == 1:
        return "You have given only 1 argument"
    elif len(n) > 1:
        result = len([1 for i in range(1, len(n) - 1) if n[i] < (n[i - 1] + n[i + 1]) / 2])
        return f"There is {result} digits in given sequence which satisfy the condition ak < (ak-1 + ak+1)/2"
    else:
        return "No arguments were given"


task_178d = Task(
    name="task_178d",
    description="""Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition ak < (ak-1 + ak+1)/2""",
    body=_task,
    test="Tasks/test_task_182.py"
)


print(_task(10000))
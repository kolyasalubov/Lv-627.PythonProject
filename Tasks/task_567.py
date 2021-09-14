from task import Task
from task_error import TaskError

def factorialof(value : int) -> int:
    result = 1
    for x in range(1, value + 1):
        result *= x
    return result

def _task(n : int) -> bool:
    if n < 1:
        raise TaskError("The 'number' argument should be greater or equal to 1")
    if n % 6 != 0:
        return False
    if n < 6:
        return False
    listofnum = []
    for x in range(1, factorialof(n) + 1):
        listofnum.append(x)
    for i in range(len(listofnum) - 2):
        res = listofnum[i] * listofnum[i+1] * listofnum[i+2]
        if factorialof(n) == res :
            return True
    return False


task_567 = Task(
    name="task_567",
    description=
    """
    Given a natural number n, find out whether you can write n! as muliplication of three consequtive numbers
    """,
    body=_task,
    test="Tasks/test_task_567.py"
)
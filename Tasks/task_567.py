from task import Task

def factorialof(value):
    result = 1
    for x in range(1, value + 1):
        result *= x
    return result

def _task(n):
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
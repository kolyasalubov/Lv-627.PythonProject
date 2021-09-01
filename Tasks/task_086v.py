from task import Task


def _task(value: int) -> str:
    if value > 0:
        string_value = str(value)
        list_values = []
        for x in string_value:
            list_values.append(int(x))
        return str(list_values[0])
    else:
        return 'Enter Natural number!'


task_086v = Task(
    name="task_086v",
    description=
    """
    Given a natural number n, find first digit of number n
    """,
    body=_task,
    test="Tasks/test_task_086v.py"
)
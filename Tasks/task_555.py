from task import Task

def _task (number: int) -> list:
    results = []
    for _ in range(number):
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(i) for i in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)
    value = [i for i in results]
    return value


task_555 = Task(
    name="task_555",
    description="",
    body=_task,
    test="Tasks/test_task_555.py"

)

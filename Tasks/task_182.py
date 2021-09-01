from task import Task
from task_error import TaskError


def _task(number: int) -> str:
    """Check members of a given sequence if they are divisible by 5 and not divisible by 7.
    Returns their number and sum."""
    sum_of_numbers = 0
    count_of_numbers = 0
    if number is not None and number > 1:
        for i in range(1, number + 1):
            if i % 5 == 0 and i % 7 != 0:
                sum_of_numbers += i
                count_of_numbers += 1
        return ("In sequence 1...{0} is {1} members that are divisible by 5 "
                "and not divisible by 7 and their sum is {2}").format(number, count_of_numbers, sum_of_numbers)
    elif number == 1:
        return "Your sequence contains one element."
    raise TaskError("Try again.")


task_182 = Task(
    name="task_182",
    description=
    """
    Check members of a sequence 1... number if they are divisible by 5 and not divisible by 7.
    Returns their number and sum.
    """,
    body=_task,
    test="Tasks/test_task_182.py"
)

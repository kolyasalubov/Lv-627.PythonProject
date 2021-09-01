from task import Task
from typing import List


def _is_armstrong_number(number: int) -> bool:
    return number == sum(int(x) ** 3 for x in list(number.__str__()))


def find_all_two_to_four_digit_armstrong_numbers() -> List[int]:
    return [x for x in range(100, 10000, 1) if _is_armstrong_number(x)]


task_562 = Task(
    name="task_562",
    body=find_all_two_to_four_digit_armstrong_numbers,
    description=
    """
    Find all two-, three- and four-digit armstrong numbers.
    A number is an armstrong number if sum of its digits cubed are equal to the number itself.
    """,
    test="test_task_562"
)

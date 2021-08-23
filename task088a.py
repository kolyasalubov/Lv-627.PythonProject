from validation import *
# 88. Given a natural number n.
#     а) Find is 3 a digit of number n^2.


def find_three_in_record_of_m(self, task: str = "088a") -> str:
    n = int(input_natural_number())
    m = n * n
    if str(m).find('3') > -1:
        return f"3 is a digit of number {n}^2 = {m}"
    return f"3 is not a digit of number {n}^2 = {m}"

from validation import *
# 88. Given a natural number n.
#     б) Change the order of digits of n by reversing its digits.


def reverse_n(self, task: str = "088b") -> str:
    n = input_natural_number()
    n = str(n)
    # if n[0] == '-':
    #     return int(n[:0:-1]))
    return f"Reversed number = {int(n[::-1])} "

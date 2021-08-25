from math import sqrt
from task import Task


class Task088a(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given a natural number n. Find is 3 a digit of number n^2."

    def solve(self) -> str:
        n = self.arg
        m = n * n    # number n^2
        if str(m).find('3') > -1:
            return f"3 is a digit of number {n}^2 = {m}"
        return f"3 is not a digit of number {n}^2 = {m}"


class Task088b(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given a natural number n. Change the order of digits of n by reversing its digits."

    def solve(self) -> str:
        n = self.arg
        n = str(n)
        return f"Reversed number = {int(n[::-1])} "     # print new number like reversed string


class Task322(Task):
    def __init__(self):
        super().__init__()
        self.description = "Find natural number from 1 to 10 000 with the largest sum of divisors."
        self.require_input = False

    def solve(self) -> str:
        count = [0] * 10001  # create a list for final sum of divisors of every number
        for n in range(1, 10001):
            i = int(1)
            sum_of_counts = []  # list for all divisors of number
            while i <= int(sqrt(n)):
                if n % i == 0:
                    # if divisors are different, we can add both of them
                    sum_of_counts.append(i + n / i)
                i = i + 1
            if n == int(sqrt(n)) * int(sqrt(n)):  # if we had same divisors, we can remove duplicate
                sum_of_counts.append(-int(sqrt(n)))
            count[n] = int(sum(sum_of_counts))  # write sum to the list where index is our result number
        max_value = max(count)
        return f"Natural number {count.index(max_value)} has the largest sum of divisors {max_value}"
        # Natural number 9240 has the largest sum of divisors 34560 (64 divisors)

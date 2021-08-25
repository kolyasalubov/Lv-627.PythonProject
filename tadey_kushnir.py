from task import Task
from math import log, sqrt


class Task107(Task):
    def __init__(self):
        super().__init__()
        self.description = "107. Given integer m > 1. Find the greatest integer k, that inequality 4^k < m is right."

    def solve(self):
        m = self.arg
        k = int(log(m, 4))

        if pow(4, k) == m:
            k -= 1

        return f"k = {k} (4^{k} < {m})"


class Task243a(Task):
    def __init__(self):
        super().__init__()
        self.description = "243 a.) Given natural number n. Can we represent it as the sum of two squares" \
                           " of natural numbers?  If possible, then find a pair x, y of such natural numbers " \
                           "that n = x^2 + y^2"

    def solve(self):
        n = self.arg
        n_sqrt = sqrt(n)

        for y in range(1, int(sqrt(n)) + 1):
            x = sqrt((n_sqrt + y)*(n_sqrt - y))

            if int(x) == x:
                if int(x) > 0:
                    return int(x), y

            elif abs(round(x) - x) < 0.0000000001:
                if round(x) > 0:
                    return round(x), y

        return "There is no pair of such x, y"


class Task243b(Task):
    def __init__(self):
        super().__init__()
        self.description = "243 b.) Given natural number n. Can we represent it as the sum of two squares" \
                           " of natural numbers?  If possible, then find all pairs x, y of such natural numbers " \
                           "\nthat n = x^2 + y^2, x >= y."

    def solve(self):
        n = self.arg
        n_sqrt = sqrt(n)

        squares = []

        for y in range(1, int(sqrt(n)) + 1):
            x = sqrt((n_sqrt + y)*(n_sqrt - y))

            if int(x) == x:
                if int(x) >= y:
                    squares.append((int(x), y))

            elif abs(round(x) - x) < 0.0000000001:
                if round(x) >= y:
                    squares.append((round(x), y))
                    
        if len(squares) == 0:
            return "There is no pairs of such x, y"

        return squares


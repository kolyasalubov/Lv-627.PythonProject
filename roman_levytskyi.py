from math import sqrt
from task import Task


class Task554(Task):
    def __init__(self):
        super().__init__()
        self.description = "Find all pythagorean triples that lower than input natural number n"

    def solve(self):
        n = self.arg
        pythagorean_triples = []
        for c in range(n):
            for b in range(c):
                for a in range(b):
                    if a ** 2 + b ** 2 == c ** 2:
                        pythagorean_triples.append((a, b, c))
        return pythagorean_triples


class Task187b(Task):
    def __init__(self):
        super().__init__()
        self.description = "Find all numbers that are divided by 3 and 5 in input list of natural numbers"

    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        counter = len([i for i in n if i % 3 == 0 and i % 5 == 0 and i >= 1])
        return counter


class Task187c(Task):
    def __init__(self):
        super().__init__()
        self.description = "Count how many numbers are squares of even number in input list of natural numbers"

    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        counter = len([i for i in n if sqrt(i) % 2 == 0])
        return counter

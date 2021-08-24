from math import sqrt
from task import Task


class Task554(Task):
    def init(self):
        super()
        self.description = "Find all pythagorean triples that lower than input natural number n"

    def solve(self):
        n = self.arg
        pythagorean_triples = []
        for c in range(n):
            for b in range(c):
                for a in range(b):
                    if a ** 2 + b ** 2 == c ** 2:
                        pythagorean_triples.append((a, b, c))
        return f"List of all pythagorean_triples below natural number {n} are:\n{pythagorean_triples}"


class Task187b(Task):
    def init(self):
        super()
        self.description = "Find all numbers that are divided by 3 and 5 in input list of natural numbers"

    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        counter = len([i for i in n if i % 3 == 0 and i % 5 == 0 and i >= 1])
        return f"There is {counter} numbers that are divided by 3 and 5 in list of natural numbers:\n{n}"


class Task187c(Task):
    def init(self):
        super()
        self.description = "Count how many numbers are squares of even number in input list of natural numbers"

    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        counter = len([i for i in n if sqrt(i) % 2 == 0])
        return counter
from task import Task


class Task108(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given natural number n, find the smallest number of type 2^r, bigger than n."

    def solve(self):
        binary = f"{self.arg:b}"
        return int(f'1{"0" * len(binary)}', 2)


class Task331(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given natural number n, find all possible combinations of x, y and z, if any, " \
                           "that x^2 + y^2 + z^2 = n"

    def solve(self):
        result = []
        for i in range(int(self.arg ** 0.5)):
            for j in range(i, int(self.arg ** 0.5)):
                for k in range(j, int(self.arg ** 0.5)):
                    if i ** 2 + j ** 2 + k ** 2 == self.arg:
                        result.append((i, j, k))
        return result if result else None

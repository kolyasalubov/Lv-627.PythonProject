from task import Task


class Task87(Task):
    def __init__(self):
        super().__init__()
        self.second_arg = None
        self.description = "Task 87. Given natural n, m. Calculate the sum of m last digits of the number n."

    def change_arguments(self, arg, second_arg):
        self.arg = arg
        self.second_arg = second_arg

    def solve(self):
        s, m = str(self.arg), self.second_arg
        return sum([int(s[len(s)-i-1]) for i in range(m)]) if len(s) >= m else sum([int(str(i)) for i in s])


class Task226(Task):
    def __init__(self):
        super().__init__()
        self.second_arg = None
        self.description = "Task 226. Given two natural numbers m and n. Find all less than mn natural common multiples"

    def change_arguments(self, arg, second_arg):
        self.arg = arg
        self.second_arg = second_arg

    def solve(self):
        n, m = self.arg, self.second_arg
        lg, sm = max(n, m), min(n, m)
        return [i for i in range(lg, n*m, lg) if i % sm == 0 and i < m*n]


class Task559(Task):
    def __init__(self):
        super().__init__()
        self.description = "Task 559. A natural number n is given. Find all less than n Mersenne prime numbers."

    def get_prime_numbers(self) -> list:
        """Returns a list of prime numbers from 3 to n."""
        array = []
        n = self.arg
        for num in range(3, n + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                array.append(num)
        return array

    def solve(self) -> list:
        primes = self.get_prime_numbers()
        array, i = [], 2
        while 1:
            x = 2 ** i - 1
            if x > primes[-1]:
                break
            if x in primes:
                array.append(x)
            i += 1
        return array

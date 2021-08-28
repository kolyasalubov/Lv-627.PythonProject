from math import gcd
from task import Task


class Task182(Task):
    def __init__(self):
        super().__init__()
        self.description = "Check members of a given sequence if they are divisible by 5 and not divisible by 7."

    def solve(self):
        number = self.arg
        sum_of_numbers = 0
        count_of_numbers = 0
        if number is not None and number > 1:
            for i in range(1, number+1):
                if i % 5 == 0 and i % 7 != 0:
                    sum_of_numbers += i
                    count_of_numbers += 1
            return ("In sequence 1...{0} is {1} members that are divisible by 5 "
                "and not divisible by 7 and their sum is {2}").format(number, count_of_numbers, sum_of_numbers)
        elif number == 1:
            print("Your sequence contains one element.")


class Task560(Task):
    def __init__(self):
        super().__init__()
        self.description = "Find all pairs of friendly numbers between 200 and 300"
        self.require_input = False

    @staticmethod
    def find_sum_of_divisors(number):
        """Returns sum of all divisors of the number."""
        sum_of_divisors = 0
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i
        return sum_of_divisors

    def solve(self):
        for i in range(200, 300):
            first_sum = Task560.find_sum_of_divisors(i)
            second_sum = Task560.find_sum_of_divisors(first_sum)
            if i == second_sum and i != first_sum and i == min(i, first_sum):
                return i, first_sum


class Task323(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given natural n. Get all natural coprime numbers less than n."

    def solve(self):
        number = self.arg
        if number is not None:
            return [i for i in range(1, number) if gcd(i, number) == 1]


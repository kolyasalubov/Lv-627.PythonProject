from task import Task


class Task086a(Task):
    def __init__(self):
        super()
        self.description = "Given natural number, find the the number of digits in it"
    
    def change_arguments(self, arg):
        if int(arg) == 0:
            raise ValueError()
        super().change_arguments(arg)

    def solve(self):
        return len(str(self.arg))

class Task086b(Task086a):
    def __init__(self):
        super()
        self.description = "Given natural number, find the the sum of it's digits"

    def solve(self):
        return sum(int(digit) for digit in str(self.arg))

class Task330(Task086a):
    def __init__(self):
        super()
        self.description = "Given natural number, find all perfect numbers smaller it"
        
    @staticmethod
    def is_prime(number):
        """
        This method checks if the number is prime
        """
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        divider = 5
        while divider * divider <= number:
            if number % divider == 0 or number % (divider+ 2) == 0:
                return False
            divider += 6
        return True


    @staticmethod
    def is_prime_mers(mers, degree):
        """
        This method checks if the Mersenne number is prime.
        According to Luca-Lehmer test.
        """

        mod = 4
        for index in range(degree - 2):
            l = mod**2 - 2
            mod = l % mers
        return not mod


    def solve(self):
        """
        This function returns all perfect numbers less limit
        """
        limit = self.arg

        if limit < 7:
            return []
        degree = 0
        perfect_numbers = [6]
        while True:
            degree += 1
            if not self.is_prime(degree):
                continue
            mers = 2**degree - 1
            suggested_perfect = 2**(degree-1) * mers
            if suggested_perfect >= limit:
                break
            if self.is_prime_mers(mers, degree):
                perfect_numbers.append(suggested_perfect)

        return perfect_numbers

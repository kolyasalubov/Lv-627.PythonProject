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
        This function checks if the number is prime
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

    def solve(self):
        degree = 1
        perfect_numbers = []
        while True:
            multiplier1 = 2**degree
            multiplier2 = 2**(degree+1) - 1
            suggested_number = multiplier1 * multiplier2
            if suggested_number >= self.arg:
                break
            if self.is_prime(multiplier2):
                perfect_numbers.append(suggested_number)
            degree += 1
        return perfect_numbers

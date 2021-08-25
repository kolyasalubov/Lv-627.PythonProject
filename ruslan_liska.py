from task import Task
from math import factorial

class Task555(Task):
    def __init__(self):
        super().__init__()
        self.description = "Given digit is n, get n rows of Pascal's triangle"
    
    
    def solve(self):

        num_of_rows = self.arg
        results = []
        for _ in range(num_of_rows): 
            row = [1]
            if results: 
                last_row = results[-1] 
                row.extend([sum(i) for i in zip(last_row, last_row[1:])])
                row.append(1)
            results.append(row) 
        # for i in results:
        value = [i for i in results]
    
        return f"Here is your Pascal's Triangle: {value}"

class Task178d(Task):
    def __init__(self):
        super().__init__()
        self.description = """Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition ak < (ak-1 + ak+1)/2"""
    
    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        result = len([1 for i in range(1, len(n) - 1) if n[i] < (n[i - 1] + n[i + 1]) / 2])  
        return f"There is {result} digits which satisfy this condition"

class Task178e(Task):
    def __init__(self):
        super().__init__()
        self.description = """Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition 2**k < ak-1 < k!"""

    def change_arguments(self, *args):
        self.args = args

    def solve(self):
        n = self.args
        result = len([1 for i in range(1, len(n) - 1) if 2 ** int(n[i]) < n[i - 1] < factorial([i])])
        return f"There is {result} numbers which satisfy the condition"

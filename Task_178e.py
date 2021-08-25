from task import Task
from math import factorial

class Task178e(Task):
    def __init__(self):
        super()
        self.description = """Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition 2**k < ak-1 < k!"""

    def solver(self, n):
        self.n = n
        return len([1 for i in range(1, len(n) - 1) if 2 ** n[i] < n[i - 1] < factorial([i])])

a = Task178e()
print(a.solver([1,2,34,5,6,7,0,8]))
from task import Task

class Task178d(Task):
    def __init__(self):
        super()
        self.description = """Given list n: a1, ..., an. Get a quantity 
                           of numbers ak of the sequence a1, ..., an, 
                           which satisfy the condition ak < (ak-1 + ak+1)/2"""

    def solver(self, n):
        self.n = n
        return len([1 for i in range(1, len(n) - 1) if n[i] < (n[i - 1] + n[i + 1]) / 2])

a = Task178d()
print(a.solver([1,2,34,5,6,7,0,8]))
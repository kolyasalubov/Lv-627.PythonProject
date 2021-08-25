from task import Task

class Task555(Task):
    def __init__(self):
        super()
        self.description = "Given digit is n, get n rows of Pascal triangle"
    
    
    def solve(self, num_of_rows):
        self.num_of_rows = num_of_rows
        results = []
        for _ in range(num_of_rows): 
            row = [1]
            if results: 
                last_row = results[-1] 
                row.extend([sum(i) for i in zip(last_row, last_row[1:])])
                row.append(1)
            results.append(row) 
        for i in results:
            print(i)

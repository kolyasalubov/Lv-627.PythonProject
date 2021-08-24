n = int(input("Please enter the quantity of triangle rows: "))
def pascals_triangle(n):
    results = []
    for _ in range(n): 
        row = [1]
        if results: 
            last_row = results[-1] 
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row) 
    for i in results:
        print(i)

pascals_triangle(n)
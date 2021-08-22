@console_input
def quadratic_sum(n=1):
    for i in range(int(n**0.5)):
        for j in range(i, int(n**0.5)):
            for k in range(j, int(n**0.5)):
                if i**2 + j**2 + k**2 == n:
                    yield i, j, k


def console_input(func):
    def wrapper(*args):
        n = input("Enter a number: ")
        task = input("Which task? ")
        if n.isdigit() and task == "a":
            return tuple(func(int(n)))[0]
        elif n.isdigit() and task == "b":
            return tuple(func(int(n)))
        else:
            return tuple(func())


if __name__ == "__main__":
    print(quadratic_sum())

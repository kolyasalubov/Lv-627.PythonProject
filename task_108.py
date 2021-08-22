@console_input
def task_108(n=1):
    s = f"{n:b}"
    return int(f'1{"0"*len(s)}', 2)


def console_input(func):
    def wrapper(*args):
        n = input("Enter a number: ")
        if n.isdigit():
            return func(int(n))
        else:
            return func()


if __name__ == "__main__":
    print(smallestbin())

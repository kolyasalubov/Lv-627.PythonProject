from task import Task


def get_prime_numbers(n: int) -> list:
    """Returns a list of prime numbers from 3 to n."""
    array = []
    for num in range(3, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            array.append(num)
    return array


def _task(n: int) -> list:
    """Task 559. A natural number n is given. Find all less than n Mersenne prime numbers."""
    print("Task 559. A natural number n is given. Find all less than n Mersenne prime numbers.")
    primes = get_prime_numbers(n)
    array, i = [], 2
    while 1:
        x = 2 ** i - 1
        if x > primes[-1]:
            break
        if x in primes:
            array.append(x)
        i += 1
    return array


task_559 = Task(
    name="task_559",
    body=_task,
    test="Tasks/test_task_559.py"
)

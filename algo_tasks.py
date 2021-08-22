def enter_until_int(letter):
    """
    User inputs data until ts is a natural integer.
    Returns an integer.
    """
    while 1:
        x = input("Please, enter a natural number {}: ".format(letter))
        if isinstance(x, int):
            return x
        print('You have not entered a natural number. Please, try again.')


def task_87():
    print('Task 87. Given natural n, m. Calculate the sum of m last digits of the number n.')
    """Calculates the sum of m last digits of the number n."""
    n = enter_until_int('n')
    m = enter_until_int('m')
    s = str(n)
    return sum([int(s[len(s)-i-1]) for i in range(m)]) if len(s) >= m else sum([int(str(i)) for i in s])


def task_226():
    """Returns a list of all less than mn natural common multiples."""
    print('Task 226. Given two natural numbers m and n. Find all less than mn natural common multiples.')
    n = enter_until_int('n')
    m = enter_until_int('m')
    lg, sm = max(n, m), min(n, m)
    return [i for i in range(lg, n*m, lg) if i % sm == 0 and i < m*n]


def get_prime_numbers():
    """Returns a list of prime numbers from 3 to n."""
    array = []
    n = enter_until_int('n')
    for num in range(3, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            array.append(num)
    return array


def task_559():
    """Returns Mersenne prime numbers."""
    print('Task 559. A natural number n is given. Find all less than n Mersenne prime numbers.')
    primes = get_prime_numbers()
    array, i = [], 2
    while 1:
        x = 2 ** i - 1
        if x > primes[-1]:
            break
        if x in primes:
            array.append(x)
        i += 1
    return array

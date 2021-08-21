# 322. Find natural number from 1 to 10 000 with
# the largest sum of divisors
from math import sqrt


def max_sum_of_divisors(self, task: str = "322") -> str:
    count = [0] * 10001    # create a list for final sum of divisors of every number
    for n in range(1, 10001):
        i = int(1)
        sum_of_counts = []    # list for all divisors of number
        while i <= int(sqrt(n)):
            if n % i == 0:
                # if divisors are different, we can add both of them
                sum_of_counts.append(i + n / i)
            i = i + 1
        if n == int(sqrt(n))*int(sqrt(n)):    # if we had same divisors, we can remove duplicate
            sum_of_counts.append(-int(sqrt(n)))
        count[n] = int(sum(sum_of_counts))    # write sum to the list where index is our result number
    max_value = max(count)
    return f"Natural number {count.index(max_value)} has the largest sum of divisors {max_value}"
    # Natural number 9240 has the largest sum of divisors 34560 (64 divisors)

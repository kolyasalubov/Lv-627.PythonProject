from __init__ import *


if __name__ == '__main__':
    res = Tasks()
    number_of_task = str(input("Enter the number of task from the list: 088a, 088b, 322: "))
    if number_of_task == "088a":
        print(res.find_three_in_record_of_m(number_of_task))
    elif number_of_task == "088b":
        print(res.reverse_n(number_of_task))
    else:
        print(res.max_sum_of_divisors(number_of_task))

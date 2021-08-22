from additional_functions import is_positive_integer


def task_086b():
    """
    This function calculate the sum of all digits in positive integer.
    """

    print(task_086b.__doc__.strip())
    positive_integer_input = input('Enter positive integer: ')

    if not positive_integer_input:
        print('You entered no characters.')
    elif is_positive_integer(positive_integer_input):
        digits_sum = sum(int(digit) for digit in positive_integer_input)
        print(f'The sum of all digits in {positive_integer_input} is {digits_sum}')
    else:
        print(f'"{positive_integer_input}" is not positive integer.')
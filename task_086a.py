from additional_functions import is_positive_integer


def task_086a():
    """
    This function counts the number of digits in positive integer.
    """

    print(task_086a.__doc__.strip())
    positive_integer_input = input('Enter positive integer: ')

    if not positive_integer_input:
        print('You entered no characters.')
    elif is_positive_integer(positive_integer_input):
        number_of_digits = len(positive_integer_input)
        plural = 's' if number_of_digits > 1 else ''
        print(f'It\'s {number_of_digits} digit{plural} in {positive_integer_input}')
    else:
        print(f'"{positive_integer_input}" is not positive integer.')
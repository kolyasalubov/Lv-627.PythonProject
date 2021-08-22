def is_positive_integer(string):
    """
    This function checks is the string positive integer
    """

    return string.isdecimal() and string[0] != '0'
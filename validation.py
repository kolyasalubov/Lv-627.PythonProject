def input_natural_number() -> int:
    number = input("Enter a natural number n: ")
    if str(number).isdigit() and float(number) == int(number) and int(number) > 0:
        return int(number)
    else:
        print("Wrong input. 0 < natural number <= +∞. Please, try again")
        input_natural_number()

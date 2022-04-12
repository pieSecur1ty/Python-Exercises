# function for calculating factoial
def calculate_factorial(number):
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number - 1
    return factorial


# check strong number
def check_strong_number(number):
    temp = number
    total = 0
    while number > 0:
        last_digit = number % 10
        total = total + calculate_factorial(last_digit)
        number = number // 10
    number = temp

    if number == total:
        print(f"{number} is a strong number.")
    else:
        print(f"{number} is not a strong number.")


# user input and output
input_number = int(input("Enter the number : "))
check_strong_number(input_number)

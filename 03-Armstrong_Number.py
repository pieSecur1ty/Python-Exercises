# import modules
import math


# user input
input_number = int(input("Enter the number : "))


# opration
def check_armstrong(number):
    temp = number
    total = 0
    while number > 0:
        last_digit = number % 10
        total = total + math.pow(last_digit, 3)
        number = number // 10

    number = temp
    if number == total:
        print(f"{number} is an armstrong number.")
    else:
        print(f"{number} is not an armstrong number.")


# output
check_armstrong(input_number)

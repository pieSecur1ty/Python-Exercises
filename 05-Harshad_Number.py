# function for checking harshad number
def check_harshad_number(number):
    temp = number
    total = 0
    while number > 0:
        last_digit = number % 10
        total = total + last_digit
        number = number // 10

    number = temp
    if number % total == 0:
        print(f"{number} is a harshad number.")
    else:
        print(f"{number} is not a harshad number.")


# input and output
check_harshad_number(int(input("Enter the number : ")))

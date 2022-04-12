# function for getting LCM
def get_lcm(number1, number2):
    for value in range(number1, (number1 * number2) + 1):
        if (value % number1 == 0) and (value % number2 == 0):
            print(f"LCM of {number1} and {number2} is {value}.")
            break


# user input & output
input_number1 = int(input("Enter the first number : "))
input_number2 = int(input("Enter the second number : "))

get_lcm(input_number1, input_number2)

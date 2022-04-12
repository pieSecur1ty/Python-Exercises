# function for calculating HCF or GCD
def calculate_HCF(number1, number2):
    hcf = 1
    minimum = min(number1, number2)
    for value in range(2, minimum + 1):
        if (number1 % value == 0) and (number2 % value == 0):
            hcf = value
    return hcf


# user input & output
input_number1 = int(input("Enter the first number : "))
input_number2 = int(input("Enter the second number : "))

result = calculate_HCF(input_number1, input_number2)
print(f"HCF or GCD of {input_number1} and {input_number2} is : {result}")

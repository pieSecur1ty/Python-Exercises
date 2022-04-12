# Function to check palindrome number
def check_palindrome(number):
    reverse_number = 0
    temp = number
    while number > 0:
        last_digit = number % 10
        reverse_number = (reverse_number * 10) + last_digit
        number = number // 10
    number = temp
    if number == reverse_number:
        print(f"{number} is a palindrome number.")
    else:
        print(f"{number} is not a palindrome number.")


# user input and output
number1 = int(input("Enter the number : "))
check_palindrome(number1)

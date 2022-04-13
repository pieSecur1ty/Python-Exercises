# function for fizz buzz operation
def fizz_buzz(number):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# user input and output
fizz_buzz(int(input("Enter the number : ")))

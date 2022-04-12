# Function to check the number is prime or not
def check_prime(number):
    flag = 1
    for value in range(2, number):
        if number % value == 0:
            flag = 0
            break
    if flag == 1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


# user input & output
check_prime(int(input("Enter the number : ")))

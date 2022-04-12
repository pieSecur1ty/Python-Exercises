# function for getting the fibonacci  series upto a number of elements
def get_fibonacci_series(items):
    first_element = 0
    second_element = 1
    if items == 1:
        print(first_element)
    elif items == 2:
        print(first_element)
        print(second_element)
    else:
        print(first_element)
        print(second_element)
        for value in range(3, items + 1):
            next_element = first_element + second_element
            print(next_element)
            first_element = second_element
            second_element = next_element


# input and output
print("<----- Fibonacci Series ----->")
get_fibonacci_series(int(input("Enter the number : ")))

# function for printing the fibonacci series upto the highest given value
def print_fibonacci_series(highest_value):
    first_item = 0
    second_item = 1
    print(first_item)
    print(second_item)
    while highest_value > 0:
        next_item = first_item + second_item
        first_item = second_item
        second_item = next_item
        if next_item <= highest_value:
            print(next_item)
        else:
            break


# input & output
print_fibonacci_series(int(input("Enter the upper limit : ")))

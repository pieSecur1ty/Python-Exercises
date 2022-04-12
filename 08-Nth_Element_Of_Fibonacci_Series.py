# function for getting Nth element of a fibonacci series
def get_nth_element(n):
    data = [0, 1]
    if n <= 2:
        print(f"{n} th element of fibonacci series is : {data[n - 1]}")
    else:
        for index in range(2, n):
            next_item = data[index - 1] + data[index - 2]
            data.append(next_item)
        print(f"{n} th element of fibonacci series is : {data[n - 1]}")


# input and output
get_nth_element(int(input("Enter the value of N : ")))

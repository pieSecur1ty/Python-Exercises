# user input
number_of_items = int(input("Enter the number of items : "))
items = []
for index in range(number_of_items):
    items.append(int(input(f"Enter number {index + 1} : ")))


# find out the lonely integer
lonely_elements = []
single_items = list(set(items))
for element in single_items:
    count_element = items.count(element)
    if count_element == 1:
        lonely_elements.append(element)
    else:
        pass


# output
print("<--- Here, the lonely elements are --->")
print(' '.join(map(str, lonely_elements)))

# user input
number_of_items = int(input("Enter the number of items : "))
items = []
for index in range(number_of_items):
    items.append(int(input(f"Enter number {index + 1} : ")))


# counting sort operation
zero_items = [0] * (max(items) + 1)
sigle_items = list(set(items))
for element in sigle_items:
    element_repetation = items.count(element)
    zero_items[element] = element_repetation


# output
print(f"<--- The counting sort of items --->")
print(' '.join(map(str, zero_items)))

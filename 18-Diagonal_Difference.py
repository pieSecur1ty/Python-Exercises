# import modules
import sys


# user input
input_rows = int(input("Enter the number of rows : "))
input_columns = int(input("Enter the number of columns : "))

matrix = []
if input_rows == input_columns:
    print("<--- Enter the values of matrix --->")
    for row in range(input_rows):
        rows = []
        for column in range(input_columns):
            rows.append(int(input(f"Value at matrix ({row}, {column}) : ")))
        matrix.append(rows)

else:
    print("The matrix should be a 'Square Matrix'.\ni.e. Number of rows & columns must be matched.")
    sys.exit()


# finding the absolute value of diagonal difference
first_diagonal_sum = 0
second_diagonal_sum = 0
for row in range(input_rows):
    first_diagonal_sum += matrix[row][row]
    second_diagonal_sum += matrix[row][input_columns - 1 - row]

diagonal_difference = abs(first_diagonal_sum - second_diagonal_sum)


# output
print(f"First diagonal sum : {first_diagonal_sum}")
print(f"Second diagonal sum : {second_diagonal_sum}")
print(f"The absolute value of diagonal diference is : {diagonal_difference}")

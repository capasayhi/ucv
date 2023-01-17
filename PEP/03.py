"""
Perform a program that generates a list of lists, emulating an array of order NxM, with N and M
given by the user. Suppose this matrix is filled with the horizontal zig-zag shape according to the sequence that
shown in the example:
                            1  2  3
                            6  5  4
                            7  8  9
                            12 11 10
 """

from functions import integerValidation, createBaseMatrix


print("This is a matrix generator program with random values\n")

rows = integerValidation(input("Enter the number of rows: "))

cols = integerValidation(input("Enter the number of columns: "))

matriz = createBaseMatrix(rows)

# To fill the matrix whit the correct values
counter = 1
for index in range(len(matriz)):
    for item in range(cols):
        matriz[index].append(counter)
        counter += 1
    # Depending on the parity of the row, the values are reversed
    if index % 2 != 0:
        matriz[index].reverse()
print(matriz)

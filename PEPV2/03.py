"""
Perform a program that generates a list of lists, emulating an array of order NxN, with N par
given by the user. Suppose that this array is filled in the shape shown in the example:

                                    1  2  3  4  5  6
                                    13 14 15 16 17 18
                                    25 26 27 28 29 30
                                    31 32 33 34 35 36
                                    19 20 21 22 23 24
                                    7  8  9 1 0 11 12


"""

from functions import integerValidation, createBaseMatrix

order = integerValidation(
    input("Enter the N of the square array (order NxN): "))

matriz = createBaseMatrix(order)

# Fill the rows with the number of values as indicated by the order
counter = 1
for row in range(len(matriz)):
    print("\nrow", row)
    controler = 0
    for column in range(order):

        if row == 1:
            controler = -1
            print("controler", controler)
        elif row >= 2:
            controler = (controler - 1) * -1
        print("controler", controler)

        matriz[controler].append(counter)
        counter += 1
    # if row % 2 != 0:
    #   matriz[row].reverse()
print(matriz)
print("\n")

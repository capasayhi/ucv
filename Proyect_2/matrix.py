import numpy as np
# https: // numpy.org/doc/stable/reference/index.html    / reference for the library

from modules.algebra import matrixMultiplication, inversionOfMatrix, crossProduct, transpose, linealSist

print('Avaliable operations for matrix are\n  \tMultiplication (m)\n \tInversion of matrices (i)\n \Cross product (c)\n \tTransposition of matrices (t)\n \tSystem resolution of linear equations (s)\n')

operation = input('What operation do you want to perform?: ')

if operation == 'm':
    print('\nTo first matrix (A)')
    ra = int(input("Enter the number of rows:"))
    ca = int(input("Enter the number of columns:"))

    # User input of entries in a single line separated by space
    print("Enter the entries in a single line (separated by space): ")
    entriesA = list(map(int, input().split()))
    A = np.array(entriesA).reshape(ra, ca)

    print('\nTo second matrix (B)')
    rb = int(input("Enter the number of rows:"))
    cb = int(input("Enter the number of columns:"))
    orderA = tuple((ra, ca))
    orderB = tuple((rb, cb))
    print("Enter the entries in a single line (separated by space): ")
    entriesB = list(map(int, input().split()))
    B = np.array(orderB).reshape(rb, cb)

    C = matrixMultiplication(entriesA, orderA, entriesB, orderB)
    print(f"Result Matrix (C):\n {C}\n")


elif operation == 'i':
    print('\nTo matrix (M)')
    r = int(input("Enter the number of rows:"))
    c = int(input("Enter the number of columns:"))

    # User input of entries in a single line separated by space
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    M = np.array(entries).reshape(r, c)
    print(f"Matrix (M):\n {M}\n")

    I = inversionOfMatrix(M)
    print(f'Inversion of Matrix ( M^-1 ): \n {I}\nl')

elif operation == 'c':

    # User input of entries in a single line separated by space
    print("Enter the entries of the first vector in a single line (separated by space): ")
    entriesX = list(map(int, input().split()))
    if len(entriesX) < 2 or len(entriesX) > 3:
        raise NameError(
            'Incompatible dimensions for cross product, dimension must be 2 or 3')
    else:
        X = np.array(entriesX)

        print("Now the entries of the other vector: ")
        entriesY = list(map(int, input().split()))
        if len(entriesY) < 2 or len(entriesY) > 3:
            raise NameError(
                'Incompatible dimensions for cross product, dimension must be 2 or 3')
        else:
            Y = np.array(entriesY)
            cross = crossProduct(X, Y)
            print(f'Cross product of: {X} , {Y} is\n', cross)

elif operation == 't':

    print('\nTo matrix (A)')
    ra = int(input("Enter the number of rows:"))
    ca = int(input("Enter the number of columns:"))

    # User input of entries in a single line separated by space
    print("Enter the entries in a single line (separated by space): ")
    entriesA = list(map(int, input().split()))

    if len(entriesA) < ra*ca or len(entriesA) > ra*ca:
        raise NameError(
            f'Invalid input, must enter {ra*ca} values')
    else:
        A = np.array(entriesA).reshape(ra, ca)
        transpose = transpose(A)
        print(f'Transpose of: \n\n{A} \n\nis\n\n', transpose)

elif operation == 's':
    order = int(input('Enter the order of the coeficients matrix: '))
    print(order**2)
    print("Enter the entries of coeficients matrix in a single line (separated by space): ")
    entriesC = list(map(int, input().split()))
    if len(entriesC) < order ** 2 or len(entriesC) > order ** 2:
        raise NameError(
            f'Invalid input, must enter {order**2} values')
    else:
        coeficientsMatrix = np.array(entriesC).reshape(order, order)
        print(f"Coeficients matrix:\n {coeficientsMatrix}\n")
        print("Enter the entries of results in a single line (separated by space): ")
        entriesR = list(map(int, input().split()))
        if len(entriesR) < order or len(entriesR) > order:
            raise NameError(
                f'Invalid input, it must be at least {order} values')
        else:
            results = np.array(entriesR).reshape(order, 1)
        print(results)
        R = linealSist(coeficientsMatrix, results)
        print(f'Result of the system of linear equations  : \n\n{R}')
else:
    raise NameError('Invalid input, check the character you are typing')

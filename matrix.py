import numpy as np
# https: // numpy.org/doc/stable/reference/index.html    / reference for the library

from modules.algebra import matrixMultiplication, inversionOfMatrix

print('Avaliable operations for matrix are\n  \tMultiplication (m)\n \tInversion of matrices (i)\n \tVector product (p)\n \tTransposition of matrices (t)\n \tSystem resolution of linear equations (s)\n')

operation = input('What operation do you want to perform?: ')

# generate 2 matrix of random values
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 2))
print(f"Matrix A:\n {A}\n")
print(f"Matrix B:\n {B}\n")

C = matrixMultiplication(A, B)
print(f"Result Matrix (C):\n {C}\n")

I = inversionOfMatrix(A)
print(f'Inversion of A:\n {I}\nl')

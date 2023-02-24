import numpy as np
# https: // numpy.org/doc/stable/reference/index.html    / reference for the library


def matrixMultiplication(A, B):
    global C
    if A.shape[1] == B.shape[0]:  # Validates if A has as many columns as B has rows
        C = np.array([[sum(r*c for r, c in zip(rowsMatrixA, columnsMatrixB)) for columnsMatrixB in zip(*B)]
                      for rowsMatrixA in A])
        return C
    else:
        return "Ups! cannot multiply A and B. Check the order of the matrices."


def inversionOfMatrix(M):
    if M.shape[0] == M.shape[1]:
        try:
            I = np.linalg.inv(M)
            return I
        except:
            raise NameError("Check the order of the matrices.")

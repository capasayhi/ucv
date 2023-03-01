import numpy as np
# https: // numpy.org/doc/stable/reference/index.html    / reference for the library


def matrixMultiplication(A, B):
    if A.shape[1] == B.shape[0]:  # Validates if A has as many columns as B has rows
        C = np.array([[sum(r*c for r, c in zip(rowsMatrixA, columnsMatrixB)) for columnsMatrixB in zip(*B)]
                      for rowsMatrixA in A])
        return C
    else:
        raise NameError(
            "Ups! cannot multiply A and B. Check the order of the matrices.")


def inversionOfMatrix(m):
    I = []
    M = np.array(m)
    if M.shape[0] == M.shape[1]:
        I = np.linalg.inv(M)
        return I
    else:
        raise NameError("Check the order of the matrices.")


def crossProduct(x, y):
    X = np.array(x)
    Y = np.array(y)
    product = np.cross(X, Y)
    return product


def transpose(m):
    M = np.array(m)
    transpose = M.transpose()
    return transpose


def linealSist(A, B):  # (Coeficients matrix, Results list)

    if A.shape[1] == B.shape[0]:
        X = np.linalg.inv(A).dot(B)
        return X
    else:
        raise NameError("Check the order of the matrices.")

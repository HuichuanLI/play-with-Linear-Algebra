from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero


def LU(matrix):
    assert matrix.row_number() == matrix.col_number(), "must be a square list"

    n = matrix.row_number()

    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):

        if is_zero(A[i][i]):
            return None, None

        for j in range(i + 1, n):
            p = A[j][i] / A[i][i]
            L[j][i] = p
            A[j] = A[j] - p * A[i]

    return Matrix(L), Matrix([A[i].underlying_list() for i in range(n)])

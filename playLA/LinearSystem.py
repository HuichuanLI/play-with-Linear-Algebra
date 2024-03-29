from .Vector import Vector
from ._global import is_zero


class LinearSystem:

    def __init__(self, A, b):
        assert A.row_number() == len(b), "row number of A must be equal to the length of b"
        self._m = A.row_number()
        self._n = A.col_number()
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]
        self.pivots = []

    def _max_row(self, index_i, index_j, n):
        best, ret = self.Ab[index_i][index_j], index_i
        for index in range(index_i + 1, n):
            if self.Ab[index][index_j] > best:
                best = self.Ab[index][index_j]
                ret = index

        return ret

    def _forward(self):
        n = self._m
        i, k = 0, 0

        while i < self._m and k < self._n:
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k = k + 1
            else:
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, n):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

        for i in range(len(self.pivots),self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])

from .Vector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def row_vector(self, index):
        return Vector(self._values[index])

    def col_vector(self, index):
        return Vector([row[index] for row in self._values])

    def shape(self):
        return len(self._values), len(self._values[0])

    def size(self):
        r, c = self.shape()
        return r * c

    def row_number(self):
        return self.shape()[0]

    def col_number(self):
        return self.shape()[1]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    def __getitem__(self, item):
        r, c = item
        return self._values[r][c]

    def __add__(self, other):
        assert self.shape() == other.shape(), "the shape of two matrix must be same"
        return Matrix(
            [[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_number())])

    def __sub__(self, other):
        assert self.shape() == other.shape(), "the shape of two matrix must be same"
        return Matrix(
            [[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_number())])

    def __mul__(self, k):
        return Matrix([[k * a for a in self.row_vector(i)] for i in range(self.row_number())])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return (-1) * self

    def T(self):
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_number())])

    @classmethod
    def zero(cls, r, c):
        return cls([[0] * c for _ in range(r)])

    def dot(self, another):
        if isinstance(another, Vector):
            assert self.col_number() == len(another), "error"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_vector())])
        if isinstance(another, Matrix):
            assert self.col_number() == another.row_number(), "error"
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(self.col_number())] for i in
                           range(self.row_number())])

    @classmethod
    def identity(cls,n):
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    __str__ = __repr__
    __len__ = row_number

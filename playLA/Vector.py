# -*- coding: utf-8 -*-
import math
from ._global import EPSILON
from ._global import is_equal


class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """零向量"""
        return cls([0] * dim)

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("there is error")
        return Vector(self._values) / self.norm()

    def underlying_list(self):
        return self._values[:]

    def __add__(self, another):
        assert len(another) == len(self), " Error in adding. Length must be same"
        return Vector([a + b for a, b, in zip(self, another)])

    def __sub__(self, another):
        assert len(another) == len(self), " Error in adding. Length must be same"
        return Vector([a - b for a, b, in zip(self, another)])

    def __iter__(self):
        return self._values.__iter__();

    def __getitem__(self, item):
        return self._values[item]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "vector({})".format(self._values)

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果向量：self / k"""
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        other_list = other.underlying_list()

        if len(other_list) != len(self._values):
            return False
        return all(is_equal(x,y) for x,y in zip(self._values,other_list))

    def __neq__(self,other):
        return not(self == other)

    def dot(self, another):
        assert len(another) == len(self), "the dimension should be same"
        return sum(a * b for a, b in zip(self, another))

class Vector:

    def __init__(self, lst):
        self._values = list(lst)

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

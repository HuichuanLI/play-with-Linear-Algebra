
from playLA.Vector import Vector

u = Vector([5, 2])

u2 = Vector([3, 4])

print("{} + {} = {}".format(u,u2,u+u2))

print("{} * {} = {}".format(2,u,u*2))

print("-{} = {}".format(u,-u))

zero3 = Vector.zero(3)

print("{}".format(zero3))
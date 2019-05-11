
from playLA.Vector import Vector

u = Vector([5, 2])

u2 = Vector([3, 4])

print("{} + {} = {}".format(u,u2,u+u2))

print("{} * {} = {}".format(2,u,u*2))

print("-{} = {}".format(u,-u))

zero3 = Vector.zero(3)

print("{}".format(zero3))


print("norm({}) = {}".format(u,u.norm()))
print("normzlize({}) = {}".format(u,u / 3))

print("{}*{} = {}".format(u,u2,u.dot(u2)))

print(u[1:])
try:
    zero3.normalize()
except ZeroDivisionError:
    print("Cannot normalize zero vector{}".format(zero3))



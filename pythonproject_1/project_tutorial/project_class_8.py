# objective :
#           -take two inputs and perform addition, subtraction, multiplication, division,
#            also find the modulus(remainder), square, cube of the number, square root, x to the power y
x = 27
y = 9

# addition
print("addition:", x + y)
add = x + y
print("sum of", x, "and", y, "is", add)

output = "sum of " + str(x) + " and " + str(y) + " is " + str(add)
print(output)

#  subtraction
print("subtractio:", x - y)
sub = x - y
print("subtraction of", x, "and", y, "is", sub)

output = "sub of " + str(x) + " and " + str(y) + " is " + str(sub)
print(output)

# [TODO] - MULTIPLICATION

# divsion
print("division:", x / y)
print("division:", x // y)
print("division:", int(x / y))

div = x / y
output = "division of " + str(x) + " and " + str(y) + " is " + str(int(div))
print(output)

# modulus(also known as remainder, also known as mod)
print("mod:", x % y)
#[TODO] - modulus complete

# square of a number
print("square of", x, "is", x * x)
print("squareof", x, "is", x ** 2)
output = "square of " + str(x) + " is " + str(x * x)
print(output)
print("square of", y, "is", y * y)
output = "square of " + str(y) + " is " + str(y * y)
print(output)

# [TODO] - cube


# x to the power y
print("x to the power y", x ** y)

# [TODO] - COMPLETE X TO THE POWER Y

# SQUARE ROOT

import math


print("square root of", y, "is", int(math.sqrt(y)))

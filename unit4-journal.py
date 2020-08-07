import math


# import the math module so we can use the sqrt function

def hypotenuse(a, b):
    # finds hypotenuse of a right triangle using the Pythagorean Theorem
    return math.sqrt(a ** 2 + b ** 2)


# adding some test prints to confirm if working properly
print("Test Output for Function 'hypotenuse':")
print("Result of hypotenuse(3,4):", hypotenuse(3, 4))
print("Result of hypotenuse(2,3):", hypotenuse(2, 3))
print("Result of hypotenuse(7,9):", hypotenuse(7, 9))

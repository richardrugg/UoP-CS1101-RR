import math


# import the math module so we can use the sqrt function
def right_triangle_area(a, b, c):
    # finds the area of a triangle when the length of all 3 sides are known
    # a & b are sides, c is hypotenuse
    if a + b > c and a > 0 and b > 0 and c > 0:
        # a + b > c to be a valid triangle, no value may be zero
        return .25 * math.sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))
        # returns none if invalid


# added scaffolding print functions for testing area calculation
print("right_triangle_area(0,2,1) output:\n", right_triangle_area(0, 2, 1))
print("right_triangle_area(1,1,3) output:\n", right_triangle_area(1, 1, 3))
print("right_triangle_area(1,2,3) output:\n", right_triangle_area(1, 2, 3))
print("right_triangle_area(1,3,3) output:\n", right_triangle_area(1, 3, 3))
print("right_triangle_area(4,7,5) output:\n", right_triangle_area(4, 7, 5))
print("right_triangle_area(7,9,3) output:\n", right_triangle_area(7, 9, 3))

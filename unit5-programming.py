import math


def my_sqrt(a):
    x = a + 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y


def test_sqrt(a, z):
    # test square root starting from a to z

    while True:
        print("a = ", a, " | ", "my_sqrt(a) = ", my_sqrt(a), " | ", "math.sqrt(a) = ", math.sqrt(a), " | ", "diff = ",
              abs(my_sqrt(a) - math.sqrt(a)), "\n")
        if a == z:
            break
        a = a + 1


test_sqrt(1, 25)

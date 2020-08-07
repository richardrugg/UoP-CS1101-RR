def is_between(x, y, z):
    # is y between or equal to x and z?
    if x <= y <= z:
        return True
    else:
        return False


def is_divisible(x, y):
    # is x divisible by y?
    if x % y == 0:
        return True
    else:
        return False


def is_power(a, b):
    # is a power of b?
    if a == 1 and b == 1:
        # 1 is a power of 1 and a special case
        # this is here to avoid infinite recursion for a & b = 1
        return True
    elif b == 1:
        # 1 is the only power of 1
        # this avoids false positives for this special value
        return False
    elif is_divisible(a, b) == 1 and is_power(a / b, b) == 0:
        return True
    else:
        return False


# test cases to exercise the is_power function
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

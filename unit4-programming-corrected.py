def is_divisible(x, y):
    # is x divisible by y?
    if x % y == 0:
        return True
    else:
        return False


def is_power(a, b):
    # is a power of b?
    if a < 1 or b < 1:
        return False
    elif a == b:
        return True
    elif b == 1:
        # 1 is the only power of 1
        # this avoids false positives for this special value
        return False
    elif is_divisible(a, b) is True and is_power(a / b, b) is True:
        return True
    else:
        return False


# test cases to exercise the is_power function
print("is_power(10, 2) returns: ", is_power(10, 2))  # should be False
print("is_power(27, 3) returns: ", is_power(27, 3))  # should be True
print("is_power(1, 1) returns: ", is_power(1, 1))  # should be True
print("is_power(10, 1) returns: ", is_power(10, 1))  # should be False
print("is_power(3, 3) returns: ", is_power(3, 3))  # should be True

def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


print(divide(5, (subtract(1, 1))))
# the output of the subtract function is zero
# leading the divide function to divide by zero
# while zero is a logical output of the divide function
# it's logical use outside of the function is the issue
# this also is a precondition issue for the divide function

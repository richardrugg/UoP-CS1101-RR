#  method 1 using a while loop
factorial_number = int(input("Input number to solve for factorial: "))
countup = int(1)
newsum = countup
while countup < factorial_number:
    newsum = newsum * (countup + 1)
    countup = countup + 1
print(factorial_number, " factorial is: ", newsum)

# method 2 using a range list
factorial_number2 = int(input("Input number to solve for factorial: "))
newsum2 = int(1)
for i in range(factorial_number2):
    newsum2 = newsum2 * (i + 1)
print(factorial_number2, " factorial is: ", newsum2)

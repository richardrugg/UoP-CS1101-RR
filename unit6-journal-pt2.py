#  nested list is a list inside a list, such as acctnumbers below
subacctnumbers = [100, 101, 102]
acctnumbers = [1, 2, 3, subacctnumbers]
print('subacctnumbers = ', subacctnumbers)
print('acctnumbers = ', acctnumbers)

#  the * operator repeats a list by the given amount of times
print('subacctnumbers * 2 = ', subacctnumbers * 2)

#  a list slice prases a portion of a list, by index in this example
#  note that index 3 in this example is a list itself, subacctnumbers
print('2 & 3 index values of acctnumbers = ', acctnumbers[2:4])

#  the += operator is also called an accumulator
#  a = a + b is equivalent to a += b


def acct_total_ballance(list_var):
    total = 0
    for val in list_var:
        total += val
    return total


acct_ballance = [25, 20, 10, 30]
print('total of acct_ballance = ', acct_total_ballance(acct_ballance))

#  a list filter selects some list elements, but not others based on set criteria
#  this creates a sublist out of the original elements that match the criteria


def acct_over_20(list_var):
    over20 = []
    for x in list_var:
        if x > 20:
            over20.append(x)
    return over20


print('acct_ballance elements that are over 20 = ', acct_over_20(acct_ballance))

#  legal but unexpected
#  this method does not actually add the element 60 to the actual list
#  while that would be the expected result
acct_ballance + [60]
print('acct_ballance + [60] = ', acct_ballance)

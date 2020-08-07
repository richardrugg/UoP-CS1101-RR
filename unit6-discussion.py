#  Part 1: Objects vs. Values
variable1 = 'value1'
variable2 = 'value1'
print(variable1 is variable2)

#  Part 2: Objects, References and Aliasing
list1 = ['first', 'second', 'third']
list2 = list1
print(list1)


#  Part 3: Function
list3 = ['beginning', 'middle']


def listaddend(x):
    x.append('end')


print(list3)
listaddend(list3)
print(list3)

# creating string of colors
mystring = 'red green blue yellow white black gray'
print('mystring = ', mystring)

#  converting mystring to a list using space as the delimiter using split
stringlist = mystring.split(' ')
print('stringlist = ', stringlist)

#  removing yellow by index and add it, along with 'purple' to stringlist2 using pop
stringlist2 = [stringlist.pop(3), 'purple']
print('stringlist after pop = ', stringlist)
print('stringlist2 = ', stringlist2)

#  removing gray by index using del
del stringlist[5]
print('stringlist after del = ', stringlist)

#  removing white by element using remove
stringlist.remove('white')
print('stringlist after remove = ', stringlist)

#  sorting list from low to high alphabetically using sort
stringlist.sort()
print('stringlist after being sorted = ', stringlist)

#  adding 'orange' to the end of the list using append
stringlist.append('orange')
print('stringlist after append = ', stringlist)

#  adding elements of stringlist2 to the end of stringlist using extend
stringlist.extend(stringlist2)
print('stringlist after extend stringlist2 = ', stringlist)

#  replacing black with brown by index
stringlist[0] = 'brown'
print('stringlist after replacing black with brown by index = ', stringlist)

#  joining stringlist back into a string using space as the delimiter using join
newstring = ' '.join(stringlist)
print('newstring = ', newstring)

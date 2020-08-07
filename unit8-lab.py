"""
#  open a file with a r, w, or a flag
#  r = readonly, w = write, a = append
testfile = open('test.txt', 'r')
#  print the file name
print(testfile.name)
#  print the r, w or a flag
print(testfile.mode)
#  print the contents of the file
print(testfile.read)
#  get lines of file
print(testfile.readlines()
#  get line of file, one at a time starting at beginning
print(testfile.readline()
#  close the file - required when done to avoid leaks
testfile.close()
"""
"""
#  context manager will auto close and allow you to catch exceptions
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    
    print(f.tell())
    
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
"""

with open('unit8-lab.txt', 'w') as f:
    f.write('I like cheesecake.')
prompt = 'Please enter cable size in inches, as an integer:\n'
size = input(prompt)
if int(size) == 0:
    print('Invalid Size')
else:
    if int(size) < 0:
        print('Invalid Size')
    else:
        print('Valid Size')

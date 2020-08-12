try:
    open('nonexistent_file')
except:
    print('ERROR: File Does Not Exist')

try:
    open('/etc/usr', 'w')
except:
    print('ERROR: Permission Denied')

try:
    open('/')
except:
    print('ERROR: Cannot Open Directory')

prefixes = 'JKLMNOPQ'

suffix = 'ack'
for letter in prefixes:
    if letter == "Q" or letter == "O":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

desert = 'cheesecake'
print(desert[6:])
print(desert[:6])
print(desert[4:7])

desert = 'cheesecake'
improved_desert = 'chocolate ' + desert[6:]
print(improved_desert)

desert = 'ice cream'
print(desert.upper())

"""
# ORIGINAL SAMPLE GIVEN FOR INVERTING:
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
"""

class_map = {'Core': ['ASR9K', 'NCS5501', 'NCS540'], 'Aggregate': ['ASR920', 'NCS540', 'C9500', 'ASR920'],
             'Distribution': ['ASR920', 'C9500', 'C3850', 'C4948']}
print('Original List: ', class_map)


def invert_dict(d):
    inverse = dict()
    for key in d:
        #  run through the list that is saved in the dictionary
        for item in d[key]:
            #  check if the key already exists in the inverted dictionary
            if item not in inverse:
                #  if key in inverted dictionary does not already exist, create it
                inverse[item] = [key]
            else:
                #  if key does exist, append the item to it
                inverse[item].append(key)
    return inverse


inverse_class_map = invert_dict(class_map)
print('Inverted List: ', inverse_class_map)

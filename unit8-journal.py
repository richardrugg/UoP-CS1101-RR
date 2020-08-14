import pickle

class_map = {'Core': ['ASR9K', 'NCS5501', 'NCS540'], 'Aggregate': ['ASR920', 'NCS540', 'C9500', 'ASR920'],
             'Distribution': ['ASR920', 'C9500', 'C3850', 'C4948'], 'Server': ['UCS', 'PowerEdge'], 'CPE': ['Modem', 'NIDGT'], 'VoIP': ['TG862', 'ME34xx']}

'''
#  write database to pickle file for later import
unit8_input = open('unit8-input.pkl', 'wb')
pickle.dump(class_map, unit8_input)
unit8_input.close()  # must close before read or run out of input
'''

read_class_map = pickle.load(open('unit8-input.pkl', 'rb'))
#  scaffolding print for troubleshooting
#  print('Normal Read: ', read_class_map)


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


inverse_class_map = invert_dict(read_class_map)
#  scaffolding print for troubleshooting
#  print('Inverted: ', inverse_class_map)
#  the following saves the inverted dictionary to an output pickle file
unit8_output = open('unit8-output.pkl', 'wb')
pickle.dump(inverse_class_map, unit8_output)
unit8_output.close()
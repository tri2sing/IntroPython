

if __name__ == '__main__':

    # Dict as a map from keys to values
    D1 = dict()
    D1['a'] = 1
    D1['b'] = 2
    D1['c'] = 3
    print(D1)

    D2 = {}
    D3 = {}
    start = ord('a')  # get ASCII code of character
    end = ord('z')

    # Creating a dictionary automatically and its reverse too
    for i in range(start, end+1):
        D2[i-start+1] = chr(i) # get character from ASCII code
        D3[chr(i)] = i-start+1

    # Keys are unordered, even when they appear to be, there are
    # no guarantees that the order will be the same next time
    print(D2)
    print(D3)

    # Look up a value
    print(D2[5])
    print(D3['m'])

    # Find length of dictionary
    print('The number of items in D1 = ' + str(len(D1)))
    print('The number of items in D2 = ' + str(len(D2)))

    # The in operator works for the keys by default
    print(5 in D2)
    print('a' in D3)

    # Test for presence in values
    print('p' in D2.values())
    print(17 in D3.values())

    # Using the dictionary as a histogram
    counts = {}
    s = "This is a string to test show the us of dictionaries"
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    print(counts)

    print('\n')
    # Iterate through they keys in dictionary
    for key in counts:
        print("%s: %s" % (key, counts[key]))

    print('\n')
    # Iterate through the values in dictionary
    for value in counts.values():
        print(value, end=' ')

    print('\n')
    # Iterate through the keys and values in dictionary
    for key, value in counts.items():
        print("%s: %s" % (key, value))


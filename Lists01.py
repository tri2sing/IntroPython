

if __name__ == '__main__':

    # Creating lists
    L1 = [1, 2, 3, 4]   # list of integers
    L2 = ['apple', 'banana', 'grape', 'pear']  # list of strings
    L3 = [1, 2, 3, 'hello', 'hi', 'hey']  # list of different types
    L4 = [L1, L2, L3] # list of lists

    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print('\n')

    # Accessing elements of a list -> exactly like strings
    print(L1[0])
    print(L2[2:4])
    print(L3[4])
    print(L4[2])
    print(L4[2][2])
    print('\n')

    # check if item exists in list
    print("Apple is in fruits = %r" % ('apple' in L2))
    print('\n')


    # traverse the list without worry about the indices
    for fruit in L2:
        print(fruit)
    print('\n')

    # when you care about the indices
    for i in range(len(L1)):
        L1[i] = 2*L1[i]
    print(L1)
    print('\n')


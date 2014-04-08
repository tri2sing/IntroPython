

if __name__ == '__main__':

    # Creating lists
    l1 = [1, 2, 3, 4]   # list of integers
    l2 = ['apple', 'banana', 'grape', 'pear']  # list of strings
    l3 = [1, 2, 3, 'hello', 'hi', 'hey']  # list of different types
    l4 = [l1, l2, l3] # list of lists

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print('\n')

    # Accessing elements of a list -> exactly like strings
    print(l1[0])
    print(l2[2:4])
    print(l3[4])
    print(l4[2])
    print(l4[2][2])
    print('\n')

    # check if item exists in list
    print("Apple is in fruits = %r" % ('apple' in l2))
    print('\n')


    # traverse the list without worry about the indices
    for fruit in l2:
        print(fruit)
    print('\n')

    # when you care about the indices
    for i in range(len(l1)):
        l1[i] = 2*l1[i]
    print(l1)
    print('\n')


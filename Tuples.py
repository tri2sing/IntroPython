
if __name__ == '__main__':
    # Tuple is a comma-separated set of immutabe values
    # position of values in the set is unique
    # Couple of representations: with and without parentheses
    t1 = 1, 2, 3, 4, 5
    t2 = ('a', 'b', 'c')
    print(t1)
    print(t2)
    t6 = 1, 2, 3, 5, 4
    print("t1 == t6 is " + str(t1 == t6))

    #Single element tuple creation requires comma
    t3 = 1,  #without the comma Python will consider this one as an integer
    t4 = 'a',   #without the comma Python will consider this one as a string
    t7 = tuple([1])  # Need to send an iterable to the tuple() function
    t5 = tuple('tuples') # Notice the quotes
    print(t5)
    print(t7)

    #Accessing elements in a tuple
    print(t5[3])
    print(t1[2:5])

    #Using tuples

    print('\n')
    L1 = [7, 8, 9]
    for i, v in enumerate(L1):
        print(i, v)

    print('\n')
    D1 = {'a': 1, 'b': 2, 'c': 3}
    for key, val in D1.items():
        print(key, val)

    print('\n')
    IP = '10.100.51.132'
    o1, o2, o3, o4 = IP.split(sep='.')
    print(o1, o2, o3, o4)

    print('\n')
    # You can also write functions that return multiple values
    numer = 10
    denom = 4
    quo, rem = divmod(numer, denom)
    print(numer, denom, quo, rem)

    # zip again
    # input: two or more sequences
    # output: iterator of tuples
    S1 = 'abc'
    S2 = 'ABC'
    L1 = [0, 1, 2]
    T1 = list(zip(S1, S2, L1)) # create list from iterator
    print(T1)

    # Compare tuples
    print((0, 1, 20) < (0, 3, 10))

    def retmultiple():
        """Function that returns multiple values"""
        return 'hello', 'world'

if __name__ == '__main__':

    # create set
    # empty set requires set() not {}, which is an empty dict
    S1 = set('abracadabras')
    S2 = set('openshazam')
    S3 = {1, 2, 3, 4, 5, 6, 7}
    S4 = {2, 4, 6, 7, 8, 10}
    S5 = {1, 2, 3}

    print('S1 = ' + str(S1))
    print('S2 = ' + str(S2))
    print('S3 = ' + str(S3))
    print('S4 = ' + str(S4))

    print('S1 intersection S2 = ' + str(S1 & S2))
    print('In S1 or in S2 but not both = ' + str(S1 ^ S2))
    print('In S3 but not in S4 = ' + str(S3 - S4))
    print('In S3 or in S4 = ' + str(S3 | S4))

    S1.add('z')
    print("S1 after adding 'z'= " + str(S1))
    S4.remove(2)
    print('S4 after removing 2 = ' + str(S4))

    #Iteration over set
    for item in S3:
        print(item, end=' ')

    print('\nS2 size = ' + str(len(S2)))
    print("S5 subset of S3 = " + str(S5 <= S3))
    print("S5 subset of S4 = " + str(S5 <= S4))
    print("S3 superset of S5 = " + str(S3 >= S5))


if __name__ == '__main__':
    # Dict as a sparse list
    print('\n')
    L1 = {0: 'a', 5: 'r', 10: 'z'}
    print(L1)


    # Dict as a matrix
    X = 3 # Dimensions
    Y = 3
    Z = 3
    M = {}
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                M[i, i, k] = i * j * k
    print(M)

    # Create dict from two lists using the zip function
    # Length of the dict will be equal to shorter of the two lists
    L1 = [1, 2, 3]
    L2 = ['a', 'b', 'c', 'd']
    D = dict(zip(L1, L2))
    print(L1)
    print(L2)
    print(D)


if __name__ == '__main__':
    # Dict as a sparse list
    print('\n')
    L1 = {0: 'are', 5: 'you', 99: 'home'}
    print(L1)
    print(L1[0])
    print(L1[5])
    print(L1[99])
    if 77 not in L1:
        print("Key Missing")

    # By default is you use a list
    # Then 0 -> are
    # but 1 -> you instead of our desired 5
    # and 2 -> home
    L2 = ["are", "you", "home"]

    # But if you still want to map 99 -> home
    # then you need to create a list with 100 items
    # Lists for sequential indices
    # Lists are akin to arrays in other languages

    # Dict as a matrix
    X = 3 # Dimensions
    Y = 3
    Z = 3
    M = {}
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                # Uses tuple of i, j, k as key
                M[i, j, k] = i * j * k
    print(M)

    # Create dict from two lists using the zip function
    # Length of the dict will be equal to shorter of the two lists
    L1 = [1, 2, 3]
    L2 = ['a', 'b', 'c', 'd']
    D = dict(zip(L1, L2))
    print(L1)
    print(L2)
    print(D)

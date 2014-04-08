

if __name__ == '__main__':

    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    print(L1)

    # List comprehension
    L2 = []
    for i in range(len(L1)):
        L2.append(2*L1[i])
    print(L2)

    # Multiply each element in the source list
    L3 = [2*n for n in L1]
    print(L3)

    # Multiply only the odd numbers in the source list
    L4 = [2*n for n in L1 if n%2==1]
    print(L4)

    # Get every alternate element from the source list
    # Get the ith element of source when i is even
    L5 = [L1[i] for i in range(len(L1)) if i%2==0]
    print(L5)
    L6 = [L1[i] for i in range(0, len(L1), 2)]
    print(L6)

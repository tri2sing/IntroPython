

if __name__ == '__main__':

    # Some list operations
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    print(l1)
    print(l2)

    # Concatenate
    l3 = l1 + l2
    print(l3)

    # repeat
    l4 = l1 * 3
    print(l4)
    l5 = 2 * l2
    print(l5)

    # Some list methods
    t1 = ['a', 'b', 'c']
    print(t1)
    t1.append('p')
    print(t1)
    t2 = ['e', 'f']
    t1.extend(t2)
    print(t1)
    t1.sort(reverse=True)
    print(t1)
    t1.sort()
    print(t1)

    # Deleting list elements
    # if you care about the deleted value
    x = t1.pop(3)
    print(t1)
    print(x)
    # if you don't care about the deleted value
    del t1[1]
    print(t1)
    # If you know the element but not the index
    t1.remove('f')
    print(t1)
    t1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # delete a range
    del t1[2:5]
    print(t1)

    # convert a string into list of characters
    s = "this is an unnecessary string"
    t1 = list(s)
    print(s)
    print(t1)

    # convert a string into list of words
    t2 = s.split()
    print(t2)

if __name__ == "__main__":

    items = [i for i in range(1,11)]
    print(items)

    # Map = apply the same operation to each item in an iterable
    # map ( function , sequence , [ sequence... ] ) -> iterable
    # The same can be achieved by list comprehension or a for loop

    # Using a for loop
    sqr1 = []
    for item in items:
        sqr1.append(item**2)

    # Using a list comprehension
    sqr2 = [i**2 for i in items]

    # Using a map with defined function
    def sqr(x): return x**2
    sqr3 = list(map(sqr, items))

    # Using a map with a lambda function
    sqr4 = list(map(lambda x: x**2, items))

    print(sqr1)
    print(sqr2)
    print(sqr3)
    print(sqr4)

    from math import pow

    # More advanced use of map with two iterators providing inputs
    L1 = [2, 3, 4]
    L2 = [5, 6, 7]
    L3 = list(map(pow, L1, L2))
    print(L1)
    print(L2)
    print(L3)
    L9 = [8, 9, 10]
    print(L9)
    L10 = list(map(lambda x, y, z: x + y + z ,L1, L2, L9))
    print(L10)

    # Filter = returns elements that match a criterion
    # filter(function or None, sequence) -> iterable
    def lt5(x): return x<5
    L4 = list(filter(lt5, items))
    print(L4)
    L5 = list(filter(lambda x: x < 5, items))
    print(L5)

    #Using for loop
    L7 = []
    for item in items:
        if item < 5: L7.append(item)
    print(L7)

    #using list comprehension
    L8 = [i for i in items if i < 5]
    print(L8)


    # Reduce = apply a function cumulatively to a sequence from left to right
    # reduce(function, sequence[, initial]) -> value
    from functools import reduce
    sum1 = reduce(lambda x, y: x + y, items)
    print(sum1)

    #using for loop
    sum2 = 0
    for i in items:
        sum2 += i
    print(sum2)

    # Can't think of way to use list comprehension for reduce





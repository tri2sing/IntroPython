

if __name__ == "__main__":
    dish = "szechuan chicken"

    print(dish)

    # String slices
    print(dish[0:5])
    print(dish[:4])
    print(dish[9:])
    print(dish[-8:-3])
    print(dish[:])

    # Some string methods
    print('In upper case our string is "' + dish.upper())
    print('We can find "masala" at location = ' + str(dish.find('masala')))
    print('We can find "chicken" at location = ' + str(dish.find('chicken')))
    print('Between 0 and 8 Wwe can find "chicken" at location = ' + str(dish.find('chicken', 0, 8)))

    # Another use of the 'in' operator
    flavor = 'masala'
    if flavor in dish:
        print(flavor + ' is in ' + dish)
    else:
        print(flavor + ' is not in ' + dish)

    flavor = 'szechuan'
    if flavor in dish:
        print(flavor + ' is in ' + dish)
    else:
        print(flavor + ' is not in ' + dish)

    # Comparison operators for strings
    # Useful in lexical ordering
    lessthan = 'masala chicken' < 'szechuan chicken'
    print('Less than test is ' + str(lessthan))
    equalto = 'masala chicken' == 'szechuan chicken'
    print('Equal to test is ' + str(equalto))
    greaterthan = 'masala chicken' > 'szechuan chicken'
    print('Greater than test is ' + str(greaterthan))

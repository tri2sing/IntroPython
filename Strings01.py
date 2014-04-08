
def skipper03(instr, step):
    print(instr)
    l = len(instr)
    for i in range(0, l, step):
        print(instr[i], end=' ')
    print('\n')

if __name__ == "__main__":

    # String is a sequence of characters
    dish = 'chicken masala'

    # You can use single of double quotes
    print('The string is "' + dish + '"')
    l1 = dish[0]

    # You can mix single and double quotes
    print("The first letter is '" + l1 + "'")
    l2 = dish[1]
    print("The second letter is '" + l2 + "'")

    # Length of string
    l = len(dish)
    print('The length of the string is ' + str(l))

    # One way of getting last character
    last = dish[l-1]
    print("The last letter one way is '" + last + "'")

    # Another way of getting last character
    last = dish[-1]
    print("The last letter another way is '" + last + "'")

    secondlast = dish[-2]
    print("The penultimate letter another way is '" + secondlast + "'")

    # Traverse string using index
    print('\nTraversing a string using an index')
    for i in range(l):
        print("The %dth character is '%c'" % (i, dish[i]))

    # Traverse string without using index
    print('\nTraversing a string without using an index')
    for c in dish:
        print("The character is '" + c + "'")

    # Traverse string by using enumerate
    print('\nTraversing a string using enumerate')
    for i, c in enumerate(dish):
        print("The %dth character is '%c'" % (i, c))

    skipper03("Test string for skipper", 2)
    skipper03("Test string for skipper", 3)
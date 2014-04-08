if __name__ == '__main__':
    print("The name of the module is " + __name__)
    msg = "This is my message"
    n = 97
    pi = 3.1415926535897932
    print('The type of the variables is:')
    print('msg = ' + type(msg).__name__)
    print('n = ' + str(type(n)))
    print('pi = ' + type(pi).__name__)
    print(type(30))
    print(type(n + pi))
    k = int(n + pi)
    print(k)
    print(type(k))

else:
    print("The name of the module is not __main__ but it is " + __name__)
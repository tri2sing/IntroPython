import math # import a module object
from math import pow # import a specific object from module

def conversions():
    '''Function that shows conversion of one data type to another.
    For example, and string to int, and string to float.
    '''
    s = '37'
    print('Type of ' + s + " = " + str(type(s)))
    i = int(s)
    print('Type of ' + str(i) + " = " + str(type(i)))
    f = float(s)
    print('Type of ' + str(f) + " = " + str(type(f)))

def mathematics():
    """Function that shows usage of some math functions.
    For example, sine , square root, and power.
    """
    d = 45
    r = math.pi*d/180
    s = math.sin(r)
    print("%d degrees in radians is %.4f whose sine is %0.4f" % (d, r, s))
    n = 16
    t = math.sqrt(n)
    print('The square root of %d is %.2f' % (n, t))
    n = 19
    t = math.sqrt(n)
    print('The square root of %d is %.2f' % (n, t))
    b = 2
    e = 3
    n = pow(b, e)
    print('The number %d raised to the power %d is %d' % (b, e, n))

if __name__ == '__main__':
    conversions()
    mathematics()
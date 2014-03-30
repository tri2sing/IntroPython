import math

def conversions():
    s = '37'
    print('Type of ' + s + " = " + str(type(s)))
    i = int(s)
    print('Type of ' + str(i) + " = " + str(type(i)))
    f = float(s)
    print('Type of ' + str(f) + " = " + str(type(f)))

def mathematics():
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

if __name__ == '__main__':
    conversions()
    mathematics()
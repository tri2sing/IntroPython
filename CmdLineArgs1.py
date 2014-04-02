import sys

if __name__ == '__main__':
    for i in range(len(sys.argv)):
        print('Arg %d is %s of type %s' % (i, sys.argv[i], type(sys.argv[i])))  # C-like
        print(u'Arg {0:d} is {1:s} of type {2:s}'.format(i, sys.argv[i], type(sys.argv[i])))
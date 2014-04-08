import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument ('-c', '--count', type=int, default=1, help='the number of ice cream orders')
    parser.add_argument ('-f', '--flavor', default='vanilla', help='name of the flavor to use for the order')
    parser.add_argument ('-s', '--size', default='medium', help='default size of each order')
    args = parser.parse_args()
    print(type(args))
    print("You ordered %d count of %s ice cream in %s size" % (args.count, args.flavor, args.size))
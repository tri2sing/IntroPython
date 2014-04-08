import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument ('-f', '--file', required=True, help='name of the file to read/write/append')
    parser.add_argument ('-m', '--mode', choices=['r', 'w', 'a'], default='r', help='default size of each order')
    args = parser.parse_args()

    print('You chose to open file "%s" in "%s" mode' % (args.file, args.mode))

    # The with statement allows for better handling of errors
    # Python will automatically handle exceptions and close file
    with open(args.file, args.mode) as fp:
        if args.mode == 'r':
            for line in fp:
                print(line)
        else:
            while True:
                line = sys.stdin.readline()
                print("Input = " + line)
                if not line.strip():  # remove \n
                    break
                else:
                    fp.write(line)



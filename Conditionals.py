import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--num', type=float, default=float('-inf'), help='a number of your choice')
    args = parser.parse_args()

    num = args.num

    if num == float('-inf'):
        print('You should have made a choice')
    elif num < float('inf'):
        print('Maybe should have chosen a bigger number')
    else:
        print('This condition should never be true')

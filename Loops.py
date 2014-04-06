
from sys import float_info as sfi

def square_root (n):
    '''Square root calculated using Netwton's method
    '''
    x = n/2.0
    while True:
        y = (x + n/x)/2
        # As equality in floating numbers can be elusive,
        # we check if the numbers are close to each other.
        if abs(y-x) < sfi.epsilon:
            break
        x = y

    return x

def factorial_new(n):
    '''Factorial using for loop
    '''
    result = 1
    if n < 0: return None
    if n == 0: return 1
    for i in range(1, n+1):
        result = result * i

    return result

if __name__ == "__main__":
    print("The square root of 4 = " + str(square_root(4)))
    print("The square root of 9 = " + str(square_root(9)))
    print("The square root of 15 = %.4f " % square_root(14))
    print("The factorial of 4 = " + str(factorial_new(4)))
    print("The factorial of 7 = " + str(factorial_new(7)))
    print("The factorial of 10 = %d " % factorial_new(10))


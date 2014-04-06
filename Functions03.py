'''This module shows canonical example of recursion.
'''

def factorial (n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci (n):
    if not isinstance(n, int):
        print('Fibonacci is only defined for integers.')
        return None
    elif n < 0:
        print('Fibonacci is not defined for negative integers.')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print('The factorial of 7 = ' + str(factorial(7)))
    print('The fibonacci of 7 = ' + str(fibonacci(7)))
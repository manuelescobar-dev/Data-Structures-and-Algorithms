import time


def recursive_factorial(number):
    """
    NOT RECOMMENDED
    """
    if number > 2:
        return number * recursive_factorial(number - 1)
    else:
        return number


def iterative_factorial(number):
    """
    RECOMMENDED
    """
    multiplication = number
    nxt = number - 1
    while nxt > 1:
        multiplication = multiplication * nxt
        nxt = nxt - 1
    return multiplication

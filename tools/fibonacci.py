def recursive_dynamic_fibonacci():
    """
    RECOMMENDED RECURSIVE SOLUTION
    """
    cache = {}

    def computation(N):
        if N < 2:
            return N
        else:
            if N in cache:
                result = cache[N]
            else:
                result = computation(N - 1) + computation(N - 2)
                cache[N] = result
            return result

    return computation


def recursive_fibonacci(N):
    """
    NOT RECOMMENDED
    """
    if N < 2:
        return N
    else:
        return recursive_fibonacci(N - 1) + recursive_fibonacci(N - 2)


def iterative_fibonacci(N):
    """
    RECOMMENDED
    """
    first = 0
    second = 1
    for i in range(1, N, 1):
        sum = first + second
        first, second = second, sum
    return sum

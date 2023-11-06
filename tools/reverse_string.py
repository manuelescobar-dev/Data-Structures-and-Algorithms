def recursive_reverse_string(str):
    """
    NOT RECOMMENDED
    """
    if len(str) == 2:
        return str[-1] + str[-2]
    elif len(str) == 1:
        return str
    else:
        return str[-1] + str[-2] + recursive_reverse_string(str[:-2])


def iterative_reverse_string(str):
    """
    RECOMMENDED
    """
    new = ""
    for i in range(len(str) - 1, -1, -1):
        new += str[i]
    return new

def bubble_sort(array):
    swap = False
    for i in range(len(array)):
        for j in range(1, len(array) - i, 1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swap = True
        if not swap:
            return array
        else:
            swap = False
    return array

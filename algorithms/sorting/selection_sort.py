def selection_sort(array):
    length = len(array)
    for iteration in range(length):
        min = (iteration, array[iteration])
        for i in range(iteration + 1, length):
            if array[i] < min[1]:
                min = (i, array[i])
        if min[0] != iteration:
            array[iteration], array[min[0]] = array[min[0]], array[iteration]
    return array

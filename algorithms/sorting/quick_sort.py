def quick_sort(array):
    def find_pivot(array):
        pivot = len(array) - 1
        return pivot

    def sortAtPivot(array):
        pivot = find_pivot(array)
        i = 0
        while i < pivot:
            if array[i] >= array[pivot]:
                array[i], array[pivot], array[pivot - 1] = (
                    array[pivot - 1],
                    array[i],
                    array[pivot],
                )
                pivot -= 1
            else:
                i += 1
        return array[:pivot], array[pivot + 1 :], array[pivot]

    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    else:
        left, right, pivot_value = sortAtPivot(array)
        return quick_sort(left) + [pivot_value] + quick_sort(right)

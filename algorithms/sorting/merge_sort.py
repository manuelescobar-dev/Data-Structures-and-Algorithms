def merge_sort(array):
    def divide(array):
        middle = round(len(array) / 2)
        left = array[:middle]
        right = array[middle:]
        return left, right

    def merge(array1, array2):
        sorted = []
        index1 = 0
        index2 = 0
        while index1 < len(array1) and index2 < len(array2):
            if array1[index1] <= array2[index2]:
                sorted.append(array1[index1])
                index1 += 1
            else:
                sorted.append(array2[index2])
                index2 += 1
        return sorted + array1[index1:] + array2[index2:]

    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array
    else:
        left, right = divide(array)
        return merge(merge_sort(left), merge_sort(right))

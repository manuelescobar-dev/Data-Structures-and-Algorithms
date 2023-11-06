def insertion_sort(array):
    for i in range(1, len(array)):
        selected_index = i
        selected = array[i]
        for explored in range(i - 1, -1, -1):
            if selected < array[explored]:
                array[explored + 1] = array[explored]
                selected_index -= 1
            else:
                break
        array[selected_index] = selected
    return array

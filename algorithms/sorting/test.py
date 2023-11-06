from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
import time
import random

sorting_algorithms = [
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
]


def compare(array_length, algorithms):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    array = [
        alphabet[random.randint(0, len(alphabet) - 1)] for i in range(array_length)
    ]
    a = array.copy()
    a.sort()
    correct = a
    for i in algorithms:
        start = time.time()
        a = array.copy()
        result = i(a)
        end = time.time()
        if result == correct:
            print("Correct | Time:", end - start)
        else:
            print("Incorrect | Time:", end - start)


compare(10000, sorting_algorithms)

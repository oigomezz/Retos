def quicksort(array):
    if not array:
        return array
    else:
        return quicksort_recursive(array, 0, len(array) - 1)


def quicksort_recursive(array, first, last):
    i = first
    j = last
    pivot = (array[i] + array[j]) // 2

    while i < j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            x = array[j]
            array[j] = array[i]
            array[i] = x
            i += 1
            j -= 1

    if first < j:
        array = quicksort_recursive(array, first, j)

    if last > i:
        array = quicksort_recursive(array, i, last)

    return array


sorted_array = quicksort([3, 5, 1, 8, 9, 0])
for item in sorted_array:
    print(item)

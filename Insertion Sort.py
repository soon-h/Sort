def insertion_sort(array):
    for point in range(1,len(array)):
        i = point
        while i > 0 and array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
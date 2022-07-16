def insertion_sort(array):
    for point in range(1,len(array)):
        for compare in range(point, 0 , -1):
            if array[compare - 1] > array[compare]:
                array[compare - 1], array[compare] = array[compare], array[compare - 1]
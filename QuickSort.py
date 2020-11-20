def QuickSort(input_array):
    n = len(input_array)
    if n <=1:
        return input_array
    pivot = input_array[n-1]
    left = [x for x in input_array if x<pivot]
    right = [x for x in input_array if x>pivot]
    pivotList = [x for x in input_array if x==pivot]

    left = QuickSort(left)
    right = QuickSort(right)

    return left+pivotList+right
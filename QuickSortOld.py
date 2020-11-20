"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    print("start",array)
    n = len(array)
    if (n<2):
        print("end",array)
        return array
    if(n==2):
        if(array[0]>array[1]):
            array[0], array[1]= array[1], array[0]
        print("end",array)
        return array
    pivot_index = n-1
    i=0
    while i< pivot_index:
        if array[i] > array[pivot_index]:
            array[i], array[pivot_index-1] = array[pivot_index-1], array[i]
            array[pivot_index], array[pivot_index-1] = array[pivot_index-1], array[pivot_index]
            pivot_index -= 1
        else:
            i+=1
    print("recursion",array)
    array[0:pivot_index] = quicksort(array[0:pivot_index])
    array[pivot_index+1:] = quicksort(array[pivot_index+1:])
    print("end",array)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print( quicksort(test))
def MergeSort(input_array):
    n = len(input_array)
    if n ==1:
        return input_array
    m = n//2
    left = MergeSort(input_array[0:m])
    right = MergeSort(input_array[m:])
    return Merge(left,right)

def Merge(left,right):
    l_index =0
    r_index =0
    l_count = len(left)
    r_count = len(right)
    result =[]
    while l_index < l_count and r_index< r_count:
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index+=1
        else:
            result.append(right[r_index])
            r_index+=1
    while l_index < l_count:
        result.append(left[l_index])
        l_index+=1
    while r_index < r_count:
        result.append(right[r_index])
        r_index+=1
    return result
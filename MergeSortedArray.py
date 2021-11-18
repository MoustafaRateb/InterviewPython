import TestHelper


def MergeSortedArrays(a, b):
    # define index for each array
    indexA = indexB = 0
    # store each array length in variable
    lenA = len(a)
    lenB = len(b)
    # define empty array
    result = []
    # loop until the 2 indices are larger than or equal their array length
    while indexA < lenA or indexB < lenB:
        # loop on the 1st array until you found element > current element of 2nd array
        if indexA < lenA and (indexB >= lenB or a[indexA] <= b[indexB]):
            result.append(a[indexA])
            indexA += 1

        # loop on the 2nd array until you found element > current element of 1st array
        if indexB < lenB and (indexA >= lenA or b[indexB] <= a[indexA]):
            result.append(b[indexB])
            indexB += 1
    return result


a = TestHelper.GenerateRandomIntSortedList(4, 0, 1000)
b = TestHelper.GenerateRandomIntSortedList(3, 0, 1000)

result = MergeSortedArrays(a, b)

print(a, b, result)

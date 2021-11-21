import TestHelper
def inserionSort(arr):

    for i in range(1,len(arr)):
    # loop over the input starting from second element
        j = i-1
        isSorted = True
        while j>=0 and arr[i] < arr[j]:
            j -=1
            isSorted = False
        if not isSorted and j>=0:
            arr = arr[0:j+1] + [arr[i]] + arr[j+1:i] + arr[i+1:]
        elif not isSorted and j<0:
            arr = [arr[i]] + arr[0:i] + arr[i+1:]
            
    return arr

a = TestHelper.GenerateRandomIntList(15)

print(a)

a= inserionSort(a)

print(a)
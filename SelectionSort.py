import TestHelper
def selectionSort(arr):
    # loop over the input
    for i in range(len(arr)):
        # define var for minimum location
        minLoc = i
        # loop over the input again to find min location
        for j in range(i,len(arr)):
            if arr[j] < arr[minLoc]:
                minLoc = j
        # swap i with minimum location
        arr[minLoc],arr[i] = arr[i],arr[minLoc]

a = TestHelper.GenerateRandomIntList(20)

print(a)

selectionSort(a)

print(a)
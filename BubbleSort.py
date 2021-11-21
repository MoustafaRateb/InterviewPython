import TestHelper
def bubbleSort(arr):
    # loop over the input
    for i in range(len(arr)):
        # loop over the input again
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            # if the first loop var > second loop var swap them

a = TestHelper.GenerateRandomIntList(15)

print(a)

bubbleSort(a)

print(a)
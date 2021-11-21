def insort(num,arrSorted):
    
    if not arrSorted:
        return [num]
    
    testArr = arrSorted
    n = len(arrSorted)
    insertionIndex = n//2
    indexMin =0
    indexMax = n-1
    while testArr:
        m = getMedian(testArr)
        if num > m:
            indexMin = insertionIndex+1
            testArr=arrSorted[insertionIndex+1:indexMax]
        elif num == m:
            break
        else:
            indexMax = insertionIndex
            testArr = arrSorted[indexMin:insertionIndex]
        insertionIndex = (indexMax-indexMin+1)//2 
    return arrSorted[0:indexMin] +[num]+arrSorted[insertionIndex+1:]   
    
def runningMedian(a):
    # define results array 
    result =[]
    # define median array 
    medians =[]
    # loop over input array 
    for i in a:
        medians = insort(i,medians)
        result.append(getMedian(medians))
        # apply insertion sort for new value
        # add median to result list
    # Write your code here
def getMedian(a):
    n = len(a)
    if n%2:
        return a[n//2]
    else:
        return (a[n//2]+a[n//2 -1])/2

r = runningMedian([12, 4, 5, 3, 8, 7])
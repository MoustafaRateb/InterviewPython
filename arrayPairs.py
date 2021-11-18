import TestHelper


def CreatePairs(arr):
    resultArr = []
    for i in arr:
        for j in arr:
            if i != j:
                resultArr.append((i, j))
    return resultArr


testArr = TestHelper.GenerateRandomIntList(5)
result = CreatePairs(testArr)
print(result, len(result))

import TestHelper
from datetime import datetime


def IsArraysIntersected(arr1, arr2):

    for i in arr1:
        for j in arr2:
            if i == j:
                return True

    return False


def IntersectionCount(arr1, arr2):
    count = 0
    for i in arr1:
        for j in arr2:
            if i == j:
                count += 1

    return count


def IntersectionCountSorted(arr1, arr2):
    count = 0
    arr1.sort()
    arr2.sort()
    index1 = 0
    index2 = 0
    n = len(arr1)
    m = len(arr2)
    while index1 < n and index2 < m:

        e1 = arr1[index1]
        e2 = arr2[index2]
        if e1 == e2:
            count += 1
            index2 += 1
        while e1 < e2 and index1 < n:
            index1 += 1
            if index1 < n:
                e1 = arr1[index1]

        while e2 < e1 and index2 < m:
            index2 += 1
            if index2 < m:
                e2 = arr2[index2]

    return count


def IntersectionCountHash(arr1, arr2):
    count = 0
    d1 = {}
    for i in arr1:
        d1[i] = 1

    for j in arr2:
        if j in d1:
            count += 1

    return count


a1 = TestHelper.CreateRandomIntListWithoutDuplicates(50000, 0, 1000000)
a2 = TestHelper.CreateRandomIntListWithoutDuplicates(40000, 0, 1000000)

print("solution 1")
t1 = datetime.now()

count = IntersectionCount(a1, a2)

t2 = datetime.now()

print("IntersectionCount", count, "Time diff", t2-t1)

print("solution 2")
t1 = datetime.now()

count = IntersectionCountSorted(a1, a2)

t2 = datetime.now()

print("IntersectionCountSorted", count, "Time diff", t2-t1)

print("solution 3")
t1 = datetime.now()

count = IntersectionCountHash(a1, a2)

t2 = datetime.now()

print("IntersectionCountHash", count, "Time diff", t2-t1)

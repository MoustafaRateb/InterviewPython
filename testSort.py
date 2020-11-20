import TestHelper
import MergeSort
import QuickSort
import heapSort
from time import time

l = TestHelper.CreateRandomIntList(100000,10,9000000)
lc = list(l)
t0 = time()

qck = QuickSort.QuickSort(l)
t1 = time()
s = MergeSort.MergeSort(l)
t2 = time()
heapSort.heapSort(lc)
t3 = time()
print((l[99],s[99]))
print((l[99],qck[99]))
print((l[99],lc[99]))

print('function vers1 takes %f' %(t1-t0))
print('function vers2 takes %f' %(t2-t1))
print('function vers3 takes %f' %(t3-t2))

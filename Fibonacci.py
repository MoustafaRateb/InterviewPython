import TestHelper
from datetime import datetime

def Fibonacci_iterative(number):
    #handle 0 and 1 special case
    if number in [0,1]: return number
    #def firstTerm = 0, secondTertm =1
    firstTerm = 0
    secondTerm = 1
    # loop from 2 to number
    for n in range(2,number+1):
        # temp = second term
        temp = secondTerm
        # second term = first + second
        secondTerm += firstTerm
        # first = temp
        firstTerm = temp
        # 
    return secondTerm 

def Fibonacci_recursive(number):
    cache = {}
    def fib(number):
        # base case fpr 1 & 0
        if number in [0,1] : return number
        # recursive case
        if not number in cache:
            cache[number] = fib(number-1) + fib(number-2)
        return cache[number]
    return fib(number)
    
    
intList = TestHelper.GenerateRandomIntListWithoutDuplicates(5,1,60)

for i in intList:
    t1 = datetime.now()
    r = Fibonacci_iterative(i)
    t2 = datetime.now()
    print(i,"Fibonacci_iterative",r,t2-t1)
    t1 = datetime.now()
    r = Fibonacci_recursive(i)
    t2 = datetime.now()
    print(i,"Fibonacci_recursive",r,t2-t1)


import TestHelper
def Factorial_Iterative(num):
    if num == 0: return 1
    # define var for factorial initialy = 1
    factorialResult = 1
    # loop on numbers from 1 to num
    for i in range(1,num+1):
        # multiply each num * factorial var and save result to factorial
        factorialResult *= i
    return factorialResult

def Factorial_Recursive(num):
    if num == 0: return 1
    # define base case  for 1 return 1
    if num == 1:return 1
    # if num > 1 call recursively num * Factorial_Recursive(num -1)
    return num * Factorial_Recursive(num -1)
    
intList = TestHelper.GenerateRandomIntListWithoutDuplicates(5,1,20)

for i in intList:
    print(i,"Factorial_Iterative",Factorial_Iterative(i))
    print(i,"Factorial_Recursive",Factorial_Recursive(i))

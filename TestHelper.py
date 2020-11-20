from random import randint,sample
def CreateRandomIntList(size,mn=0,mx=100):
    l = [randint(mn,mx) for i in range(size)]
    return l
def CreateRandomIntListWithoutDuplicates(size,mn=0,mx=100):
    l = sample(range(mn,mx),size)
    return l



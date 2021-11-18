from CharListEnum import CharType
import TestHelper


def GetFirstDuplicateIndex(s):
    # Create empty dict
    charDict = {}

    # define empty var contains min duplicate index = string length
    minDuplicateIndex = len(s)
    duplicateFound = False

    # loop on string by index
    for index in range(len(s)):
        # get char by index
        c = s[index]
        # check if char exist in dict
        if c in charDict:
            # if index saved in dict less than value in minDuplicateIndex update it
            duplicateFound = True
            if minDuplicateIndex > charDict[c]:
                minDuplicateIndex = charDict[c]
        elif not duplicateFound:
            # otherwise if minDuplicateIndex not assigned add current char to dict
            charDict[c] = index
    if duplicateFound:
        return s[minDuplicateIndex]
    return "No duplicate"


def GetFirstDuplicate(s):
    # Create empty dict
    charDict = {}
    # loop on string
    for c in s:
        # check if char exist in dict return it
        if c in charDict:
            return c
        charDict[c] = True
        # otherwise add it
    return "No duplicate"


m = TestHelper.GenerateRandomString(20, CharType.Uppercase)

print(m, "  First duplicate  ", GetFirstDuplicate(m))
print(m, "  First index  ", GetFirstDuplicateIndex(m))

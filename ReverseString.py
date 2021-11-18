from CharListEnum import CharType
import TestHelper


def ReverseString(s):
    # Create empty string
    r = ''
    # loop on string in reverse order
    for i in range(len(s)-1, -1, -1):
        r += s[i]

    return r
    # add chars to empty string


m = TestHelper.GenerateRandomString(8, CharType.Digit)

print(m, "  ---  ", ReverseString(m))

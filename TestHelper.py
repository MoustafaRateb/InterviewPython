import string
from CharListEnum import CharType
from random import randint, sample, choices, choice

# region Integer methods


def GenerateRandomIntList(size, mn=0, mx=100):
    l = [randint(mn, mx) for i in range(size)]
    return l


def GenerateRandomIntListWithoutDuplicates(size, mn=0, mx=100):
    l = sample(range(mn, mx), size)
    return l


def GenerateRandomIntSortedList(size, mn=0, mx=100):
    l = GenerateRandomIntList(size, mn, mx)
    l.sort()
    return l
# endregion

# region char and strings


def GenerateRandomCharList(size, charString):
    l = choices(charString, k=size)
    return l


def GenerateRandomLowercaseCharList(size):
    return GenerateRandomCharList(size, string.ascii_lowercase)


def GenerateRandomUppercaseCharList(size):
    return GenerateRandomCharList(size, string.ascii_lowercase)


def GenerateRandomAlphaCharList(size):
    return GenerateRandomCharList(size, string.ascii_letters)


def GenerateRandomAlphaNumCharList(size):
    return GenerateRandomCharList(size, string.ascii_letters + string.digits)


def GenerateRandomPrintableCharList(size):
    return GenerateRandomCharList(size, string.printable)


def GenerateRandomString(size, type=CharType.Alphabetic):
    charString = ''

    if type == CharType.Alphabetic:
        charString = string.ascii_letters
    elif type == CharType.Alphanumeric:
        charString = string.ascii_letters + string.digits
    elif type == CharType.Lowercase:
        charString = string.ascii_lowercase
    elif type == CharType.Uppercase:
        charString = string.ascii_uppercase
    elif type == CharType.Printable:
        charString = string.printable
    elif type == CharType.Digit:
        charString = string.digits
    else:
        charString = string.ascii_letters
    s = "".join(GenerateRandomCharList(size, charString))
    return s

# endregion

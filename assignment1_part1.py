class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):
    divisible = 0
    for n in numbers:
        if (n % divide == 0):
            divisible += 1
    return divisible

def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except Exception:
        raise ListDivideException

testListDivide()
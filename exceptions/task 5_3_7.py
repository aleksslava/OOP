digits = list(map(float, input().split()))

class TupleLimits(tuple):
    def __init__(self, lst, max_length):

        self.lst = lst
        self.max_length = max_length

    def __new__(cls, iterable, max):
        if len(iterable) > max:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return tuple.__new__(cls, iterable)

    def __str__(self):
        res = list(map(str, self.lst))
        return ' '.join(res)

    def __repr__(self):
        res = list(map(str, self.lst))
        return ' '.join(res)

try:
    t = TupleLimits(digits, 5)
    print(t)
except Exception as error:
    print(error)
class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self._min_value <= value <= self._max_value:
            self.__value = value
        else:
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self._min_value <= value <= self._max_value:
            self.__value = value
        else:
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self._min_length <= len(value) <= self._max_length:
            self.__value = value
        else:
            raise CellStringException('длина строки выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, item):
        if item >= len(self.data):
            raise IndexError
        else:
            res = self.data[item].value
            return res

    def __setitem__(self, key, val):
        if key >= len(self.data):
            raise IndexError
        else:
            self.data[key].value = val

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        if self.ind < len(self):
            res = self.data[self.ind]
            self.ind += 1
            return res.value
        else:
            raise StopIteration



ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception as e:
    print(e)
    print("Общая ошибка при работе с объектом TupleData")

for i in ld:
    print(i)
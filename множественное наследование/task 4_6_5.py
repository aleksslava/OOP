class Digit:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        else:
            object.__setattr__(self, key, value)


class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


digits = [PrimeNumber(2),
          PrimeNumber(5),
          PrimeNumber(19),
          FloatPositive(5.4),
          FloatPositive(15.3),
          FloatPositive(11.5),
          FloatPositive(2.4),
          FloatPositive(0.5)
          ]

lst_positive = [obj for obj in digits if isinstance(obj, Positive)]
lst_float = [obj for obj in digits if isinstance(obj, Float)]
print(len(lst_positive))
print(len(lst_float))
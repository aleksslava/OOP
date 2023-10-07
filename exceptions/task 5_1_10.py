class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if not isinstance(value, float) or not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return True


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int or not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')
        else:
            return True

def is_valid(lst, validators):
    new_lst = []
    for char in lst:
        for obj in validators:
            try:
                obj(char)
                new_lst.append(char)
            except:
                continue



    return new_lst

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]

print(lst_out)
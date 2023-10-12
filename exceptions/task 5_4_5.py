class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'pk' in kwargs or 'id' in kwargs:
            key, value = tuple(kwargs.items())[0]
            self.message = f'Значение первичного ключа {key} = {value} недопустимо'
        else:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id='-10,5')
except PrimaryKeyError as e:
    print(e)

e = PrimaryKeyError(qr='3')
print(e)
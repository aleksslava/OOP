class Note:
    def __init__(self, name, ton):
        self.__valid_name(name)
        self.__valid_ton(ton)
        self._name = name
        self._ton = ton

    @staticmethod
    def __valid_name(name):
        if not isinstance(name, str) or name not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')

    @staticmethod
    def __valid_ton(ton):
        if not isinstance(ton, int) or not -1 <= ton <= 1:
            raise ValueError('недопустимое значение аргумента')

    def __setattr__(self, key, value):
        if key == '_name':
            self.__valid_name(value)
        if key == '_ton':
            self.__valid_ton(value)
        object.__setattr__(self, key, value)


class Notes:
    __instance = None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        for note, name in zip(self.__slots__, ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')):
            setattr(self, note, Note(name, 0))


    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item <= 6:
            raise IndexError('недопустимый индекс')
        key = self.__slots__[item]
        return getattr(self, key)





notes = Notes()
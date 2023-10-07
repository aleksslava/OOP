class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getattr__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            print("Атрибут с именем z не существует")


pt = Point(1, 2)


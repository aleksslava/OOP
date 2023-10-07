class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height'):
            if value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)


    def is_collision(self, rect):
        if self._y < rect._y - rect._height or self._y - self._height > rect._y:
            return True
        if self._x + self._width < rect._x or rect._x + rect._width < self._x:
            return True
        raise TypeError('прямоугольники пересекаются')

    def __hash__(self):
        return hash((self._x, self._y, self._width, self._height))


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []

for obj in lst_rect:
    try:
        for other in lst_rect:
            if hash(obj) != hash(other):
                obj.is_collision(other)
        lst_not_collision.append(obj)
    except:
        continue



r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if hash(x) != hash(rect):
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))

assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
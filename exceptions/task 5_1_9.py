class Triangle:
    def __init__(self, a, b, c):

        self._a = a
        self._b = b
        self._c = c
        self.is_triangle(a, b, c)

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')

        else:
            object.__setattr__(self, key, value)

    def is_triangle(self, a, b, c):
        if a >= c+b or b >= a+c or c >= a+b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []

for args in input_data:
    try:
        obj = Triangle(*args)
        lst_tr.append(obj)
    except:
        continue

print(lst_tr)

tr = Triangle(-1, 4.54, 3)
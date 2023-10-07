class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


x, y = input().split()

try:
    x, y = int(x), int(y)
    pt = Point(x, y)

except:
    try:
        x, y = float(x), float(y)
        pt = Point(x, y)
    except:
        pt = Point()

finally:
    print(f'Point: x = {pt._x}, y = {pt._y}')



x, y = input().split()

try:
    pt = Point(x, y)

except:
    pt = Point()

finally:
    print(f'Point: x = {pt._x}, y = {pt._y}')
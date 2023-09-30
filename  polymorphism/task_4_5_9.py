from collections import deque
class Deskr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        else:
            object.__setattr__(instance, self.name, value)


class PointTrack:
    x = Deskr()
    y = Deskr()
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'



class Track:
    def __init__(self, *args):
        if len(args) == 2:
            if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
                self.__points = [].append(PointTrack(args[0], args[1]))
        else:
            self.__points = list(args)
        self.__points = deque(self.__points)


    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, obj):
        self.__points.append(obj)

    def add_front(self, obj):
        self.__points.appendleft(obj)

    def pop_back(self):
        return self.__points.pop()

    def pop_front(self):
        return self.__points.popleft()


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
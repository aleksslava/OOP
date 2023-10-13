import copy

class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):

        if self.box_weight() + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        else:
            self._things.append(obj)

    def box_weight(self):
        res = list(map(lambda x: x[1], self._things))

        return sum(res)

class BoxDefender:
    def __init__(self, box):
        self._box = box

    def __enter__(self):
        self._box_copy = copy.deepcopy(self._box)
        return self._box_copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._box._things[:] = self._box_copy._things
        else:

            return False


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))

print(box._things)

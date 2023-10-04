class ShopGenericView:
    def __repr__(self):
        res = ''
        for key, value in self.__dict__.items():
             res += f'{key}: {value}\n'
        return res
    def __str__(self):
        res = ''
        for key, value in self.__dict__.items():
            res += f'{key}: {value}\n'
        return res


class ShopUserView:
    def __repr__(self):
        res = ''
        for key, value in self.__dict__.items():
            if key != "_id":
                res += f'{key}: {value}\n'
        return res

    def __str__(self):
        res = ''
        for key, value in self.__dict__.items():
             if key != "_id":
                  res += f'{key}: {value}\n'
        return res


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year



book = Book("Python ООП", "Балакирев", 2022)

print(book)



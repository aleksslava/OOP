def input_int_numbers():
    str = input().split()
    try:
        str = tuple(map(int, str))
    except:
        raise TypeError('все числа должны быть целыми')

    else:
        return str


while True:
    try:
        str = input_int_numbers()
    except TypeError:
        pass

    else:
        print(*str)
        break

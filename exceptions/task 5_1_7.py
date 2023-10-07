lst_in = input().split()

def is_num(char):
    try:
        char = int(char)
    except ValueError:
        return False

    return True

lst_in = sum(list(map(int, filter(is_num, lst_in))))
print(lst_in)
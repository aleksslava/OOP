lst_in = input().split()

def is_num(char):
    try:
        char = int(char)
    except ValueError:
        try:
            char = float(char)
        except ValueError:
            return char

        return char

    return char

lst_out = list(map(is_num, lst_in))


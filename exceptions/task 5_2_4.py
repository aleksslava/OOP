x, y = input().split()

try:
    res = int(x) + int(y)
except:
    try:
        res = float(x) + float(y)
    except:
        res = str(x) + str(y)

finally:
    print(res)
print("hello world")

a = 1

if a > 1:
    print(a)
    print("맞느뇨~")
    s = "good"

    if a + 1 == 2:
        print(a)

print("앤드게임")

def int2digit(n, base):
    res = ""
    while n > 0:
        n, r = divmod(n, base)
        res = str(r) + res
    return res

result = int2digit(22, 2)

print(result)
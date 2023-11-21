def s(a, b, c):
    D = (b**2 - 4*a*c)**0.5

    if D > 0:
        x1 = (-b + D) / (2 * a)
        x2 = (-b - D) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return "無實跟"

a, b, c = map(int, input("請輸入 a, b, c: ").split(", "))
print(s(a, b, c))

def a(a1, b1, c1, a2, b2, c2):
    
    if b1 == 0 or b2 == 0:
        return "相交"

    slope1 = -a1 / b1
    slope2 = -a2 / b2

    if slope1 == slope2:
        if a1 * c2 == a2 * c1:
            return "重合"
        return "平行"
    else:
        return "相交"

a1, b1, c1, a2, b2, c2 = map(int, input("請輸入 a1, b1, c1, a2, b2, c2: ").split(", "))
print(a(a1, b1, c1, a2, b2, c2))

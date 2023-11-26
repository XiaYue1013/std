def t(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "不是有效的三角形"
        
    longest = max(a, b, c)
    if longest == a:
        c, a = a, c
    elif longest == b:
        c, b = b, c

    if c**2 == a**2 + b**2:
        t_type = "直角三角形"
    elif c**2 > a**2 + b**2:
        t_type = "鈍角三角形"
    else:
        t_type = "銳角三角形"

    s = (a + b + c) / 2 
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return f'類型: {t_type}, 面積: {area}'

a, b, c = map(int, input("請輸入 a, b, c: ").split(", "))
print(t(a, b, c))

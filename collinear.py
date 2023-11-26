def c(x1, y1, x2, y2, x3, y3):
    
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    
    if area == 0:
        return "共線"
    else:
        return f"未共線，面積: {area}"

x1, y1, x2, y2, x3, y3 = map(int, input("請輸入三個座標 (x1, y1, x2, y2, x3, y3): ").split(", "))
print(c(x1, y1, x2, y2, x3, y3))

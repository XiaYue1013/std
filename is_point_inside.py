def is_point_inside(x1, y1, x2, y2, x3, y3, x4, y4):

    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

    area_ABC = area(x1, y1, x2, y2, x3, y3)

    area_DAB = area(x4, y4, x1, y1, x2, y2)

    area_DBC = area(x4, y4, x2, y2, x3, y3)

    area_DAC = area(x4, y4, x1, y1, x3, y3)

    return area_ABC == area_DAB + area_DBC + area_DAC

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input("請輸入 x1, y1, x2, y2, x3, y3, x4, y4: ").split(", "))
print("D 在 ABC內" if is_point_inside(x1, y1, x2, y2, x3, y3, x4, y4) else "D 在 ABC外")

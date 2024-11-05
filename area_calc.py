#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / coverage)
    print(cans)
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)



import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(distance(1,1,4,4,))

def area(r):
    radius = distance(xc, yc, xp, yp)
    return 3.14*r*r


result = area(radius)
print(result)



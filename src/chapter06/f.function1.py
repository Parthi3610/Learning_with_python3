

def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    dsquare = dx*dx +dy*dy
    result = dsquare*(1/2)
    return result

print(distance(1,1,4,4,))


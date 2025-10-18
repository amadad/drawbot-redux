a = (200, 200)
b = (800, 800)
c = (800, 200)

def lerp(n1, n2, rat):
    return n1 + rat * (n2 - n1)
    
def lerpPts(pt1, pt2, rat): #2-tuples (x, y)
    return lerp(pt1[0], pt2[0], rat), lerp(pt1[1], pt2[1], rat) # returns 2-tuple (x, y)
    
def fAngle(pt1, pt2):  
    return atan2((pt2[1] - pt1[1]), (pt2[0] - pt1[0]))
    
def fDist(pt1, pt2): # Length of hypoteneuse
    return sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
    
newPage()
stroke(0)
strokeWidth(3)
lineCap('round')

line(a, b)
#line(a, c)
line(a, lerpPts(a, c, .5))

print(degrees(fAngle(a, b)))
print(fDist(a, b))
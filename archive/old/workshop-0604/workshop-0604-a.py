# newPage()
# #fill(127/255, .75, .75, .25)
# rect(250, 250, 250, 250)
# oval(500, 500, 250, 250)
# stroke(0)
# #strokeWidth(2)
# lineCap('round')
# fill(.5)
# line((275, 525), (475,725)) # 2-tuple
# line((275, 725), (475,525))

# newPage()
# polygon((250,250), (250,500), (500,500), (500,750), (750,750), (750,500), (500,500), (500,250))

# newPage()
# stroke(0)
# #fill(none)
# path = newPath()
# moveTo((250, 250))
# lineTo((250, 500))
# lineTo((500, 500))
# lineTo((500, 750))
# lineTo((750, 750))
# lineTo((750, 500))
# lineTo((500, 500))
# lineTo((500, 250))
# closePath()
# drawPath()

newPage()
# fill(None)
# stroke(0)
a = BezierPath()
b = BezierPath()
a.rect(350, 350, 250, 250)
b.oval(450, 450, 250, 250)

#drawPath(a); drawPath(b)
drawPath(a.xor(b))
#drawPath(a + b)

newPage()
a = BezierPath()
b = BezierPath()
c = BezierPath()
a.moveTo((250, 250))
a.lineTo((250, 500))
a.lineTo((500, 500))
a.lineTo((500, 750))
a.lineTo((750, 750))
a.lineTo((750, 500))
a.lineTo((500, 500))
a.lineTo((500, 250))
a.closePath()
drawPath(a)

rad = 250
def fOffCurve(radius, fraction): # arc fraction of the circle
    # formula for control points (handles) to draw circular arcs
    return radius * (4/3) * tan(pi/(fraction * 2))

bx, by = 250, 750 # defining center of b circle
handle = fOffCurve(rad, 4) # dist from on-curve points to control points
print(handle)

fill(None)
stroke(0)
b.moveTo((bx, by + rad))
# draw clockwise
b.curveTo((bx + handle, by + rad), (bx + rad, by + handle), (bx + rad, by))
b.curveTo((bx + rad, by - handle), (bx + handle, by - rad), (bx, by - rad))
b.curveTo((bx - handle, by - rad), (bx - rad, by - handle), (bx - rad, by))
b.curveTo((bx - rad, by + handle), (bx - handle, by + rad), (bx, by + rad))
b.closePath()
drawPath(b)

fill(0)
stroke(None)
c.rect(0, 500, 500, 500)
c = c.difference(b)
drawPath(c)
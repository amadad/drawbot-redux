if 0:
    size(400, 400)
    # x, y, w, h
    for n in range(500):
        fill(random(), random(), random(), 0.5)
        x = random()*400
        y = random()*400
        if random()<0.5:
            rect(x, y, random()*60+10, 6)
        else:
            oval(x, y, random()*30+10, 6)
    print random()

# create a bezier path
path = BezierPath()

# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((100, 200))
path.lineTo((200, 200))
# close the path
path.closePath()

# loop over a range of 10
for i in range(20):
    newPage(1000, 1000)
    # set a random color with alpha value of .3
    fill(random(), random(), random(), .3)
    # translate the canvas
    translate(i*35, i*25)
    # in each loop draw the path
    drawPath(path)

saveImage('triangles.gif')
canvas = 1024
side = canvas/8
limit = canvas
fRate = 1/24
nFrames = 48
offset = 128
colorspace = "sRGB"

colorsRGB = [
    (0,0,0),
    (71,88,56),
    (159,184,173),
    (255,236,68),
    (255,185,32),
    (206,208,206),
    (232,232,230),
    (161,135,120),
    (50,26,20),
    ]
colors = [(r/255, g/255, b/255) for (r,g,b) in colorsRGB]

for n in range(nFrames):
    newPage(canvas, canvas)
    fill(1)
    rect(0,0,width(),height())
    stroke(0)
    currentPos = offset
    while currentPos < canvas:
        line((0, currentPos), (canvas, currentPos))
        line((currentPos, 0), (currentPos, canvas))
        currentPos += offset
    rowIncrement = 0 # draw from the bottom up
    colorCounter = True
    r = cos(n * pi/nFrames)
    r1 = cos(pi/4 + (n * (2 * pi)/nFrames))
    rot = r * 45 + r1 * 67.5
    
    while rowIncrement < canvas:
        colIncrement = 0 # draw from left to right
        isBlack = colorCounter
        while colIncrement < canvas:
            if isBlack:
                fill(0)
            else:
                fill(1)
            # frameDuration(fRate)
            # translate(width()/2, height()/2)
            with savedState():
                rotate(rot, (colIncrement + side/2, rowIncrement + side/2))
                if isBlack == True:
                    rect(colIncrement, rowIncrement, side, side)
            isBlack = not isBlack
            colIncrement += side
        colorCounter = not colorCounter
        rowIncrement += side
    
saveImage('~/Desktop/spin_square4.gif')
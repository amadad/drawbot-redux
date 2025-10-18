canvas = 1024
side = canvas/8
limit = canvas
fRate = 1/24
nFrames = 48

for n in range(nFrames):
    newPage(canvas, canvas)
    rowIncrement = 0 # draw from the bottom up
    #colorCounter = True
    r = cos(n * pi/nFrames)
    r1 = cos(pi/4 + (n * (2 * pi)/nFrames))
    rot = r * 45 + r1 * 67.5
    while rowIncrement < canvas:
        colIncrement = 0 # draw from left to right
        #isBlack = colorCounter
        while colIncrement < canvas:
            #if isBlack:
            fill(0)
            frameDuration(fRate)
            translate(width()/2, height()/2)
            rotate(rot)
            rect(colIncrement, rowIncrement, side, side)
            colIncrement += side
        rowIncrement += side
    
saveImage('~/Desktop/spin_square4.gif')
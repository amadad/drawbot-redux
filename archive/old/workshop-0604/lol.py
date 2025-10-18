canvas = 1048
nSquares = 8
side = canvas/nSquares
offset = side
fRate = 1/24
nFrames = 48

for n in range(nFrames):
    newPage(canvas, canvas)
    r = cos(n * pi/nFrames)
    fill(1)
    rect(0, 0, height(), width())
    fill(0)
    for row in range(nSquares):
        y = row * side
        for col in range(nSquares):
            x = col * side
            if (row + col) % 2 == 0:
                fill(0)
            else:
                fill(1)
            frameDuration(fRate)
            rotate(r)
            rect(x, y, side, side)
        
saveImage('~/Desktop/spin_square5.gif')
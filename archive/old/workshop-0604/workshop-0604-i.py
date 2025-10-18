canvas = 1024
size = canvas/2
fRate = 1/24
nFrames = 48


for n in range(nFrames):
    newPage(canvas, canvas)
    # r = n * 90/nFrames
    r = cos(n * pi/nFrames)
    r1 = cos(pi/4 + (n * (2 * pi)/nFrames))
    rot = r * 45 + r1 * 67.5
    fill(1)
    rect(0, 0, height(), width())
    fill(0)
    frameDuration(fRate)
    translate(width()/2, height()/2)
    rotate(rot)
    rect(-size/2, -size/2, size, size)
    
saveImage('~/Desktop/spin_square3.gif')
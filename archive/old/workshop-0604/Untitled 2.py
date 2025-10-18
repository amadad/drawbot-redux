canvas = 1048
nSquares = 8
side = canvas/nSquares
offset = side

newPage(canvas, canvas)
r = cos(pi/nSquares)

#translate(height()/2, width()/2)
#translate(-(nSquares - 1) * offset/2, (nSquares -1) * offset/2)

for row in range(nSquares):
    y = row * side
    for col in range(nSquares):
        x = col * side
        if (row + col) % 2 == 0:
            fill(0)
        else:
            fill(1)
        rotate(r)
        rect(x, y, side, side)
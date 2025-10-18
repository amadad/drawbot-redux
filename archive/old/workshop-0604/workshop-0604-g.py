canvas = 1048
nSquares = 8
side = canvas/nSquares
offset = side

newPage(canvas, canvas)
for row in range(nSquares):
    y = row * side
    for col in range(nSquares):
        x = col * side
        if (row + col) % 2 == 0:
            fill(0)
        else:
            fill(1)
        rect(x, y, side, side)
        
newPage(canvas, canvas)
for row in range(nSquares):
    y = height()/2 - ((nSquares - 1) * offset/2) + (row * offset)
    for col in range(nSquares):
        x = width()/2 - ((nSquares - 1) * offset/2) + (col * offset)
        if (row + col) % 2 == 0:
            fill(0)
        else:
            fill(1)
        rect(x - side/2, y - side/2, side, side)
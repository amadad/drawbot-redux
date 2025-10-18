canvas = 1024
nSquares = 8
side = canvas/nSquares
offset = side

newPage(canvas, canvas)
fill(1) # set color to white
rect(0, 0, width(), height()) # draw background shape (white)
fill(None) # reset color

translate(height()/2, width()/2)
translate(-(nSquares - 1) * offset/2, (nSquares -1) * offset/2)
#oval(-5, -5, 10, 10)

fill(0)
for row in range(nSquares):
    with savedState(): # Like Las Vegas
        translate(0, row * -offset)
        for col in range(nSquares):
            with savedState():
                translate(col * offset, 0)
                if (row + col) % 2 == 1:
                    rotate((7 - row) * 1)
                    rect(-side/2, -side/2, side, side)
      
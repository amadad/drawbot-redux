canvas = 1048
side = canvas/8
limit = canvas

newPage(canvas, canvas)
rowIncrement = 0 # draw from the bottom up
colorCounter = True
while rowIncrement < canvas:
    colIncrement = 0 # draw from left to right
    isBlack = colorCounter
    while colIncrement < canvas:
        if isBlack:
            fill(0)
        else:
            fill(1)
        rect(colIncrement, rowIncrement, side, side)
        
        isBlack = not isBlack
        colIncrement += side
    
    colorCounter = not colorCounter
    rowIncrement += side
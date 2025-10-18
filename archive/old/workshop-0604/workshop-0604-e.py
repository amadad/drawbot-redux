newPage()
thickness = width()/10
isHorizontal = True

if isHorizontal: # toggle direction
    limit = height()
else:
    limit = width()
    
isBlack = True # color counter
increment = 0 # sets guide position for stripes


while increment < limit:
    if isBlack:
        fill(0)
    else:
        fill(1)
    if isHorizontal:
        rect(0, increment, width(), thickness)
    else:
        rect(increment, 0, thickness, height())
    
    isBlack = not isBlack
    increment += thickness
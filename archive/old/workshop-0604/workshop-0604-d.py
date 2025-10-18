canvas = 1000
offset = 25

newPage(canvas, canvas)
stroke(0)
currentPos = offset
while currentPos < canvas:
    line((0, currentPos), (canvas, currentPos))
    line((currentPos, 0), (currentPos, canvas))
    currentPos += offset
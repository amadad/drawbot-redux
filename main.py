import drawBot

with drawBot.drawing():
    drawBot.newPage(1000, 1000)
    drawBot.rect(10, 10, 100, 100)
    drawBot.saveImage("~/Desktop/aRect.png")

cellSize = 250
images = {}
im = ImageObject('custom-images/Amz1.png')
# im = ImageObject()
# with im:
#     size(cellSize, cellSize)
#     font('myleaves curvepoint', cellSize*2.5)
#     text('b', (0, 0))
images['b'] = im

# derive d, p, q from b
d = ImageObject()
with d:
    translate(im.size()[0], 0)
    scale(-1, 1)
    image(im, (0, 0))
images['d'] = d

p = ImageObject()
with p:
    translate(0, im.size()[1])
    scale(1, -1)
    image(im, (0, 0))
images['p'] = p

q = ImageObject()
with q:
    translate(*im.size())
    scale(-1, -1)
    image(im, (0, 0))
images['q'] = q

a = ImageObject()
with a:
    translate(im.size()[0], 0)
    rotate (90)
    image(im, (0, 0))
images['a'] = a

c = ImageObject()
with c:
    translate(0, im.size()[1])
    rotate (-90)
    image(im, (0, 0))
images['c'] = c

e = ImageObject()
with e:
    # translate(im.size()[0], 0)
    rotate (-90, (cellSize/2, cellSize/2))
    image(d, (0, 0))
images['e'] = e

f = ImageObject()
with f:
    # translate(0, im.size()[1])
    rotate (90, (cellSize/2, cellSize/2))
    image(d, (0, 0))
images['f'] = f

# '1' = b
# '2' = a
# '3' = q
# '4' = c
# '5' = e
# '6' = d
# '7' = f
# '8' = p

for char in images:
    newDrawing()
    newPage(cellSize, cellSize)
    image(images[char], (0, 0))
    saveImage(f'images/{char}.png')
    
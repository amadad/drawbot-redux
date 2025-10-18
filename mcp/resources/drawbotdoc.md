DrawBot Documentation

Shapes
-Primitives
-Drawing Paths
-Path Properties
-BezierPath

Colors
-Fill
-Stroke
-CMYK Fill
-CMYK Stroke

Canvas
-Pages
-Transformations
-Saving

Text
-Drawing Text
-Text Properties
-Formatted Strings

Images
-Drawing Images
-Image Properties
-ImageObject

Variables
Quick Reference

### SHAPES

db.rect(x, y, w, h)
Draw a rectangle from position x, y with the given width and height.

# draw a rectangle
#x, y, w, h
db.rect(100, 100, 800, 800)

db.oval(x, y, w, h)
Draw an oval from position x, y with the given width and height.

# draw an oval
# x, y, w, h
db.oval(100, 100, 800, 800)

db.line((x1, y1), (x2, y2)))
Draws a line between two given points.

# set a stroke color
db.stroke(0)
# draw a line between two given points
db.line((100, 100), (900, 900))

db.polygon((x1, y1), (x2, y2), ..., close=True)
Draws a polygon with n-amount of points. Optionally a close argument can be provided to open or close the path. As default a polygon is a closed path.

# draw a polygon with x-amount of points
db.polygon((100, 100), (100, 900), (900, 900), (200, 800), close=True)

db.newPath()
Create a new path.

db.moveTo(xy)
Move to a point x, y.

db.lineTo(xy)
Line to a point x, y.

db.curveTo(xy1, xy2, xy3)
Curve to a point x3, y3. With given bezier handles x1, y1 and x2, y2.

db.qCurveTo(*points)
Quadratic curve with a given set of off curves to a on curve.

db.arc(center, radius, startAngle, endAngle, clockwise)
Arc with center and a given radius, from startAngle to endAngle, going clockwise if clockwise is True and counter clockwise if clockwise is False.

db.arcTo(xy1, xy2, radius)
Arc from one point to an other point with a given radius.

pt0 = 74, 48
pt1 = 238, 182
pt2 = 46, 252
radius = 60

def drawPt(pos, r=5):
    x, y = pos
    db.oval(x-r, y-r, r*2, r*2)

db.size(300, 300)
db.fill(None)

path = db.BezierPath()
path.moveTo(pt0)
path.arcTo(pt1, pt2, radius)

db.stroke(0, 1, 1)
db.polygon(pt0, pt1, pt2)
for pt in [pt0, pt1, pt2]:
    drawPt(pt)

db.stroke(0, 0, 1)
drawPath(path)
stroke(1, 0, 1)
for pt in path.onCurvePoints:
    drawPt(pt, r=3)
for pt in path.offCurvePoints:
    drawPt(pt, r=2)

closePath()
Close the path.

drawPath(path=None)
Draw the current path, or draw the provided path.

# create a new empty path
newPath()
# set the first oncurve point
moveTo((100, 100))
# line to from the previous point to a new point
lineTo((100, 900))
lineTo((900, 900))

# curve to a point with two given handles
curveTo((900, 500), (500, 100), (100, 100))

# close the path
closePath()
# draw the path
drawPath()

clipPath(path=None)
Use the given path as a clipping path, or the current path if no path was given.

Everything drawn after a clipPath() call will be clipped by the clipping path. To "undo" the clipping later, make sure you do the clipping inside a with savedState(): block, as shown in the example.

# create a bezier path
path = BezierPath()
# draw a triangle
# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((100, 900))
path.lineTo((900, 900))
# close the path
path.closePath()
# save the graphics state so the clipping happens only
# temporarily
with savedState():
    # set the path as a clipping path
    clipPath(path)
    # the oval will be clipped inside the path
    oval(100, 100, 800, 800)
# no more clipping here

strokeWidth(value)
Sets stroke width.

# set no fill
fill(None)
# set black as the stroke color
stroke(0)
# loop over a range of 10
for i in range(20):
    # in each loop set the stroke width
    strokeWidth(i)
    # draw a line
    line((100, 100), (200, 900))
    # and translate the canvas
    translate(30, 0)

miterLimit(value)
Set a miter limit. Used on corner points.

# create a path
path = BezierPath()
# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((150, 700))
path.lineTo((300, 100))
# set stroke color to black
stroke(0)
# set no fill
fill(None)
# set the width of the stroke
strokeWidth(50)
# draw the path
drawPath(path)
# move the canvas
translate(500, 0)
# set a miter limit
miterLimit(5)
# draw the same path again
drawPath(path)

lineJoin(value)
Set a line join.

Possible values are miter, round and bevel.

# set the stroke color to black
stroke(0)
# set no fill
fill(None)
# set a stroke width
strokeWidth(30)
# set a miter limit
miterLimit(30)
# create a bezier path
path = BezierPath()
# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((100, 600))
path.lineTo((160, 100))
# set a line join style
lineJoin("miter")
# draw the path
drawPath(path)
# translate the canvas
translate(300, 0)
# set a line join style
lineJoin("round")
# draw the path
drawPath(path)
# translate the canvas
translate(300, 0)
# set a line join style
lineJoin("bevel")
# draw the path
drawPath(path)

lineCap(value)
Set a line cap.

Possible values are butt, square and round.

# set stroke color to black
stroke(0)
# set a strok width
strokeWidth(50)
# translate the canvas
translate(150, 50)
# set a line cap style
lineCap("butt")
# draw a line
line((0, 200), (0, 800))
# translate the canvas
translate(300, 0)
# set a line cap style
lineCap("square")
# draw a line
line((0, 200), (0, 800))
# translate the canvase
translate(300, 0)
# set a line cap style
lineCap("round")
# draw a line
line((0, 200), (0, 800))

lineDash(*value)
Set a line dash with any given amount of lenghts. Uneven lenghts will have a visible stroke, even lenghts will be invisible.

# set stroke color to black
stroke(0)
# set a strok width
strokeWidth(50)
# translate the canvas
translate(150, 50)
# set a line dash
lineDash(2, 2)
# draw a line
line((0, 200), (0, 800))
# translate the canvas
translate(300, 0)
# set a line dash
lineDash(2, 10, 5, 5)
# draw a line
line((0, 200), (0, 800))
# translate the canvase
translate(300, 0)
# reset the line dash
lineDash(None)
# draw a line
line((0, 200), (0, 800))


### COLORS

## Fill

Set a fill before drawing a shape.

fill(r=None, g=None, b=None, alpha=1)
Sets the fill color with a red, green, blue and alpha value. Each argument must a value float between 0 and 1.

fill(1, 0, 0, .5)
# draw a rect
rect(10, 10, 200, 980)

# only set a gray value
fill(0)
# draw a rect
rect(200, 10, 200, 980)

# only set a gray value with an alpha
fill(0, .5)
# draw a rect
rect(400, 10, 200, 980)

# set rgb with no alpha
fill(1, 0, 0)
# draw a rect
rect(600, 10, 200, 980)

# set rgb with an alpha value
fill(1, 0, 0, .5)
# draw a rect
rect(800, 10, 190, 980)

linearGradient(startPoint=None, endPoint=None, colors=None, locations=None)
A linear gradient fill with:

startPoint as (x, y)
endPoint as (x, y)
colors as a list of colors, described similary as fill
locations of each color as a list of floats. (optionally)
Setting a gradient will ignore the fill.

# set a gradient as the fill color
linearGradient(
    (100, 100),                         # startPoint
    (800, 800),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
    )
# draw a rectangle
rect(10, 10, 980, 980)

radialGradient(startPoint=None, endPoint=None, colors=None, locations=None, startRadius=0, endRadius=100)
A radial gradient fill with:

startPoint as (x, y)
endPoint as (x, y)
colors as a list of colors, described similary as fill
locations of each color as a list of floats. (optionally)
startRadius radius around the startPoint in degrees (optionally)
endRadius radius around the endPoint in degrees (optionally)
Setting a gradient will ignore the fill.

# set a gradient as the fill color
radialGradient(
    (300, 300),                         # startPoint
    (600, 600),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .2, 1],                         # locations
    0,                                  # startRadius
    500                                 # endRadius
    )
# draw a rectangle
rect(10, 10, 980, 980)

shadow(offset, blur=None, color=None)
Adds a shadow with an offset (x, y), blur and a color. The color argument must be a tuple similarly as fill. The offset`and `blur argument will be drawn independent of the current context transformations.

# a red shadow with some blur and a offset
shadow((100, 100), 100, (1, 0, 0))
# draw a rect
rect(100, 100, 600, 600)

## Stroke

Set a stroke before drawing a shape.

stroke(r=None, g=None, b=None, alpha=1)
Sets the stroke color with a red, green, blue and alpha value. Each argument must a value float between 0 and 1.

# set the fill to none
fill(None)
# set a stroke width
stroke(1, 0, 0, .3)
strokeWidth(10)
# draw a rect
rect(10, 10, 180, 980)

# only set a gray value
stroke(0)
# draw a rect
rect(210, 10, 180, 980)

# only set a gray value with an alpha
stroke(0, .5)
# draw a rect
rect(410, 10, 180, 980)

# set rgb with no alpha
stroke(1, 0, 0)
# draw a rect
rect(610, 10, 180, 980)

# set rgb with an alpha value
stroke(1, 0, 0, .5)
# draw a rect
rect(810, 10, 180, 980)

## CMYK Fill

Set a fill before drawing a shape. A cmyk color used while exporting to a .pdf or an image. Handy if the file is used for print.

cmykFill(c, m=None, y=None, k=None, alpha=1)
Set a fill using a CMYK color before drawing a shape. This is handy if the file is intended for print.

Sets the CMYK fill color. Each value must be a float between 0.0 and 1.0.

# cyan
cmykFill(1, 0, 0, 0)
rect(0, 0, 250, 1000)
# magenta
cmykFill(0, 1, 0, 0)
rect(250, 0, 250, 1000)
# yellow
cmykFill(0, 0, 1, 0)
rect(500, 0, 250, 1000)
# black
cmykFill(0, 0, 0, 1)
rect(750, 0, 250, 1000)

cmykLinearGradient(startPoint=None, endPoint=None, colors=None, locations=None)
A cmyk linear gradient fill with:

startPoint as (x, y)
endPoint as (x, y)
colors as a list of colors, described similary as cmykFill
locations of each color as a list of floats. (optionally)
Setting a gradient will ignore the fill.

# set a gradient as the fill color
cmykLinearGradient(
    (100, 100),                                  # startPoint
    (800, 800),                                  # endPoint
    [(1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0)],  # colors
    [0, .2, 1]                                   # locations
    )
# draw a rectangle
rect(10, 10, 980, 980)

cmykRadialGradient(startPoint=None, endPoint=None, colors=None, locations=None, startRadius=0, endRadius=100)
A cmyk radial gradient fill with:

startPoint as (x, y)
endPoint as (x, y)
colors as a list of colors, described similary as cmykFill
locations of each color as a list of floats. (optionally)
startRadius radius around the startPoint in degrees (optionally)
endRadius radius around the endPoint in degrees (optionally)
Setting a gradient will ignore the fill.

# set a gradient as the fill color
cmykRadialGradient(
    (300, 300),                                     # startPoint
    (600, 600),                                     # endPoint
    [(1, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, .2)],    # colors
    [0, .2, 1],                                     # locations
    0,                                              # startRadius
    500                                             # endRadius
    )
# draw a rectangle
rect(10, 10, 980, 980)

cmykShadow(offset, blur=None, color=None)
Adds a cmyk shadow with an offset (x, y), blur and a color. The color argument must be a tuple similarly as cmykFill.

# a cyan with some blur and a offset
cmykShadow((100, 100), 100, (1, 0, 0, 0))
# draw a rect
rect(100, 100, 600, 600)

## CMYK Stroke

cmykStroke(c, m=None, y=None, k=None, alpha=1)
Set a stroke using a CMYK color before drawing a shape. This is handy if the file is intended for print.

Sets the CMYK stroke color. Each value must be a float between 0.0 and 1.0.

# define x, y and the amount of lines needed
x, y = 20, 20
lines = 49
# calculate the smallest step
colorStep = 1.00 / lines
# set stroke width
strokeWidth(10)
# start a loop
for i in range(lines):
    # set a cmyk color
    # the magenta value is calculated
    cmykStroke(0, i * colorStep, 1, 0)
    # draw a line
    line((x, y), (x, y + 960))
    # translate the canvas
    translate(20, 0)

### Canvas

## Page

newPage(width=None, height=None)
Create a new canvas to draw in. This will act like a page in a pdf or a frame in a mov.

Optionally a width and height argument can be provided to set the size. If not provided the default size will be used.

Alternatively size('A4') with a supported papersizes or size('screen') setting the current screen size as size, can be used.

# loop over a range of 100
for i in range(100):
    # for each loop create a new path
    newPage(500, 500)
    # set a random fill color
    fill(random(), random(), random())
    # draw a rect with the size of the page
    rect(0, 0, width(), height())

All supported papersizes: 10x14, 10x14Landscape, A0, A0Landscape, A1, A1Landscape, A2, A2Landscape, A3, A3Landscape, A4, A4Landscape, A4Small, A4SmallLandscape, A5, A5Landscape, B4, B4Landscape, B5, B5Landscape, Executive, ExecutiveLandscape, Folio, FolioLandscape, Ledger, LedgerLandscape, Legal, LegalLandscape, Letter, LetterLandscape, LetterSmall, LetterSmallLandscape, Quarto, QuartoLandscape, Statement, StatementLandscape, Tabloid, TabloidLandscape.

newDrawing()
Reset the drawing stack to the clean and empty stack.

# draw a rectangle
rect(10, 10, width()-20, height()-20)
# save it as a pdf
saveImage("~/Desktop/aRect.pdf")

# reset the drawing stack to a clear and empty stack
newDrawing()

# draw an oval
oval(10, 10, width()-20, height()-20)
# save it as a pdf
saveImage("~/Desktop/anOval.pdf")

endDrawing()
Explicitly tell drawBot the drawing is done. This is advised when using drawBot as a standalone module.

Size
size(width, height=None)
Set the width and height of the canvas. Without calling size() the default drawing board is 1000 by 1000 points.

Alternatively size('A4') with a supported papersizes or size('screen') setting the current screen size as size, can be used.

Afterwards the functions width() and height() can be used for calculations.

You have to use size() before any drawing-related code, and you can't use size() in a multi-page document. Use newPage(w, h) to set the correct dimensions for each page.

# set a canvas size
size(200, 200)
# print out the size of the page
print((width(), height()))

# set a color
fill(1, 0, 0)
# use those variables to set a background color
rect(0, 0, width(), height())

All supported papersizes: 10x14, 10x14Landscape, A0, A0Landscape, A1, A1Landscape, A2, A2Landscape, A3, A3Landscape, A4, A4Landscape, A4Small, A4SmallLandscape, A5, A5Landscape, B4, B4Landscape, B5, B5Landscape, Executive, ExecutiveLandscape, Folio, FolioLandscape, Ledger, LedgerLandscape, Legal, LegalLandscape, Letter, LetterLandscape, LetterSmall, LetterSmallLandscape, Quarto, QuartoLandscape, Statement, StatementLandscape, Tabloid, TabloidLandscape.

sizes(paperSize=None)
Returns the width and height of a specified canvas size. If no canvas size is given it will return the dictionary containing all possible page sizes.

Page Attributes
width()
Returns the width of the current page.

height()
Returns the height of the current page.

pageCount()
Returns the current page count.

pages()
Return all pages.

# set a size
size(200, 200)
# draw a rectangle
rect(10, 10, 100, 100)
# create a new page
newPage(200, 300)
# set a color
fill(1, 0, 1)
# draw a rectangle
rect(10, 10, 100, 100)
# create a new page
newPage(200, 200)
# set a color
fill(0, 1, 0)
# draw a rectangle
rect(10, 10, 100, 100)

# get all pages
allPages = pages()
# count how many pages are available
print(len(allPages))

# use the `with` statement
# to set a page as current context
with allPages[1]:
    # draw into the selected page
    fontSize(30)
    text("Hello World", (10, 150))

# loop over allpages
for page in allPages:
    # set the page as current context
    with page:
        # draw an oval in each of them
        oval(110, 10, 30, 30)

frameDuration(seconds)
When exporting to mov or gif each frame can have duration set in seconds.

# setting some variables
# size of the pages / frames
w, h = 200, 200
# frame per seconds
fps = 30
# duration of the movie
seconds = 3
# calculate the lenght of a single frame
duration = 1 / fps
# calculate the amount of frames needed
totalFrames = seconds * fps

# title page
newPage(w, h)
# set frame duration to 1 second
frameDuration(1)
# pick a font and font size
font("Helvetica", 40)
# draw the title text in a box
textBox("Rotated square", (0, 0, w, h * .8), align="center")

# loop over the amount of frames needed
for i in range(totalFrames):
    # create a new page
    newPage(w, h)
    # set the frame duration
    frameDuration(duration)
    # set a fill color
    fill(1, 0, 0)
    # translate to the center of the page
    translate(w / 2, h / 2)
    # rotate around the center
    rotate(i*10)
    # draw the rect
    rect(-50, -50, 50, 50)

# save the image as a mov on the desktop
saveImage('~/Desktop/frameDuration.gif')

linkURL(url, (x, y, w, h))
Add a clickable rectangle for an external url link.

The link rectangle will be set independent of the current context transformations.

linkRect(name, (x, y, w, h))
Add a clickable rectangle for a link within a PDF. Use linkDestination(name, (x, y)) with the same name to set the destination of the clickable rectangle.

The link rectangle will be set independent of the current context transformations.

# a variable with the amount of pages we want
totalPages = 10
# create the first page with a index
newPage()
# set a font size
fontSize(30)
# start a loop over all wanted pages
for i in range(totalPages):
    # set a random fill color
    fill(random(), random(), random())
    # draw a rectangle
    rect(10, 50 * i, 50, 50)
    # add a clickable link rectangle with a unique name
    linkRect(f"beginPage_{i}", (10, 10 + 50 * i, 50, 50))

# start a loop over all wanted pages
for i in range(totalPages):
    # create a new page
    newPage()
    # add a link destination with a given name
    # the name must refer to a linkRect name
    linkDestination(f"beginPage_{i}", (0, 0))

linkDestination(name, (x, y))
Add a destination point for a link within a PDF. Setup a clickable retangle with linkRect(name, (x, y, w, h)) with the same name.

The destination position will be set independent of the current context transformations.

## Transformations
translate(x=0, y=0)
Translate the canvas with a given offset.

rotate(angle, center=(0, 0))
Rotate the canvas around the center point (which is the origin by default) with a given angle in degrees.

scale(x=1, y=None, center=(0, 0))
Scale the canvas with a given x (horizontal scale) and y (vertical scale).

If only 1 argument is provided a proportional scale is applied.

The center of scaling can optionally be set via the center keyword argument. By default this is the origin.

skew(angle1, angle2=0, center=(0, 0))
Skew the canvas with given angle1 and angle2.

If only one argument is provided a proportional skew is applied.

The center of skewing can optionally be set via the center keyword argument. By default this is the origin.

transform((xx, xy, yx, yy, x, y))
Transform the canvas with a transformation matrix.

Managing the Graphics State
savedState()
Save and restore the current graphics state in a with statement.

# Use the 'with' statement.
# This makes any changes you make to the graphics state -- such as
# colors and transformations -- temporary, and will be reset to
# the previous state at the end of the 'with' block.
with savedState():
    # set a color
    fill(1, 0, 0)
    # do a transformation
    translate(450, 50)
    rotate(45)
    # draw something
    rect(0, 0, 700, 600)
# already returned to the previously saved graphics state
# so this will be a black rectangle
rect(0, 0, 50, 50)
Open in DrawBot: savedState.py
Download: savedState.py

save()
DrawBot strongly recommends to use savedState() in a with statement instead.

Save the current graphics state. This will save the state of the canvas (with all the transformations) but also the state of the colors, strokes…

restore()
DrawBot strongly recommends to use savedState() in a with statement instead.

Restore from a previously saved graphics state. This will restore the state of the canvas (with all the transformations) but also the state of colors, strokes…

## Saving
saveImage(paths, **options)
Save or export the canvas to a specified format. The path argument is a single destination path to save the current drawing actions.

The file extension is important because it will determine the format in which the image will be exported.

All supported file extensions: pdf, png, jpg, jpeg, tif, tiff, svg, gif, bmp, mp4, icns, *, PIL, NSImage. (* will print out all actions.)

When exporting an animation or movie, each page represents a frame and the framerate is set by calling frameDuration() after each newPage().

# set the canvas size
size(150, 100)

# draw a background
rect(10, 10, width()-20, height()-20)

# set a fill
fill(1)
# draw some text
text("Hello World!", (20, 40))
# save it as a png and pdf on the current users desktop
saveImage("~/Desktop/firstImage.png")
saveImage("~/Desktop/firstImage.pdf")
Open in DrawBot: saveImage.py
Download: saveImage.py

saveImage() options can be set by adding keyword arguments. Which options are recognized depends on the output format.

pdf options:

multipage: If False, only the last page in the document will be saved into the output PDF. This value is ignored if it is None (default).
png options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
imagePNGGamma: The gamma value for the image. It is a floating-point number between 0.0 and 1.0, with 0.0 being black and 1.0 being the maximum color.
imagePNGInterlaced: Boolean value that indicates whether the image should be interlaced.
imageColorSyncProfileData: A bytes or NSData object containing the ColorSync profile data.
jpg, jpeg options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
imageJPEGCompressionFactor: A float between 0.0 and 1.0, with 1.0 resulting in no compression and 0.0 resulting in the maximum compression possible
imageJPEGProgressive: Boolean that indicates whether the image should use progressive encoding.
imageFallbackBackgroundColor: The background color to use when writing to an image format (such as JPEG) that doesn't support alpha. The color's alpha value is ignored. The default background color, when this property is not specified, is white. The value of the property should be an NSColor object or a DrawBot RGB color tuple.
imageColorSyncProfileData: A bytes or NSData object containing the ColorSync profile data.
tif, tiff options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
imageTIFFCompressionMethod: None, or 'lzw' or 'packbits', or an NSTIFFCompression constant
imageColorSyncProfileData: A bytes or NSData object containing the ColorSync profile data.
svg options:

multipage: Output a numbered svg file for each page or frame in the document.
gif options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
imageGIFDitherTransparency: Boolean that indicates whether the image is dithered
imageGIFRGBColorTable: A bytes or NSData object containing the RGB color table.
imageColorSyncProfileData: A bytes or NSData object containing the ColorSync profile data.
imageGIFLoop: Boolean that indicates whether the animated gif should loop
bmp options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
mp4 options:

ffmpegCodec: The codec to be used by ffmpeg. By default it is 'libx264' (for H.264). The 'mpeg4' codec gives better results when importing the movie into After Effects, at the expense of a larger file size.
imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
imagePNGGamma: The gamma value for the image. It is a floating-point number between 0.0 and 1.0, with 0.0 being black and 1.0 being the maximum color.
imagePNGInterlaced: Boolean value that indicates whether the image should be interlaced.
imageColorSyncProfileData: A bytes or NSData object containing the ColorSync profile data.
icns options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
PIL options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
NSImage options:

imageResolution: The resolution of the output image in PPI. Default is 72.
antiAliasing: Indicate if a the image should be rendedered with anti-aliasing. Default is True.
multipage: Output a numbered image for each page or frame in the document.
# same example but we just change the image resolution
size(150, 100)
rect(10, 10, width()-20, height()-20)
fill(1)
text("Hello World!", (20, 40))
# save it with an option that controls the resolution (300 PPI)
saveImage("~/Desktop/firstImage300.png", imageResolution=300)
Open in DrawBot: saveImageResolutionExample.py
Download: saveImageResolutionExample.py

printImage(pdf=None)
Export the canvas to a printing dialog, ready to print.

Optionally a pdf object can be provided.

# set A4 page size
size(595, 842)
# draw something
oval(0, 0, width(), height())
# send it to the printer
printImage()
Open in DrawBot: printImage.py
Download: printImage.py

pdfImage()
Return the image as a pdf document object.

### Text

Drawing Text
text(txt, (x, y), align=None)
Draw a text at a provided position.

Optionally an alignment can be set. Possible align values are: "left", "center" and "right".

The default alignment is left.

Optionally txt can be a FormattedString.

# set a font and font size
font("Times-Italic", 200)
# draw text
text("hallo", (200, 600))
text("I'm Times", (100, 300))
Open in DrawBot: text.py
Download: text.py

textBox(txt, box, align=None)
Draw a text in a provided rectangle.

A box could be a (x, y, w, h) or a bezierPath object.

Optionally an alignment can be set. Possible align values are: "left", "center", "right" and "justified".

If the text overflows the rectangle, the overflowed text is returned.

The default alignment is left.

# a box has an x, y, width and height
x, y, w, h = 100, 100, 800, 800
# set a fill
fill(1, 0, 0)
# draw a rectangle with variables from above
rect(x, y, w, h)
# set a diferent fill
fill(1)
# set a font size
fontSize(200)
# draw text in a text box
# with varibales from above
overflow = textBox("hallo, this text is a bit to long",
                (x, y, w, h), align="center")
# a text box returns text overflow
# text that did not make it into the box
print(overflow)
Open in DrawBot: textBox.py
Download: textBox.py

The returned overflow can be used to add new pages until all text is set:

t = '''DrawBot is a powerful, free application for MacOSX that invites you to write simple Python scripts to generate two-dimensional graphics. The builtin graphics primitives support rectangles, ovals, (bezier) paths, polygons, text objects and transparency.
DrawBot is an ideal tool to teach the basics of programming. Students get colorful graphic treats while getting familiar with variables, conditional statements, functions and what have you. Results can be saved in a selection of different file formats, including as high resolution, scaleable PDF.
DrawBot has proven itself as part of the curriculum at selected courses at the Royal Academy in The Hague.'''

# setting some variables
# setting the size
x, y, w, h = 10, 10, 480, 480

# setting the color change over different frames
coloradd = .1

# setting the start background color only red and blue
r = .3
b = 1

# start a loop and run as long there is t variable has some text
while len(t):
    # create a new page
    newPage(500, 500)
    # set a frame duration
    frameDuration(3)
    # set the background fill
    fill(r, 0, b)
    # draw the background
    rect(x, y, w, h)
    # set a fill color
    fill(0)
    # set a font with a size
    font("DrawBot-Bold", randint(50, 100))
    # pick some random colors
    rr = random()
    gg = random()
    bb = random()
    # set a gradient as fill
    radialGradient((250, 250), (250, 250), [(rr, gg, bb), (1-rr, 1-gg, 1-bb)], startRadius=0, endRadius=250)

    # draw the text in a box with the gradient fill
    t = textBox(t, (x, y, w, h))

    # setting the color for the next frame
    r += coloradd
    b -= coloradd

    # set a font
    font("DrawBot-Bold", 20)
    # get the page count text size as a (width, height) tuple
    tw, th = textSize("%s" % pageCount())
    # draw the text
    textBox("%s" % pageCount(), (10, 10, 480, th), align="center")

saveImage("~/Desktop/drawbot.mp4")
Open in DrawBot: overflowText.py
Download: overflowText.py

Another example, this time using a bezierPath as a text envelope:

# create a fresh bezier path
path = BezierPath()
# draw some text
# the text will be converted to curves
path.text("a", font="Helvetica-Bold", fontSize=500)
# set an indent
indent = 50
# calculate the width and height of the path
minx, miny, maxx, maxy = path.bounds()
w = maxx - minx
h = maxy - miny
# calculate the box where we want to draw the path in
boxWidth = width() - indent * 2
boxHeight = height() - indent * 2
# calculate a scale based on the given path bounds and the box
s = min([boxWidth / float(w), boxHeight / float(h)])
# translate to the middle
translate(width()*.5, height()*.5)
# set the scale
scale(s)
# translate the negative offset, letter could have overshoot
translate(-minx, -miny)
# translate with half of the width and height of the path
translate(-w*.5, -h*.5)
# draw the path
drawPath(path)
# set a font
font("Helvetica-Light")
# set a font size
fontSize(5)
# set white as color
fill(1)
# draw some text in the path
textBox("abcdefghijklmnopqrstuvwxyz"*30000, path)

Helpers
textSize(txt, align=None, width=None, height=None)
Returns the size of a text with the current settings, like font, fontSize and lineHeight as a tuple (width, height).

Optionally a width constrain or height constrain can be provided to calculate the lenght or width of text with the given constrain.

textOverflow(txt, box, align=None)
Returns the overflowed text without drawing the text.

A box could be a (x, y, w, h) or a bezierPath object.

Optionally an alignment can be set. Possible align values are: "left", "center", "right" and "justified".

The default alignment is left.

Optionally txt can be a FormattedString. Optionally box can be a BezierPath.

textBoxBaselines(txt, box, align=None)
Returns a list of x, y coordinates indicating the start of each line for a given text in a given box.

A box could be a (x, y, w, h) or a bezierPath object.

Optionally an alignment can be set. Possible align values are: "left", "center", "right" and "justified".

textBoxCharacterBounds(txt, box, align=None)
Returns a list of typesetted bounding boxes ((x, y, w, h), baseLineOffset, formattedSubString).

A box could be a (x, y, w, h) or a bezierPath object.

Optionally an alignment can be set. Possible align values are: "left", "center", "right" and "justified".

installedFonts(supportsCharacters=None)
Returns a list of all installed fonts.

Optionally a string with supportsCharacters can be provided, the list of available installed fonts will be filtered by support of these characters,

installFont(path)
Install a font with a given path and the postscript font name will be returned. The postscript font name can be used to set the font as the active font.

Fonts are installed only for the current process. Fonts will not be accesible outside the scope of drawBot.

All installed fonts will automatically be uninstalled when the script is done.

# set the path to a font file
path = "path/to/font/file.otf"
# install the font
fontName = installFont(path)
# set the font
font(fontName, 200)
# draw some text
text("Hello World", (10, 10))
# uninstall font
uninstallFont(path)
Open in DrawBot: installFont.py
Download: installFont.py

This function has been deprecated: please use the font path directly in all places that accept a font name.

uninstallFont(path)¶
Uninstall a font with a given path.

This function has been deprecated: please use the font path directly in all places that accept a font name.

Text Properties
font(fontNameOrPath, fontSize=None, fontNumber=0)
Set a font with the name of the font. If a font path is given the font will be installed and used directly. Optionally a fontSize can be set directly. The default font, also used as fallback font, is 'LucidaGrande'. The default fontSize is 10pt.

The name of the font relates to the font's postscript name.

The font name is returned, which is handy when the font was loaded from a path.

font("Times-Italic")
fontSize(fontSize)
Set the font size in points. The default fontSize is 10pt.

fontSize(30)
fallbackFont(fontNameOrPath, fontNumber=0)
Set a fallback font, this is used whenever a glyph is not available in the current font.

fallbackFont("Times")
underline(value)
Set the underline value. Underline must be single, thick, double or None.

underline("single")
fontSize(140)
text("hello underline", (50, 50))
Open in DrawBot: underline.py
Download: underline.py

hyphenation(value)
Set hyphenation, True or False.

txt = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum.'''
# enable hyphenation
hyphenation(True)
# set font size
fontSize(50)
# draw text in a box
textBox(txt, (100, 100, 800, 800))
Open in DrawBot: hyphenation.py
Download: hyphenation.py

lineHeight(value)
Set the line height.

# set line height
lineHeight(150)
# set font size
fontSize(60)
# draw text in a box
textBox("Hello World " * 10, (100, 100, 800, 800))
Open in DrawBot: lineHeight.py
Download: lineHeight.py

tracking(value)
Set the tracking between characters. It adds an absolute number of points between the characters.

size(1000, 350)
# set tracking
tracking(100)
# set font size
fontSize(100)
# draw some text
text("hello", (100, 200))
# disable tracking
tracking(None)
# draw some text
text("world", (100, 100))
Open in DrawBot: tracking.py
Download: tracking.py

baselineShift(value)
Set the shift of the baseline.

openTypeFeatures(frac=True, case=True, ...)
Enable OpenType features.

Supported OpenType tags:

c2pc, c2sc, calt, case, cpsp, cswh, dlig, frac, liga, kern, lnum, onum, ordn, pnum, rlig, sinf, smcp, ss01, ss02, ss03, ss04, ss05, ss06, ss07, ss08, ss09, ss10, ss11, ss12, ss13, ss14, ss15, ss16, ss17, ss18, ss19, ss20, subs, sups, swsh, titl, tnum
A resetFeatures argument can be set to True in order to get back to the default state.

newPage(1000, 300)
# set a font
font("Didot")
# set the font size
fontSize(50)
# create a string
someTxt = "aabcde1234567890"
# draw the string
text(someTxt, (100, 220))
# enable some OpenType features
openTypeFeatures(onum=True, smcp=True)
# draw the same string
text(someTxt, (100, 150))
# reset defaults
openTypeFeatures(resetFeatures=True)
# the same string again, back to default features
text(someTxt, (100, 70))
Open in DrawBot: openTypeFeatures.py
Download: openTypeFeatures.py

listOpenTypeFeatures(fontNameOrPath=None)
List all OpenType feature tags for the current font.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

fontVariations(wdth=0.6, wght=0.1, ...)
Pick a variation by axes values.

size(1000, 500)
# pick a font
font("Skia")
# pick a font size
fontSize(200)
# list all axis from the current font
for axis, data in listFontVariations().items():
    print((axis, data))
# pick a variation from the current font
fontVariations(wght=.6)
# draw text!!
text("Hello Q", (100, 100))
# pick a variation from the current font
fontVariations(wght=3, wdth=1.2)
# draw text!!
text("Hello Q", (100, 300))
Open in DrawBot: fontVariations.py
Download: fontVariations.py

listFontVariations(fontNameOrPath=None)
List all variation axes for the current font.

Returns a dictionary with all axis tags instance with an info dictionary with the following keys: name, minValue and maxValue. For non variable fonts an empty dictionary is returned.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

listNamedInstances(fontNameOrPath=None)
List all named instances from a variable font for the current font.

Returns a dictionary with all named instance as postscript names with their location. For non variable fonts an empty dictionary is returned.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

tabs(*tabs)
Set tabs, tuples of (float, alignment) Aligment can be "left", "center", "right" or any other character. If a character is provided the alignment will be right and centered on the specified character.

t = " hello w o r l d"
# replace all spaces by tabs
t = t.replace(" ", "\t")
# set some tabs
tabs((85, "center"), (232, "right"), (300, "left"))
# draw the string
text(t, (10, 10))
# reset all tabs
tabs(None)
# draw the same string
text(t, (10, 50))
Open in DrawBot: tabs.py
Download: tabs.py

language(language)
Set the preferred language as language tag or None to use the default language.

Support is depending on local OS.

language() will activate the locl OpenType features, if supported by the current font.

size(1000, 600)
# a long dutch word
word = "paardenkop"
# a box where we draw in
box = (100, 50, 400, 500)
# set font size
fontSize(118)
# enable hyphenation
hyphenation(True)
# draw the text with no language set
textBox(word, box)
# set language to dutch (nl)
language("nl")
# shift up a bit
translate(500, 0)
# darw the text again with a language set
textBox(word, box)
Open in DrawBot: language.py
Download: language.py

Font Properties
fontContainsCharacters(characters)
Return a bool if the current font contains the provided characters. Characters is a string containing one or more characters.

fontContainsGlyph(glyphName)
Return a bool if the current font contains a provided glyph name.

fontFilePath()
Return the path to the file of the current font.

listFontGlyphNames()
Return a list of glyph names supported by the current font.

fontDescender()
Returns the current font descender, based on the current font and fontSize.

fontAscender()
Returns the current font ascender, based on the current font and fontSize.

fontXHeight()
Returns the current font x-height, based on the current font and fontSize.

fontCapHeight()
Returns the current font cap height, based on the current font and fontSize.

fontLeading()
Returns the current font leading, based on the current font and fontSize.

fontLineHeight()
Returns the current line height, based on the current font and fontSize. If a lineHeight is set, this value will be returned.

txt = "Hello World"
x, y = 10, 100

# set a font
font("Helvetica")
# set a font size
fontSize(100)
# draw the text
text(txt, (x, y))

# calculate the size of the text
textWidth, textHeight = textSize(txt)

# set a red stroke color
stroke(1, 0, 0)
# loop over all font metrics
for metric in (0, fontDescender(), fontAscender(), fontXHeight(), fontCapHeight()):
    # draw a red line with the size of the drawn text
    line((x, y+metric), (x+textWidth, y+metric))

Formatted Strings
FormattedString(txt=None, font=None, fontSize=10, fallbackFont=None, fill=(0, 0, 0), cmykFill=None, stroke=None, cmykStroke=None, strokeWidth=1, align=None, lineHeight=None, tracking=None, baselineShift=None, openTypeFeatures=None, tabs=None, language=None, indent=None, tailIndent=None, firstLineIndent=None, paragraphTopSpacing=None, paragraphBottomSpacing=None)
Return a string object that can handle text formatting.

size(1000, 200)
# create a formatted string
txt = FormattedString()

# adding some text with some formatting
txt.append("hello", font="Helvetica", fontSize=100, fill=(1, 0, 0))
# adding more text
txt.append("world", font="Times-Italic", fontSize=50, fill=(0, 1, 0))

# setting a font
txt.font("Helvetica-Bold")
txt.fontSize(75)
txt += "hello again"

# drawing the formatted string
text(txt, (10, 30))


# create a formatted string
txt = FormattedString()

# adding some text with some formatting
txt.append("hello", font="Didot", fontSize=50)
# adding more text with an
txt.append("world", font="Didot", fontSize=50, openTypeFeatures=dict(smcp=True))

text(txt, (10, 150))
Open in DrawBot: formattedString.py
Download: formattedString.py

class FormattedString(txt=None, **kwargs)
Bases: drawBot.context.baseContext.SVGContextPropertyMixin, drawBot.context.baseContext.ContextPropertyMixin

FormattedString is a reusable object, if you want to draw the same over and over again. FormattedString objects can be drawn with the text(txt, (x, y)) and textBox(txt, (x, y, w, h)) methods.

clear()
append(txt, **kwargs)
Add txt to the formatted string with some additional text formatting attributes:

font: the font to be used for the given text, if a font path is given the font will be installed and used directly.
fallbackFont: the fallback font
fontSize: the font size to be used for the given text
fill: the fill color to be used for the given text
cmykFill: the cmyk fill color to be used for the given text
stroke: the stroke color to be used for the given text
cmykStroke: the cmyk stroke color to be used for the given text
strokeWidth: the strokeWidth to be used for the given text
align: the alignment to be used for the given text
lineHeight: the lineHeight to be used for the given text
tracking: set tracking for the given text in absolute points
baselineShift: set base line shift for the given text
openTypeFeatures: enable OpenType features
fontVariations: pick a variation by axes values
tabs: enable tabs
indent: the indent of a paragraph
tailIndent: the tail indent of a paragraph
firstLineIndent: the first line indent of a paragraph
paragraphTopSpacing: the spacing at the top of a paragraph
paragraphBottomSpacing: the spacing at the bottom of a paragraph
language: the language of the text
All formatting attributes follow the same notation as other similar DrawBot methods. A color is a tuple of (r, g, b, alpha), and a cmykColor is a tuple of (c, m, y, k, alpha).

Text can also be added with formattedString += "hello". It will append the text with the current settings of the formatted string.

font(fontNameOrPath, fontSize=None, fontNumber=0)
Set a font with the name of the font. If a font path is given the font will used directly. Optionally a fontSize can be set directly. The default font, also used as fallback font, is 'LucidaGrande'. The default fontSize is 10pt.

The name of the font relates to the font's postscript name.

The font name is returned, which is handy when the font was loaded from a path.

fontNumber(fontNumber)
fallbackFont(fontNameOrPath, fontNumber=0)
Set a fallback font, used whenever a glyph is not available in the normal font. If a font path is given the font will be installed and used directly.

fallbackFontNumber(fontNumber)
fontSize(fontSize)
Set the font size in points. The default fontSize is 10pt.

fill(*fill)
Sets the fill color with a red, green, blue and alpha value. Each argument must a value float between 0 and 1.

stroke(*stroke)
Sets the stroke color with a red, green, blue and alpha value. Each argument must a value float between 0 and 1.

cmykFill(*cmykFill)
Set a fill using a CMYK color before drawing a shape. This is handy if the file is intended for print.

Sets the CMYK fill color. Each value must be a float between 0.0 and 1.0.

cmykStroke(*cmykStroke)
Set a stroke using a CMYK color before drawing a shape. This is handy if the file is intended for print.

Sets the CMYK stroke color. Each value must be a float between 0.0 and 1.0.

strokeWidth(strokeWidth)
Sets stroke width.

align(align)
Sets the text alignment. Possible align values are: left, center and right.

lineHeight(lineHeight)
Set the line height.

tracking(tracking)
Set the tracking between characters. It adds an absolute number of points between the characters.

baselineShift(baselineShift)
Set the shift of the baseline.

underline(underline)
Set the underline value. Underline must be single, thick, double or None.

url(url)
set the url value. url must be a string or None

openTypeFeatures(*args, **features)
Enable OpenType features and return the current openType features settings.

If no arguments are given openTypeFeatures() will just return the current openType features settings.

size(1000, 200)
# create an empty formatted string object
t = FormattedString()
# set a font
t.font("Didot")
# set a font size
t.fontSize(60)
# add some text
t += "0123456789 Hello"
# enable some open type features
t.openTypeFeatures(smcp=True, onum=True)
# add some text
t += " 0123456789 Hello"
# draw the formatted string
text(t, (10, 80))
Open in DrawBot: openTypeFeaturesFormattedString.py
Download: openTypeFeaturesFormattedString.py

listOpenTypeFeatures(fontNameOrPath=None, fontNumber=0)
List all OpenType feature tags for the current font.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

fontVariations(*args, **axes)
Pick a variation by axes values and return the current font variations settings.

If no arguments are given fontVariations() will just return the current font variations settings.

listFontVariations(fontNameOrPath=None, fontNumber=0)
List all variation axes for the current font.

Returns a dictionary with all axis tags instance with an info dictionary with the following keys: name, minValue and maxValue. For non variable fonts an empty dictionary is returned.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

listNamedInstances(fontNameOrPath=None, fontNumber=0)
List all named instances from a variable font for the current font.

Returns a dictionary with all named instance as postscript names with their location. For non variable fonts an empty dictionary is returned.

Optionally a fontNameOrPath can be given. If a font path is given the font will be used directly.

tabs(*tabs)
Set tabs,tuples of (float, alignment) Aligment can be "left", "center", "right" or any other character. If a character is provided the alignment will be right and centered on the specified character.

# create a new formatted string
t = FormattedString()
# set some tabs
t.tabs((85, "center"), (232, "right"), (300, "left"))
# add text with tabs
t += " hello w o r l d".replace(" ", "\t")
# draw the string
text(t, (10, 10))
Open in DrawBot: tabsFormattedString.py
Download: tabsFormattedString.py

indent(indent)
Set indent of text left of the paragraph.

# setting up some variables
x, y, w, h = 10, 10, 500, 600

txtIndent = 100
txtFirstLineIndent = 200
txtTailIndent = -100
txtFontSize = 22

paragraphTop = 3
paragraphBottom = 10

txt = '''DrawBot is an ideal tool to teach the basics of programming. Students get colorful graphic treats while getting familiar with variables, conditional statements, functions and what have you. Results can be saved in a selection of different file formats, including as high resolution, scaleable PDF, svg, movie, png, jpeg, tiff...'''

# a new page with preset size
newPage(w+x*2, h+y*2)
# draw text indent line
stroke(1, 0, 0)
line((x+txtIndent, y), (x+txtIndent, y+h))
# draw text firstline indent line
stroke(1, 1, 0)
line((x+txtFirstLineIndent, y), (x+txtFirstLineIndent, y+h))
# draw tail indent
pos = txtTailIndent
# tail indent could be negative
if pos <= 0:
    # substract from width of the text box
    pos = w + pos
stroke(0, 0, 1)
line((x+pos, y), (x+pos, y+h))
# draw a rectangle
fill(0, .1)
stroke(None)
rect(x, y, w, h)

# create a formatted string
t = FormattedString(fontSize=txtFontSize)
# set alignment
t.align("justified")
# add text
t += txt
# add hard return
t += "\n"
# set style for indented text
t.fontSize(txtFontSize*.6)
t.paragraphTopSpacing(paragraphTop)
t.paragraphBottomSpacing(paragraphBottom)
t.firstLineIndent(txtFirstLineIndent)
t.indent(txtIndent)
t.tailIndent(txtTailIndent)
# add text
t += txt
# add hard return
t += "\n"
# reset style
t.fontSize(txtFontSize)
t.indent(None)
t.tailIndent(None)
t.firstLineIndent(None)
t.paragraphTopSpacing(None)
t.paragraphBottomSpacing(None)
# add text
t += txt
# draw formatted string in a text box
textBox(t, (x, y, w, h))
Open in DrawBot: indent.py
Download: indent.py

tailIndent(indent)
Set indent of text right of the paragraph.

If positive, this value is the distance from the leading margin. If 0 or negative, it's the distance from the trailing margin.

firstLineIndent(indent)
Set indent of the text only for the first line.

paragraphTopSpacing(value)
set paragraph spacing at the top.

paragraphBottomSpacing(value)
set paragraph spacing at the bottom.

language(language)
Set the preferred language as language tag or None to use the default language.

language() will activate the locl OpenType features, if supported by the current font.

size()
Return the size of the text.

getNSObject()
copy()
Copy the formatted string.

fontContainsCharacters(characters)
Return a bool if the current font contains the provided characters. Characters is a string containing one or more characters.

fontContainsGlyph(glyphName)
fontFilePath()
Return the path to the file of the current font.

fontFileFontNumber()
listFontGlyphNames()
Return a list of glyph names supported by the current font.

fontAscender()
Returns the current font ascender, based on the current font and fontSize.

fontDescender()
Returns the current font descender, based on the current font and fontSize.

fontXHeight()
Returns the current font x-height, based on the current font and fontSize.

fontCapHeight()
Returns the current font cap height, based on the current font and fontSize.

fontLeading()
Returns the current font leading, based on the current font and fontSize.

fontLineHeight()
Returns the current line height, based on the current font and fontSize. If a lineHeight is set, this value will be returned.

appendGlyph(*glyphNames)
Append a glyph by his glyph name or glyph index using the current font. Multiple glyph names are possible.

size(1300, 400)
# create an empty formatted string object
t = FormattedString()
# set a font
t.font("Menlo-Regular")
# set a font size
t.fontSize(300)
# add some glyphs by glyph name
t.appendGlyph("A", "ampersand", "Eng", "Eng.alt")
# add some glyphs by glyph ID (this depends heavily on the font)
t.appendGlyph(50, 51)
# draw the formatted string
text(t, (100, 100))
Open in DrawBot: appendGlyphFormattedString.py
Download: appendGlyphFormattedString.py

svgClass
The svg class, as a string.

svgID
The svg id, as a string.

svgLink
The svg link, as a string.

### Images

Drawing Images
image(path, (x, y), alpha=1, pageNumber=None)
Add an image from a path with an offset and an alpha value. This should accept most common file types like pdf, jpg, png, tiff and gif.

Optionally an alpha can be provided, which is a value between 0 and 1.

Optionally a pageNumber can be provided when the path referes to a multi page pdf file.

# the path can be a path to a file or a url
image("https://d1sz9tkli0lfjq.cloudfront.net/items/1T3x1y372J371p0v1F2Z/drawBot.jpg", (100, 100), alpha=.3)

Image Properties
imageSize(path)
Return the width and height of an image.

print(imageSize("https://d1sz9tkli0lfjq.cloudfront.net/items/1T3x1y372J371p0v1F2Z/drawBot.jpg"))
Open in DrawBot: imageSize.py
Download: imageSize.py
imagePixelColor(path, (x, y))
Return the color r, g, b, a of an image at a specified x, y possition.

# path to the image
path = u"https://d1sz9tkli0lfjq.cloudfront.net/items/1T3x1y372J371p0v1F2Z/drawBot.jpg"

# get the size of the image
w, h = imageSize(path)

# setup a variable for the font size as for the steps
s = 15

# shift it up a bit
translate(100, 100)

# set a font with a size
font("Helvetica-Bold")
fontSize(s)

# loop over the width of the image
for x in range(0, w, s):
    # loop of the height of the image
    for y in range(0, h, s):
        # get the color
        color = imagePixelColor(path, (x, y))
        if color:
            r, g, b, a = color
            # set the color
            fill(r, g, b, a)
            # draw some text
            text("W", (x, y))

imageResolution(path)
Return the image resolution for a given image.

numberOfPages(path)
Return the number of pages for a given pdf or (animated) gif.

ImageObject
ImageObject(path=None)
Return a Image object, packed with filters. This is a reusable object.

size(550, 300)
# initiate a new image object
im = ImageObject()

# draw in the image
# the 'with' statement will create a custom context
# only drawing in the image object
with im:
    # set a size for the image
    size(200, 200)
    # draw something
    fill(1, 0, 0)
    rect(0, 0, width(), height())
    fill(1)
    fontSize(30)
    text("Hello World", (10, 10))

# draw in the image in the main context
image(im, (10, 50))
# apply some filters
im.gaussianBlur()

# get the offset (with a blur this will be negative)
x, y = im.offset()
# draw in the image in the main context
image(im, (300+x, 50+y))

ImageObject
ImageObject(path=None)
Return a Image object, packed with filters. This is a reusable object.

size(550, 300)
# initiate a new image object
im = ImageObject()

# draw in the image
# the 'with' statement will create a custom context
# only drawing in the image object
with im:
    # set a size for the image
    size(200, 200)
    # draw something
    fill(1, 0, 0)
    rect(0, 0, width(), height())
    fill(1)
    fontSize(30)
    text("Hello World", (10, 10))

# draw in the image in the main context
image(im, (10, 50))
# apply some filters
im.gaussianBlur()

# get the offset (with a blur this will be negative)
x, y = im.offset()
# draw in the image in the main context
image(im, (300+x, 50+y))
Open in DrawBot: imageObject.py
Download: imageObject.py

class ImageObject(path=None)
An image object with support for filters.

Optional a path to an existing image can be provided.

For more info see: Core Image Filter Reference.

size()
Return the size of the image as a tuple.

offset()
Return the offset of the image, the origin point can change due to filters.

clearFilters()
Clear all filters.

open(path)
Open an image with a given path.

copy()
Return a copy.

lockFocus()
Set focus on image.

unlockFocus()
Set unlock focus on image.

boxBlur(radius=None)
Blurs an image using a box-shaped convolution kernel.

Attributes: radius a float.

discBlur(radius=None)
Blurs an image using a disc-shaped convolution kernel.

Attributes: radius a float.

gaussianBlur(radius=None)
Spreads source pixels by an amount specified by a Gaussian distribution.

Attributes: radius a float.

maskedVariableBlur(mask=None, radius=None)
Blurs the source image according to the brightness levels in a mask image.

Attributes: mask an Image object, radius a float.

motionBlur(radius=None, angle=None)
Blurs an image to simulate the effect of using a camera that moves a specified angle and distance while capturing the image.

Attributes: radius a float, angle a float in degrees.

noiseReduction(noiseLevel=None, sharpness=None)
Reduces noise using a threshold value to define what is considered noise.

Attributes: noiseLevel a float, sharpness a float.

zoomBlur(center=None, amount=None)
Simulates the effect of zooming the camera while capturing the image.

Attributes: center a tuple (x, y), amount a float.

colorClamp(minComponents=None, maxComponents=None)
Modifies color values to keep them within a specified range.

Attributes: minComponents a tuple (x, y, w, h), maxComponents a tuple (x, y, w, h).

colorControls(saturation=None, brightness=None, contrast=None)
Adjusts saturation, brightness, and contrast values.

Attributes: saturation a float, brightness a float, contrast a float.

colorMatrix(RVector=None, GVector=None, BVector=None, AVector=None, biasVector=None)
Multiplies source color values and adds a bias factor to each color component.

Attributes: RVector a tuple (x, y, w, h), GVector a tuple (x, y, w, h), BVector a tuple (x, y, w, h), AVector a tuple (x, y, w, h), biasVector a tuple (x, y, w, h).

colorPolynomial(redCoefficients=None, greenCoefficients=None, blueCoefficients=None, alphaCoefficients=None)
Modifies the pixel values in an image by applying a set of cubic polynomials.

Attributes: redCoefficients a tuple (x, y, w, h), greenCoefficients a tuple (x, y, w, h), blueCoefficients a tuple (x, y, w, h), alphaCoefficients a tuple (x, y, w, h).

exposureAdjust(EV=None)
Adjusts the exposure setting for an image similar to the way you control exposure for a camera when you change the F-stop.

Attributes: EV a float.

gammaAdjust(power=None)
Adjusts midtone brightness.

Attributes: power a float.

hueAdjust(angle=None)
Changes the overall hue, or tint, of the source pixels.

Attributes: angle a float in degrees.

linearToSRGBToneCurve()
Maps color intensity from a linear gamma curve to the sRGB color space.

SRGBToneCurveToLinear()
Maps color intensity from the sRGB color space to a linear gamma curve.

temperatureAndTint(neutral=None, targetNeutral=None)
Adapts the reference white point for an image.

Attributes: neutral a tuple, targetNeutral a tuple.

toneCurve(point0=None, point1=None, point2=None, point3=None, point4=None)
Adjusts tone response of the R, G, and B channels of an image.

Attributes: point0 a tuple (x, y), point1 a tuple (x, y), point2 a tuple (x, y), point3 a tuple (x, y), point4 a tuple (x, y).

vibrance(amount=None)
Adjusts the saturation of an image while keeping pleasing skin tones.

Attributes: amount a float.

whitePointAdjust(color=None)
Adjusts the reference white point for an image and maps all colors in the source using the new reference.

Attributes: color RGBA tuple Color (r, g, b, a).

colorCrossPolynomial(redCoefficients=None, greenCoefficients=None, blueCoefficients=None)
Modifies the pixel values in an image by applying a set of polynomial cross-products.

Attributes: redCoefficients a tuple (x, y, w, h), greenCoefficients a tuple (x, y, w, h), blueCoefficients a tuple (x, y, w, h).

colorInvert()
Inverts the colors in an image.

colorMap(gradientImage=None)
Performs a nonlinear transformation of source color values using mapping values provided in a table.

Attributes: gradientImage an Image object.

colorMonochrome(color=None, intensity=None)
Remaps colors so they fall within shades of a single color.

Attributes: color RGBA tuple Color (r, g, b, a), intensity a float.

colorPosterize(levels=None)
Remaps red, green, and blue color components to the number of brightness values you specify for each color component.

Attributes: levels a float.

falseColor(color0=None, color1=None)
Maps luminance to a color ramp of two colors.

Attributes: color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a).

maskToAlpha()
Converts a grayscale image to a white image that is masked by alpha.

maximumComponent()
Returns a grayscale image from max(r,g,b).

minimumComponent()
Returns a grayscale image from min(r,g,b).

photoEffectChrome()
Applies a preconfigured set of effects that imitate vintage photography film with exaggerated color.

photoEffectFade()
Applies a preconfigured set of effects that imitate vintage photography film with diminished color.

photoEffectInstant()
Applies a preconfigured set of effects that imitate vintage photography film with distorted colors.

photoEffectMono()
Applies a preconfigured set of effects that imitate black-and-white photography film with low contrast.

photoEffectNoir()
Applies a preconfigured set of effects that imitate black-and-white photography film with exaggerated contrast.

photoEffectProcess()
Applies a preconfigured set of effects that imitate vintage photography film with emphasized cool colors.

photoEffectTonal()
Applies a preconfigured set of effects that imitate black-and-white photography film without significantly altering contrast.

photoEffectTransfer()
Applies a preconfigured set of effects that imitate vintage photography film with emphasized warm colors.

sepiaTone(intensity=None)
Maps the colors of an image to various shades of brown.

Attributes: intensity a float.

vignette(radius=None, intensity=None)
Reduces the brightness of an image at the periphery.

Attributes: radius a float, intensity a float.

vignetteEffect(center=None, intensity=None, radius=None)
Modifies the brightness of an image around the periphery of a specified region.

Attributes: center a tuple (x, y), intensity a float, radius a float.

additionCompositing(backgroundImage=None)
Adds color components to achieve a brightening effect.

Attributes: backgroundImage an Image object.

colorBlendMode(backgroundImage=None)
Uses the luminance values of the background with the hue and saturation values of the source image.

Attributes: backgroundImage an Image object.

colorBurnBlendMode(backgroundImage=None)
Darkens the background image samples to reflect the source image samples.

Attributes: backgroundImage an Image object.

colorDodgeBlendMode(backgroundImage=None)
Brightens the background image samples to reflect the source image samples.

Attributes: backgroundImage an Image object.

darkenBlendMode(backgroundImage=None)
Creates composite image samples by choosing the darker samples (from either the source image or the background).

Attributes: backgroundImage an Image object.

differenceBlendMode(backgroundImage=None)
Subtracts either the source image sample color from the background image sample color, or the reverse, depending on which sample has the greater brightness value.

Attributes: backgroundImage an Image object.

divideBlendMode(backgroundImage=None)
Divides the background image sample color from the source image sample color.

Attributes: backgroundImage an Image object.

exclusionBlendMode(backgroundImage=None)
Produces an effect similar to that produced by the differenceBlendMode filter but with lower contrast.

Attributes: backgroundImage an Image object.

hardLightBlendMode(backgroundImage=None)
Either multiplies or screens colors, depending on the source image sample color.

Attributes: backgroundImage an Image object.

hueBlendMode(backgroundImage=None)
Uses the luminance and saturation values of the background image with the hue of the input image.

Attributes: backgroundImage an Image object.

lightenBlendMode(backgroundImage=None)
Creates composite image samples by choosing the lighter samples (either from the source image or the background).

Attributes: backgroundImage an Image object.

linearBurnBlendMode(backgroundImage=None)
Darkens the background image samples to reflect the source image samples while also increasing contrast.

Attributes: backgroundImage an Image object.

linearDodgeBlendMode(backgroundImage=None)
Brightens the background image samples to reflect the source image samples while also increasing contrast.

Attributes: backgroundImage an Image object.

luminosityBlendMode(backgroundImage=None)
Uses the hue and saturation of the background image with the luminance of the input image.

Attributes: backgroundImage an Image object.

maximumCompositing(backgroundImage=None)
Computes the maximum value, by color component, of two input images and creates an output image using the maximum values.

Attributes: backgroundImage an Image object.

minimumCompositing(backgroundImage=None)
Computes the minimum value, by color component, of two input images and creates an output image using the minimum values.

Attributes: backgroundImage an Image object.

multiplyBlendMode(backgroundImage=None)
Multiplies the input image samples with the background image samples.

Attributes: backgroundImage an Image object.

multiplyCompositing(backgroundImage=None)
Multiplies the color component of two input images and creates an output image using the multiplied values.

Attributes: backgroundImage an Image object.

overlayBlendMode(backgroundImage=None)
Either multiplies or screens the input image samples with the background image samples, depending on the background color.

Attributes: backgroundImage an Image object.

pinLightBlendMode(backgroundImage=None)
Conditionally replaces background image samples with source image samples depending on the brightness of the source image samples.

Attributes: backgroundImage an Image object.

saturationBlendMode(backgroundImage=None)
Uses the luminance and hue values of the background image with the saturation of the input image.

Attributes: backgroundImage an Image object.

screenBlendMode(backgroundImage=None)
Multiplies the inverse of the input image samples with the inverse of the background image samples.

Attributes: backgroundImage an Image object.

softLightBlendMode(backgroundImage=None)
Either darkens or lightens colors, depending on the input image sample color.

Attributes: backgroundImage an Image object.

sourceAtopCompositing(backgroundImage=None)
Places the input image over the background image, then uses the luminance of the background image to determine what to show.

Attributes: backgroundImage an Image object.

sourceInCompositing(backgroundImage=None)
Uses the background image to define what to leave in the input image, effectively cropping the input image.

Attributes: backgroundImage an Image object.

sourceOutCompositing(backgroundImage=None)
Uses the background image to define what to take out of the input image.

Attributes: backgroundImage an Image object.

sourceOverCompositing(backgroundImage=None)
Places the input image over the input background image.

Attributes: backgroundImage an Image object.

subtractBlendMode(backgroundImage=None)
Subtracts the background image sample color from the source image sample color.

Attributes: backgroundImage an Image object.

bumpDistortion(center=None, radius=None, scale=None)
Creates a bump that originates at a specified point in the image.

Attributes: center a tuple (x, y), radius a float, scale a float.

bumpDistortionLinear(center=None, radius=None, angle=None, scale=None)
Creates a concave or convex distortion that originates from a line in the image.

Attributes: center a tuple (x, y), radius a float, angle a float in degrees, scale a float.

circleSplashDistortion(center=None, radius=None)
Distorts the pixels starting at the circumference of a circle and emanating outward.

Attributes: center a tuple (x, y), radius a float.

circularWrap(center=None, radius=None, angle=None)
Wraps an image around a transparent circle.

Attributes: center a tuple (x, y), radius a float, angle a float in degrees.

droste(insetPoint0=None, insetPoint1=None, strands=None, periodicity=None, rotation=None, zoom=None)
Recursively draws a portion of an image in imitation of an M. C. Escher drawing.

Attributes: insetPoint0 a tuple (x, y), insetPoint1 a tuple (x, y), strands a float, periodicity a float, rotation a float, zoom a float.

displacementDistortion(displacementImage=None, scale=None)
Applies the grayscale values of the second image to the first image.

Attributes: displacementImage an Image object, scale a float.

glassDistortion(texture=None, center=None, scale=None)
Distorts an image by applying a glass-like texture.

Attributes: texture an Image object, center a tuple (x, y), scale a float.

glassLozenge(point0=None, point1=None, radius=None, refraction=None)
Creates a lozenge-shaped lens and distorts the portion of the image over which the lens is placed.

Attributes: point0 a tuple (x, y), point1 a tuple (x, y), radius a float, refraction a float.

holeDistortion(center=None, radius=None)
Creates a circular area that pushes the image pixels outward, distorting those pixels closest to the circle the most.

Attributes: center a tuple (x, y), radius a float.

pinchDistortion(center=None, radius=None, scale=None)
Creates a rectangular area that pinches source pixels inward, distorting those pixels closest to the rectangle the most.

Attributes: center a tuple (x, y), radius a float, scale a float.

stretchCrop(size=None, cropAmount=None, centerStretchAmount=None)
Distorts an image by stretching and or cropping it to fit a target size.

Attributes: size, cropAmount a float, centerStretchAmount a float.

torusLensDistortion(center=None, radius=None, width=None, refraction=None)
Creates a torus-shaped lens and distorts the portion of the image over which the lens is placed.

Attributes: center a tuple (x, y), radius a float, width a float, refraction a float.

twirlDistortion(center=None, radius=None, angle=None)
Rotates pixels around a point to give a twirling effect.

Attributes: center a tuple (x, y), radius a float, angle a float in degrees.

vortexDistortion(center=None, radius=None, angle=None)
Rotates pixels around a point to simulate a vortex.

Attributes: center a tuple (x, y), radius a float, angle a float in degrees.

aztecCodeGenerator(size=None, message=None, correctionLevel=None, layers=None, compactStyle=None)
Generates an Aztec code (two-dimensional barcode) from input data.

Attributes: message as bytes, correctionLevel a float, layers a float, compactStyle a bool.

QRCodeGenerator(size=None, message=None, correctionLevel=None)
Generates a Quick Response code (two-dimensional barcode) from input data.

Attributes: message as bytes, correctionLevel a single letter string, options are: 'L' (7%), 'M' (15%), 'Q' (25%) or 'H' (30%).

code128BarcodeGenerator(size=None, message=None, quietSpace=None)
Generates a Code 128 one-dimensional barcode from input data.

Attributes: message a bytes, quietSpace a float.

checkerboardGenerator(size, center=None, color0=None, color1=None, width=None, sharpness=None)
Generates a checkerboard pattern.

Attributes: center a tuple (x, y), color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a), width a float, sharpness a float.

constantColorGenerator(size, color=None)
Generates a solid color.

Attributes: color RGBA tuple Color (r, g, b, a).

lenticularHaloGenerator(size=None, center=None, color=None, haloRadius=None, haloWidth=None, haloOverlap=None, striationStrength=None, striationContrast=None, time=None)
Simulates a lens flare.

Attributes: center a tuple (x, y), color RGBA tuple Color (r, g, b, a), haloRadius a float, haloWidth a float, haloOverlap a float, striationStrength a float, striationContrast a float, time a float.

PDF417BarcodeGenerator(size=None, message=None, minWidth=None, maxWidth=None, minHeight=None, maxHeight=None, dataColumns=None, rows=None, preferredAspectRatio=None, compactionMode=None, compactStyle=None, correctionLevel=None, alwaysSpecifyCompaction=None)
Generates a PDF417 code (two-dimensional barcode) from input data.

Attributes: message a string, minWidth a float, maxWidth a float, minHeight a float, maxHeight a float, dataColumns a float, rows a float, preferredAspectRatio a float, compactionMode a float, compactStyle a bool, correctionLevel a float, alwaysSpecifyCompaction a bool.

randomGenerator(size)
Generates an image of infinite extent whose pixel values are made up of four independent, uniformly-distributed random numbers in the 0 to 1 range.

starShineGenerator(size, center=None, color=None, radius=None, crossScale=None, crossAngle=None, crossOpacity=None, crossWidth=None, epsilon=None)
Generates a starburst pattern that is similar to a supernova; can be used to simulate a lens flare.

Attributes: center a tuple (x, y), color RGBA tuple Color (r, g, b, a), radius a float, crossScale a float, crossAngle a float in degrees, crossOpacity a float, crossWidth a float, epsilon a float.

stripesGenerator(size, center=None, color0=None, color1=None, width=None, sharpness=None)
Generates a stripe pattern.

Attributes: center a tuple (x, y), color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a), width a float, sharpness a float.

sunbeamsGenerator(size=None, center=None, color=None, sunRadius=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, time=None)
Generates a sun effect.

Attributes: center a tuple (x, y), color RGBA tuple Color (r, g, b, a), sunRadius a float, maxStriationRadius a float, striationStrength a float, striationContrast a float, time a float.

crop(rectangle=None)
Applies a crop to an image.

Attributes: rectangle a tuple (x, y, w, h).

lanczosScaleTransform(scale=None, aspectRatio=None)
Produces a high-quality, scaled version of a source image.

Attributes: scale a float, aspectRatio a float.

perspectiveCorrection(topLeft=None, topRight=None, bottomRight=None, bottomLeft=None)
Applies a perspective correction, transforming an arbitrary quadrilateral region in the source image to a rectangular output image.

Attributes: topLeft a tuple (x, y), topRight a tuple (x, y), bottomRight a tuple (x, y), bottomLeft a tuple (x, y).

perspectiveTransform(topLeft=None, topRight=None, bottomRight=None, bottomLeft=None)
Alters the geometry of an image to simulate the observer changing viewing position.

Attributes: topLeft a tuple (x, y), topRight a tuple (x, y), bottomRight a tuple (x, y), bottomLeft a tuple (x, y).

straightenFilter(angle=None)
Rotates the source image by the specified angle in radians.

Attributes: angle a float in degrees.

gaussianGradient(size, center=None, color0=None, color1=None, radius=None)
Generates a gradient that varies from one color to another using a Gaussian distribution.

Attributes: center a tuple (x, y), color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a), radius a float.

linearGradient(size, point0=None, point1=None, color0=None, color1=None)
Generates a gradient that varies along a linear axis between two defined endpoints.

Attributes: point0 a tuple (x, y), point1 a tuple (x, y), color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a).

radialGradient(size, center=None, radius0=None, radius1=None, color0=None, color1=None)
Generates a gradient that varies radially between two circles having the same center.

Attributes: center a tuple (x, y), radius0 a float, radius1 a float, color0 RGBA tuple Color (r, g, b, a), color1 RGBA tuple Color (r, g, b, a).

circularScreen(center=None, width=None, sharpness=None)
Simulates a circular-shaped halftone screen.

Attributes: center a tuple (x, y), width a float, sharpness a float.

CMYKHalftone(center=None, width=None, angle=None, sharpness=None, GCR=None, UCR=None)
Creates a color, halftoned rendition of the source image, using cyan, magenta, yellow, and black inks over a white page.

Attributes: center a tuple (x, y), width a float, angle a float in degrees, sharpness a float, GCR a float, UCR a float.

dotScreen(center=None, angle=None, width=None, sharpness=None)
Simulates the dot patterns of a halftone screen.

Attributes: center a tuple (x, y), angle a float in degrees, width a float, sharpness a float.

hatchedScreen(center=None, angle=None, width=None, sharpness=None)
Simulates the hatched pattern of a halftone screen.

Attributes: center a tuple (x, y), angle a float in degrees, width a float, sharpness a float.

lineScreen(center=None, angle=None, width=None, sharpness=None)
Simulates the line pattern of a halftone screen.

Attributes: center a tuple (x, y), angle a float in degrees, width a float, sharpness a float.

areaAverage(extent=None)
Returns a single-pixel image that contains the average color for the region of interest.

Attributes: extent a tuple (x, y, w, h).

areaHistogram(extent=None, count=None, scale=None)
Returns a 1D image (inputCount wide by one pixel high) that contains the component-wise histogram computed for the specified rectangular area.

Attributes: extent a tuple (x, y, w, h), count a float, scale a float.

rowAverage(extent=None)
Returns a 1-pixel high image that contains the average color for each scan row.

Attributes: extent a tuple (x, y, w, h).

columnAverage(extent=None)
Returns a 1-pixel high image that contains the average color for each scan column.

Attributes: extent a tuple (x, y, w, h).

histogramDisplayFilter(height=None, highLimit=None, lowLimit=None)
Generates a histogram image from the output of the areaHistogram filter.

Attributes: height a float, highLimit a float, lowLimit a float.

areaMaximum(extent=None)
Returns a single-pixel image that contains the maximum color components for the region of interest.

Attributes: extent a tuple (x, y, w, h).

areaMinimum(extent=None)
Returns a single-pixel image that contains the minimum color components for the region of interest.

Attributes: extent a tuple (x, y, w, h).

areaMaximumAlpha(extent=None)
Returns a single-pixel image that contains the color vector with the maximum alpha value for the region of interest.

Attributes: extent a tuple (x, y, w, h).

areaMinimumAlpha(extent=None)
Returns a single-pixel image that contains the color vector with the minimum alpha value for the region of interest.

Attributes: extent a tuple (x, y, w, h).

sharpenLuminance(sharpness=None)
Increases image detail by sharpening.

Attributes: sharpness a float.

unsharpMask(radius=None, intensity=None)
Increases the contrast of the edges between pixels of different colors in an image.

Attributes: radius a float, intensity a float.

blendWithAlphaMask(backgroundImage=None, maskImage=None)
Uses alpha values from a mask to interpolate between an image and the background.

Attributes: backgroundImage an Image object, maskImage an Image object.

blendWithMask(backgroundImage=None, maskImage=None)
Uses values from a grayscale mask to interpolate between an image and the background.

Attributes: backgroundImage an Image object, maskImage an Image object.

bloom(radius=None, intensity=None)
Softens edges and applies a pleasant glow to an image.

Attributes: radius a float, intensity a float.

comicEffect()
Simulates a comic book drawing by outlining edges and applying a color halftone effect.

convolution3X3(weights=None, bias=None)
Modifies pixel values by performing a 3x3 matrix convolution.

Attributes: weights a float, bias a float.

convolution5X5(weights=None, bias=None)
Modifies pixel values by performing a 5x5 matrix convolution.

Attributes: weights a float, bias a float.

convolution7X7(weights=None, bias=None)
Modifies pixel values by performing a 7x7 matrix convolution.

Attributes: weights a float, bias a float.

convolution9Horizontal(weights=None, bias=None)
Modifies pixel values by performing a 9-element horizontal convolution.

Attributes: weights a float, bias a float.

convolution9Vertical(weights=None, bias=None)
Modifies pixel values by performing a 9-element vertical convolution.

Attributes: weights a float, bias a float.

crystallize(radius=None, center=None)
Creates polygon-shaped color blocks by aggregating source pixel-color values.

Attributes: radius a float, center a tuple (x, y).

depthOfField(point0=None, point1=None, saturation=None, unsharpMaskRadius=None, unsharpMaskIntensity=None, radius=None)
Simulates a depth of field effect.

Attributes: point0 a tuple (x, y), point1 a tuple (x, y), saturation a float, unsharpMaskRadius a float, unsharpMaskIntensity a float, radius a float.

edges(intensity=None)
Finds all edges in an image and displays them in color.

Attributes: intensity a float.

edgeWork(radius=None)
Produces a stylized black-and-white rendition of an image that looks similar to a woodblock cutout.

Attributes: radius a float.

gloom(radius=None, intensity=None)
Dulls the highlights of an image.

Attributes: radius a float, intensity a float.

heightFieldFromMask(radius=None)
Produces a continuous three-dimensional, loft-shaped height field from a grayscale mask.

Attributes: radius a float.

hexagonalPixellate(center=None, scale=None)
Maps an image to colored hexagons whose color is defined by the replaced pixels.

Attributes: center a tuple (x, y), scale a float.

highlightShadowAdjust(highlightAmount=None, shadowAmount=None)
Adjust the tonal mapping of an image while preserving spatial detail.

Attributes: highlightAmount a float, shadowAmount a float.

lineOverlay(noiseLevel=None, sharpness=None, edgeIntensity=None, threshold=None, contrast=None)
Creates a sketch that outlines the edges of an image in black.

Attributes: noiseLevel a float, sharpness a float, edgeIntensity a float, threshold a float, contrast a float.

pixellate(center=None, scale=None)
Makes an image blocky by mapping the image to colored squares whose color is defined by the replaced pixels.

Attributes: center a tuple (x, y), scale a float.

pointillize(radius=None, center=None)
Renders the source image in a pointillistic style.

Attributes: radius a float, center a tuple (x, y).

shadedMaterial(shadingImage=None, scale=None)
Produces a shaded image from a height field.

Attributes: shadingImage an Image object, scale a float.

spotColor(centerColor1=None, replacementColor1=None, closeness1=None, contrast1=None, centerColor2=None, replacementColor2=None, closeness2=None, contrast2=None, centerColor3=None, replacementColor3=None, closeness3=None, contrast3=None)
Replaces one or more color ranges with spot colors.

Attributes: centerColor1 RGBA tuple Color (r, g, b, a), replacementColor1 RGBA tuple Color (r, g, b, a), closeness1 a float, contrast1 a float, centerColor2 RGBA tuple Color (r, g, b, a), replacementColor2 RGBA tuple Color (r, g, b, a), closeness2 a float, contrast2 a float, centerColor3 RGBA tuple Color (r, g, b, a), replacementColor3 RGBA tuple Color (r, g, b, a), closeness3 a float, contrast3 a float.

spotLight(lightPosition=None, lightPointsAt=None, brightness=None, concentration=None, color=None)
Applies a directional spotlight effect to an image.

Attributes: lightPosition a tulple (x, y, z), lightPointsAt a tuple (x, y), brightness a float, concentration a float, color RGBA tuple Color (r, g, b, a).

affineClamp(transform=None)
Performs an affine transform on a source image and then clamps the pixels at the edge of the transformed image, extending them outwards.

Attributes: transform.

affineTile(transform=None)
Applies an affine transform to an image and then tiles the transformed image.

Attributes: transform.

eightfoldReflectedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by applying an 8-way reflected symmetry.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

fourfoldReflectedTile(center=None, angle=None, acuteAngle=None, width=None)
Produces a tiled image from a source image by applying a 4-way reflected symmetry.

Attributes: center a tuple (x, y), angle a float in degrees, acuteAngle a float in degrees, width a float.

fourfoldRotatedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by rotating the source image at increments of 90 degrees.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

fourfoldTranslatedTile(center=None, angle=None, acuteAngle=None, width=None)
Produces a tiled image from a source image by applying 4 translation operations.

Attributes: center a tuple (x, y), angle a float in degrees, acuteAngle a float in degrees, width a float.

glideReflectedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by translating and smearing the image.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

kaleidoscope(count=None, center=None, angle=None)
Produces a kaleidoscopic image from a source image by applying 12-way symmetry.

Attributes: count a float, center a tuple (x, y), angle a float in degrees.

opTile(center=None, scale=None, angle=None, width=None)
Segments an image, applying any specified scaling and rotation, and then assembles the image again to give an op art appearance.

Attributes: center a tuple (x, y), scale a float, angle a float in degrees, width a float.

parallelogramTile(center=None, angle=None, acuteAngle=None, width=None)
Warps an image by reflecting it in a parallelogram, and then tiles the result.

Attributes: center a tuple (x, y), angle a float in degrees, acuteAngle a float in degrees, width a float.

perspectiveTile(topLeft=None, topRight=None, bottomRight=None, bottomLeft=None)
Applies a perspective transform to an image and then tiles the result.

Attributes: topLeft a tuple (x, y), topRight a tuple (x, y), bottomRight a tuple (x, y), bottomLeft a tuple (x, y).

sixfoldReflectedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by applying a 6-way reflected symmetry.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

sixfoldRotatedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by rotating the source image at increments of 60 degrees.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

triangleTile(center=None, angle=None, width=None)
Maps a triangular portion of image to a triangular area and then tiles the result.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

twelvefoldReflectedTile(center=None, angle=None, width=None)
Produces a tiled image from a source image by rotating the source image at increments of 30 degrees.

Attributes: center a tuple (x, y), angle a float in degrees, width a float.

accordionFoldTransition(targetImage=None, bottomHeight=None, numberOfFolds=None, foldShadowAmount=None, time=None)
Transitions from one image to another of differing dimensions by unfolding and crossfading.

Attributes: targetImage an Image object, bottomHeight a float, numberOfFolds a float, foldShadowAmount a float, time a float.

barsSwipeTransition(targetImage=None, angle=None, width=None, barOffset=None, time=None)
Transitions from one image to another by passing a bar over the source image.

Attributes: targetImage an Image object, angle a float in degrees, width a float, barOffset a float, time a float.

copyMachineTransition(targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None)
Transitions from one image to another by simulating the effect of a copy machine.

Attributes: targetImage an Image object, extent a tuple (x, y, w, h), color RGBA tuple Color (r, g, b, a), time a float, angle a float in degrees, width a float, opacity a float.

disintegrateWithMaskTransition(targetImage=None, maskImage=None, time=None, shadowRadius=None, shadowDensity=None, shadowOffset=None)
Transitions from one image to another using the shape defined by a mask.

Attributes: targetImage an Image object, maskImage an Image object, time a float, shadowRadius a float, shadowDensity a float, shadowOffset a tuple (x, y).

dissolveTransition(targetImage=None, time=None)
Uses a dissolve to transition from one image to another.

Attributes: targetImage an Image object, time a float.

flashTransition(targetImage=None, center=None, extent=None, color=None, time=None, maxStriationRadius=None, striationStrength=None, striationContrast=None, fadeThreshold=None)
Transitions from one image to another by creating a flash.

Attributes: targetImage an Image object, center a tuple (x, y), extent a tuple (x, y, w, h), color RGBA tuple Color (r, g, b, a), time a float, maxStriationRadius a float, striationStrength a float, striationContrast a float, fadeThreshold a float.

modTransition(targetImage=None, center=None, time=None, angle=None, radius=None, compression=None)
Transitions from one image to another by revealing the target image through irregularly shaped holes.

Attributes: targetImage an Image object, center a tuple (x, y), time a float, angle a float in degrees, radius a float, compression a float.

pageCurlTransition(targetImage=None, backsideImage=None, shadingImage=None, extent=None, time=None, angle=None, radius=None)
Transitions from one image to another by simulating a curling page, revealing the new image as the page curls.

Attributes: targetImage an Image object, backsideImage an Image object, shadingImage an Image object, extent a tuple (x, y, w, h), time a float, angle a float in degrees, radius a float.

pageCurlWithShadowTransition(targetImage=None, backsideImage=None, extent=None, time=None, angle=None, radius=None, shadowSize=None, shadowAmount=None, shadowExtent=None)
Transitions from one image to another by simulating a curling page, revealing the new image as the page curls.

Attributes: targetImage an Image object, backsideImage an Image object, extent a tuple (x, y, w, h), time a float, angle a float in degrees, radius a float, shadowSize a float, shadowAmount a float, shadowExtent a tuple (x, y, w, h).

rippleTransition(targetImage=None, shadingImage=None, center=None, extent=None, time=None, width=None, scale=None)
Transitions from one image to another by creating a circular wave that expands from the center point, revealing the new image in the wake of the wave.

Attributes: targetImage an Image object, shadingImage an Image object, center a tuple (x, y), extent a tuple (x, y, w, h), time a float, width a float, scale a float.

swipeTransition(targetImage=None, extent=None, color=None, time=None, angle=None, width=None, opacity=None)
Transitions from one image to another by simulating a swiping action.

Attributes: targetImage an Image object, extent a tuple (x, y, w, h), color RGBA tuple Color (r, g, b, a), time a float, angle a float in degrees, width a float, opacity a float.

Variables
Variable(variables, workSpace, continuous=True)
Build small UI for variables in a script.

The workSpace is usually globals() as you want to insert the variable in the current workspace. It is required that workSpace is a dict object.

The continuous argument controls whether the script is run when UI elements change. The default is True, which will execute the script immediately and continuously when the user input changes. When set to False, there will be an "Update" button added at the bottom of the window. The user will have to click this button to execute the script and see the changes. This is useful when the script is slow, and continuous execution would decrease responsiveness.

../_images/variables.png
# create small ui element for variables in the script

Variable([
    # create a variable called 'w'
    # and the related ui is a Slider.
    dict(name="w", ui="Slider"),
    # create a variable called 'h'
    # and the related ui is a Slider.
    dict(name="h", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=100,
                minValue=50,
                maxValue=300)),
    # create a variable called 'useColor'
    # and the related ui is a CheckBox.
    dict(name="useColor", ui="CheckBox"),
    # create a variable called 'c'
    # and the related ui is a ColorWell.
    dict(name="c", ui="ColorWell")
    ], globals())

# draw a rect
rect(0, 0, w, h)

# check if the 'useColor' variable is checked
if useColor:
    # set the fill color from the variables
    fill(c)
# set the font size
fontSize(h)
# draw some text
text("Hello Variable", (w, h))

# Variable == vanilla power in DrawBot
from AppKit import NSColor
# create a color
_color = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, .5, 1, .8)
# setup variables using different vanilla ui elements.
Variable([
    dict(name="aList", ui="PopUpButton", args=dict(items=['a', 'b', 'c', 'd'])),
    dict(name="aText", ui="EditText", args=dict(text='hello world')),
    dict(name="aSlider", ui="Slider", args=dict(value=100, minValue=50, maxValue=300)),
    dict(name="aCheckBox", ui="CheckBox", args=dict(value=True)),
    dict(name="aColorWell", ui="ColorWell", args=dict(color=_color)),
    dict(name="aRadioGroup", ui="RadioGroup", args=dict(titles=['I', 'II', 'III'], isVertical=False)),
], globals())

print(aList)
print(aText)
print(aSlider)
print(aCheckBox)
print(aColorWell)
print(aRadioGroup)

# DrawBot reference

# set a size for the canvas
size(500, 500)

# using the functions width, height and pageCount
print("width:", width())
print("height:", height())

print("pageCount:", pageCount())

# simple shapes

# draw rect x, y, width, height
rect(10, 10, 100, 100)

# draw oval x, y, width, height
oval(10, 120, 100, 100)
oval(120, 120, 100, 100)

# draw polygon
polygon((10, 250), (100, 250), (100, 400), (50, 300), close=False)

# create path
db.newPath()
# move to point
db.moveTo((300, 100))
lineTo((400, 100))

# first control point (x1, y1)
# second control point (x2, y2)
# end point (x3, y3)
curveTo((450, 150), (450, 250), (400, 300))
lineTo((300, 300))
# close the path
closePath()
# draw the path
drawPath()

newPage()
# image: path, (x, y), alpha
image("https://github.com/typemytype/drawbot/raw/master/docs/content/assets/drawBot.jpg", (10, 10), .5)

newPage()
print("pageCount:", pageCount())
# colors
# fill(r, g, b)
# fill(r, g, b, alpha)
# fill(grayvalue)
# fill(grayvalue, alpha)
# fill(None)
fill(.5)
rect(10, 10, 100, 100)

fill(1, 0, 0)
rect(10, 120, 100, 100)

fill(0, 1, 0, .5)
oval(50, 50, 100, 100)

fill(None)

# stroke(r, g, b)
# stroke(r, g, b, alpha)
# stroke(grayvalue)
# stroke(grayvalue, alpha)
# stroke(None)
strokeWidth(8)
stroke(.8)
rect(200, 10, 100, 100)

stroke(.1, .1, .8)
rect(200, 120, 100, 100)

strokeWidth(20)
stroke(1, 0, 1, .5)
oval(250, 50, 100, 100)


newPage()
# stroke attributes

print("pageCount:", pageCount())
fill(None)
stroke(0)
strokeWidth(8)

lineCap("square")
lineJoin("miter")
miterLimit(5)
polygon((10, 10), (10, 400), (50, 350), close=False)

lineCap("round")
lineJoin("round")
polygon((110, 10), (110, 400), (150, 350), close=False)

lineCap("butt")
lineJoin("bevel")
polygon((210, 10), (210, 400), (250, 350), close=False)

lineDash(10, 10, 2, 5)
polygon((310, 10), (310, 400), (350, 350), close=False)

newPage()
print("pageCount:", pageCount())

text("Hello World", (10, 10))

fontSize(100)
fill(1, 0, 0)
stroke(0)
strokeWidth(5)
text("Hello World", (10, 20))

font("Times-Italic", 25)
fill(0, .5, 1)
stroke(None)
textBox("Hello World " * 100, (10, 150, 300, 300))


print("textSize:", textSize("Hallo"))

newPage()
# canvas transformations
print("pageCount:", pageCount())

fill(None)
stroke(0)
strokeWidth(3)
save()
rect(10, 10, 100, 100)


scale(2)
rect(10, 10, 100, 100)
restore()

save()
rotate(30)
rect(10, 10, 100, 100)
restore()

save()
skew(30)
rect(10, 10, 100, 100)
restore()

newPage()
print("pageCount:", pageCount())

#    c m y k alpha
cmykFill(0, 1, 0, 0)
rect(10, 10, 100, 100)

strokeWidth(5)
cmykFill(None)
cmykStroke(0, 1, 1, 0)
rect(10, 110, 100, 100)

cmykLinearGradient((10, 210), (10, 310), ([1, 1, 1, 1], [0, 1, 1, 0]))
rect(10, 210, 100, 100)

cmykStroke(None)

cmykRadialGradient((50, 410), (50, 410), ([1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 1, 0]), startRadius=0, endRadius=300)
rect(10, 310, 100, 150)

cmykShadow((10, 10), 20, (0, 1, 1, 0))
oval(130, 310, 300, 150)

newPage()
print("pageCount:", pageCount())

fill(1, 0, 1)
linearGradient((10, 10), (200, 20), ([1, 1, 0], [0, 1, 1]))

rect(10, 10, 200, 200)

radialGradient((50, 410), (50, 410), ([1, 0, 1], [1, 1, 0], [0, 1, 1]), startRadius=0, endRadius=300)
rect(10, 310, 100, 150)

shadow((10, 10), 20, (1, 0, 0))
oval(130, 310, 300, 150)

newPage()

save()

path = BezierPath()
path.oval(20, 20, 300, 100)
clipPath(path)

fill(1, 0, 0, .3)
rect(10, 10, 100, 100)

fontSize(30)
text("Hello World", (50, 80))

restore()

oval(200, 20, 50, 50)

saveImage(u"~/Desktop/drawBotTest.pdf")
saveImage(u"~/Desktop/drawBotTest.png")
saveImage(u"~/Desktop/drawBotTest.svg")
saveImage(u"~/Desktop/drawBotTest.mp4")

print("Done")
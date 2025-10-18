from drawBot import newPage, fill, rect, stroke, strokeWidth, line, lineDash, saveImage, font, fontSize, text, width, height, newPath, moveTo, curveTo, drawPath, textSize

# Define the canvas size
newPage(768, 768)

# Set a black background
fill(0)
rect(0, 0, width(), height())

# Function to draw bezier curves
def drawCurve(startPoint, controlPoint1, controlPoint2, endPoint, color, thickness):
    stroke(color)
    strokeWidth(thickness)
    newPath()
    moveTo(startPoint)
    curveTo(controlPoint1, controlPoint2, endPoint)
    drawPath()

# Define the colors of the curves
pink = (1, 0.5, 0.6)
orange = (1, 0.6, 0.2)

# Draw bezier curves
drawCurve((100, 700), (300, 100), (500, 600), (700, 100), pink, 4)
drawCurve((100, 600), (300, 200), (500, 700), (700, 200), orange, 4)

# Function to draw dashed lines
def drawDashedLine(startPoint, endPoint, dashPattern):
    stroke(1)
    strokeWidth(1)
    lineDash(dashPattern)
    line(startPoint, endPoint)

# Draw dashed lines
drawDashedLine((100, 700), (700, 100), [10, 4])
drawDashedLine((100, 600), (700, 200), [10, 4])

# Function to draw text labels
def drawLabel(labelText, position, labelFontSize, color):
    fill(color)
    stroke(None)
    font("Helvetica")
    fontSize(labelFontSize)
    text(labelText, position)

# Draw text labels
drawLabel("RESEARCH", (80, 710), 14, (1, 1, 1))
drawLabel("DISCOVERY", (720, 90), 14, (1, 1, 1))

# Draw the title
# Center the title vertically and horizontally, and adjust as needed
title = "Data lands"
titleFontSize = 48
font("Helvetica-Bold")  # Assuming title uses a bold weight
fontSize(titleFontSize)
titleWidth, titleHeight = textSize(title)
drawLabel(title, ((width() - titleWidth) / 2, (height() - titleHeight) / 2), titleFontSize, (1, 1, 1))

# Save the image
saveImage("~/Desktop/AbstractCurves.png")

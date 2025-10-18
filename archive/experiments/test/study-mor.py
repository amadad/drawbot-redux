from drawBot import newPage, fill, rect, oval, saveImage, newPath, moveTo, lineTo, closePath, drawPath, width, height
import random

# Set up the canvas
newPage(612, 792)  # Standard letter size

# Function to generate a random color
def randomColor():
    # Returns individual r, g, b values
    return random.random(), random.random(), random.random()

# Function to draw an abstract shape
def drawAbstractShape(x, y, size):
    # Determine the type of shape
    shapeType = random.choice(['oval', 'rect', 'polygon'])
    
    # Set a random fill color - Unpack the tuple directly in the call
    r, g, b = randomColor()
    fill(r, g, b)
    
    # Draw the shape
    if shapeType == 'oval':
        oval(x - size/2, y - size/2, size, size)
    elif shapeType == 'rect':
        rect(x - size/2, y - size/2, size, size)
    elif shapeType == 'polygon':
        newPath()
        moveTo((x, y + size/2))
        for _ in range(5):  # Create a pentagon for example
            dx = random.choice([-size/2, size/2])
            dy = random.choice([-size/2, size/2])
            lineTo((x + dx, y + dy))
        closePath()
        drawPath()

# Generate a series of abstract shapes
numShapes = 30
for _ in range(numShapes):
    # Generate random position and size
    xPos = random.randint(0, width())
    yPos = random.randint(0, height())
    size = random.randint(50, 150)  # Random size between 50 and 150
    
    drawAbstractShape(xPos, yPos, size)

# Save the image
saveImage("~/Desktop/AbstractShapes.pdf")

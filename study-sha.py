from drawBot import (size, width, height, newPath, moveTo, curveTo, lineTo, closePath, drawPath,
                     translate, savedState, fill, rect, stroke, strokeWidth, line, saveImage, random)
import random

# Set up the letter paper size
size(612, 792)  # 8.5 x 11 inches in points

# Define margins and grid
margin = width() * 0.1
num_columns = 3
num_rows = 4
column_width = (width() - 2 * margin) / num_columns
row_height = (height() - 2 * margin) / num_rows

def draw_unique_shape(x, y, w, h, shape_type):
    # This function will generate unique shapes based on the type: organic or geometric
    with savedState():
        translate(x, y)
        newPath()
        if shape_type == "organic":
            # Organic shapes with random curves
            moveTo((0, random.uniform(0, h/2)))
            for i in range(1, random.randint(2, 5)):
                curveTo((w * random.uniform(0, 1), h * random.uniform(0, 1)),
                        (w * random.uniform(0, 1), h * random.uniform(0, 1)),
                        (w * random.uniform(0, 1), h * random.uniform(0, 1)))
        else:
            # Geometric shapes with random lines
            moveTo((0, 0))
            for _ in range(random.randint(3, 6)):
                lineTo((w * random.uniform(0, 1), h * random.uniform(0, 1)))
            closePath()
        drawPath()

# Create the grid and draw the shapes
for row in range(num_rows):
    for col in range(num_columns):
        x = margin + col * column_width
        y = margin + row * row_height
        shape_type = "organic" if (row + col) % 2 == 0 else "geometric"
        draw_unique_shape(x, y, column_width, row_height, shape_type)

# Save the document
saveImage("~/Desktop/Shapes-Test.pdf")
print("A layout study of shapes created with all text in black.")

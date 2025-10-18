from drawBot import size, image, width, height, imageSize, stroke, strokeWidth, line, saveImage

# Set the size of the canvas
size(2160, 2700)

# Path to the background image
image_path = 'files/gradient/RB_Gradient_Background_001.jpg'  # Replace with the actual path to your image

# Get the size of the image
img_width, img_height = imageSize(image_path)

# Draw the background image
# This example just places the image at (0, 0). Adjust as needed, possibly with scaling.
image(image_path, (0, 0))

# You can now add additional elements on top of your background
# For example, defining the grid layout with columns
num_columns = 12
column_width = 180

# Example of how you might visualize the column structure (optional visualization)
for i in range(num_columns + 1):
    x = i * column_width
    # Drawing a semi-transparent line for each column boundary
    stroke(1, 0, 0, 0.5)  # Red lines with 50% opacity
    strokeWidth(1)
    line((x, 0), (x, height()))

# Save the image
saveImage('~/Desktop/Image-Test.pdf')
print("Layout created and saved as PDF.")
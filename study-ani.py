from drawBot import newPage, size, width, height, fill, rect, oval, saveImage

# Define the number of frames in the animation
numFrames = 10

# Set the size of the canvas
size(500, 500)

# Loop through each frame to draw
for i in range(numFrames):
    # Start a new page for each frame
    newPage(500, 500)
    # Set the background color
    fill(1)
    rect(0, 0, width(), height())
    # Calculate the x position of the circle for this frame
    x = (width() / numFrames) * i
    # Set the color of the circle
    fill(0)
    # Draw the circle
    oval(x, height()/2 - 25, 50, 50)

# Save the animation
saveImage("~/Desktop/simpleAnimation.gif")

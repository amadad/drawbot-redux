# Import DrawBot module
import drawBot as db

# Set canvas size
canvas_size = 600

# Set the number of frames for the animation
frames = 30

# Set square size and initial position
square_size = 100

# Set the frame duration once, outside the loop
db.frameDuration(1/10)  # 10 frames per second

# Loop through each frame
for frame in range(frames):
    # Start a new page
    db.newPage(canvas_size, canvas_size)
    
    # Set background color
    db.fill(1)  # White background
    db.rect(0, 0, canvas_size, canvas_size)
    
    # Set square color
    db.fill(0, 0, 1)  # Blue square
    
    # Calculate square's new position
    x = (frame / frames) * (canvas_size - square_size)
    y = (frame / frames) * (canvas_size - square_size)
    
    # Draw the square
    db.rect(x, y, square_size, square_size)

# Save the animation as a GIF
db.saveImage("animated_square.gif")
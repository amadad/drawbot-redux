from drawBot import size, image, oval, width, height, font, text, BezierPath, clipPath, savedState, saveImage, imageSize, scale, translate
import random

# Set canvas size
size(2400, 1350)

# Load the background image
image("files/paper/45.jpg", (0, 0))

# Set the font settings for the headline
font("Milka Soft", 36)
text("basic layout with random assets", (width()/2, height()*0.9), align="center")

# Define the circle's dimensions and position
circle_diameter = min(width(), height()) * 0.75
circle_x = (width() - circle_diameter) / 2
circle_y = (height() - circle_diameter) / 2

# Load the image to be masked, and calculate its scale factor to fit in the circle
image_path = "files/gold/04.jpg"
img_w, img_h = imageSize(image_path)
scale_factor = circle_diameter / img_h  # Focusing on height for the scale

# Use savedState to apply transformations and clipping path for the circle image
with savedState():
    # Set the clipping path to the circle
    newPath = BezierPath()
    newPath.oval(circle_x, circle_y, circle_diameter, circle_diameter)
    clipPath(newPath)
    
    # Adjust for centering the image within the circle
    translated_x = circle_x + (circle_diameter - (img_w * scale_factor)) / 2
    translated_y = circle_y
    
    # Move and scale the image
    translate(translated_x, translated_y)
    scale(scale_factor)
    
    # Draw the image at the new position
    image(image_path, (0, 0))

# Define maximum image width for the random images based on 25% of canvas height
max_img_width = height() * 0.25

# List of image paths to be randomly placed
image_paths = ["files/marker/Spiral_Circle_013.png", "files/marker/Skull_013.png", "files/marker/Shape_042.png"]

for img_path in image_paths:
    # Get original image size
    original_width, original_height = imageSize(img_path)
    
    # Calculate scale factor to ensure image width does not exceed max_img_width
    scale_factor = min(max_img_width / original_width, 1)  # Prevent scaling up
    
    # Generate random position for each image
    pos_x = random.randint(0, int(width() - (original_width * scale_factor)))
    pos_y = random.randint(0, int(height() - (original_height * scale_factor)))
    
    # Use savedState to apply transformations
    with savedState():
        translate(pos_x, pos_y)
        scale(scale_factor)
        image(img_path, (0, 0))

# Save the document
saveImage("~/Desktop/tweet.png")
print("Tweet image created and saved.")


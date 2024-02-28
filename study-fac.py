from drawBot import newPage, fill, rect, font, text, saveImage, fontSize
import random

# Letter size dimensions in points (1 inch = 72 points)
letter_width, letter_height = 612, 792  # 8.5 x 11 inches

# Define the number of pages and columns
num_pages = 3
num_columns = 3

# Define a list of sample texts
texts = ["DrawBot Fun", "Creative Coding", "Random Art", "Python Graphics", "Design Magic"]

# Function to generate a random color
def randomColor():
    return (random.random(), random.random(), random.random(), 1)

# Function to draw random text
def drawRandomText():
    fontSize(random.randint(10, 30))  # Random font size
    text(random.choice(texts), (random.randint(0, letter_width), random.randint(0, letter_height)))

for page in range(num_pages):
    newPage(letter_width, letter_height)
    
    # Draw shapes and text in columns
    column_width = letter_width / num_columns
    padding = 10  # Padding around the shapes
    
    for i in range(num_columns):
        x = i * column_width
        
        # Draw a rectangle with a random fill color
        fill(*randomColor())
        rect(x + padding, letter_height/3, column_width - 2*padding, 100)
        
        # Set a random fill color for the text
        fill(*randomColor())
        font("Helvetica", 24)
        text(f"Column {i+1}", (x + padding, letter_height/2))
    
    # Draw random texts on the page
    for _ in range(10):  # Draw 10 random texts per page
        fill(*randomColor())  # Random color for each text
        drawRandomText()

# Save the document as a PDF
saveImage("~/Desktop/letter_size_document.pdf")

print("3-page document created and saved.")
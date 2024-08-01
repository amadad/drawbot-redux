import drawBot as db

# Create a new drawing
db.newDrawing()

# Set the canvas size
width, height = 400, 400
db.newPage(width, height)

# Set the background color
db.fill(0.9)
db.rect(0, 0, width, height)

# Draw a rectangle with a different fill color
db.fill(0.1, 0.5, 0.8)
db.rect(50, 50, 300, 200)

# Draw a circle
db.fill(1, 0.2, 0.2)
db.oval(100, 150, 100, 100)

# Draw some text
db.fill(0)
db.fontSize(24)
db.text("Hello, DrawBot!", (100, 300))

# Save the drawing as a PDF
db.saveImage("output_test_drawbot.pdf")

# End the drawing
db.endDrawing()

print("Drawing completed and saved as output_test_drawbot.pdf")
import drawBot as db

db.newPage('A4')  # Create a new A4 page
db.fill(1)  # White background
db.rect(0, 0, db.width(), db.height())  # Draw the background
db.fill(0)  # Set fill color to black for the text

# Define the text to be drawn
left_text = 'typographische'
right_text = 'monatsblätter'

# Define the initial x positions for the left and right columns
left_x = 50  # Starting x position for the left column
right_x = db.width() / 2 + 50  # Starting x position for the right column, adjusted to the right of the center
y = db.height() - 50  # Starting y position from the top
sizes = [72, 60, 48, 36, 24, 12]  # Font sizes from large to small

for size in sizes:
    db.fontSize(size)
    # Draw the left text, aligning it to the left
    db.text(left_text, (left_x, y - db.fontAscender()))
    # Draw the right text, aligning it to the left
    db.text(right_text, (right_x, y - db.fontAscender()))
    # Adjust y position for the next size; the larger the size, the more it decreases
    y -= (db.fontAscender() + db.fontDescender() + 20)  # Adjust the 20 as needed for spacing

# Save the document
db.saveImage("~/Desktop/Ruder-Test.pdf")
print("A layout study document created with all text in black.")

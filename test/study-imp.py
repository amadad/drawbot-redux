from drawBot import newPage, size, width, height, font, fontSize, text, textBox, saveImage, fill, rect

# Set the size of the canvas
size(2160, 2700)

# Define the number of columns and the width for each
num_columns = 12
column_width = 180

# Set the page background color
fill(0.858, 1, 0)  # RGB equivalent of #DBFF00
rect(0, 0, width(), height())

# Placeholder text for the headline
headline_font = "TASA Explorer Bold"
headline_font_size = 180
headline_x = column_width
headline_y = height() - 9 * column_width
headline_text = f"Font: {headline_font}, Size: {headline_font_size}, X: {headline_x}, Y: {headline_y}"

# Placeholder text for the body
body_font = "Libre Caslon Condensed"
body_font_size = 36
body_x = column_width
body_y = height() - 15 * column_width
body_text = f"Font: {body_font}, Size: {body_font_size}, X: {body_x}, Y: {body_y}"

# Placeholder text for the number
number_font = "Milka Soft"
number_font_size = 180
number_x = width() - 3 * column_width
number_y = height() - 10 * column_width
number_text = f"Font: {number_font}, Size: {number_font_size}, X: {number_x}, Y: {number_y}"

# Draw the headline placeholder text
fill(0)  # Black color for text
font(headline_font, headline_font_size)
textBox(headline_text, (headline_x, headline_y, width() - 2 * column_width, 4 * column_width))

# Draw the body placeholder text
font(body_font, body_font_size)
textBox(body_text, (body_x, body_y, width() - 2 * column_width, 4 * column_width))

# Draw the number placeholder text
font(number_font, number_font_size)
text(number_text, (number_x, number_y))

# Save the image
saveImage('~/Desktop/YourDesign.pdf')
print("Layout created and saved as PDF.")

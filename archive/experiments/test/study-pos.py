import drawBot
import random

# Document settings
num_pages = 100
canvas_width = 612
canvas_height = 792
margin = 50
column_width = canvas_width / 12  # Define column width based on canvas width

# Text content
headline_text = "Exploring Layout Dynamics with DrawBot"
subhead_text = "Experimenting with Automated Design Variations"
body_text = "In the realm of digital design, the automation of layout variations presents a unique opportunity to explore the impact of typographic and compositional changes on visual communication. This study utilizes DrawBot, a Python-based scripting environment, to systematically generate a series of design layouts. Each page of the document represents a unique experiment in placement, size, and orientation of text elements, while maintaining a consistent typographic scheme. Through the automation of these elements, the study aims to uncover patterns and preferences that might not be immediately apparent in manual design processes. The DrawBot script dynamically adjusts parameters such as text box dimensions and positions across 100 pages, offering a broad perspective on layout effectiveness and viewer engagement. This exploration not only highlights the versatility of DrawBot in design experimentation but also contributes valuable insights into the principles of effective layout and typography in digital media."

# Font settings
font_name = "Helvetica"
headline_font_size = 24
subhead_font_size = 18
body_font_size = 12

# Function to draw a rotated text box with black text
def drawRotatedTextBox(txt, box, fontSize, angle):
    drawBot.save()
    drawBot.fill(0)  # Set text color to black
    drawBot.translate(box[0], box[1])
    drawBot.rotate(angle)
    drawBot.font(font_name, fontSize)
    drawBot.textBox(txt, (0, 0, box[2], box[3]))
    drawBot.restore()

# Create pages
for i in range(num_pages):
    drawBot.newPage(canvas_width, canvas_height)
    drawBot.fill(1)  # White background
    drawBot.rect(0, 0, canvas_width, canvas_height)
    
    # Define dynamic variables based on column_width
    dynamic_x = random.randint(1, 10) * column_width
    dynamic_y = random.randint(1, 10) * column_width
    dynamic_width = random.randint(2, 5) * column_width  # Ensure width is a multiple of column_width
    
    # Ensure the text box sizes and positions are multiples of column_width
    headline_x = margin
    headline_y = canvas_height - 4 * column_width
    headline_width = dynamic_width
    
    subhead_x = margin
    subhead_y = headline_y - 2 * column_width
    subhead_width = dynamic_width
    
    body_x = margin
    body_y = subhead_y - 5 * column_width
    body_width = dynamic_width
    
    headline_angle = 0
    subhead_angle = 0
    body_angle = 0
    
    # Draw text boxes with black text
    drawRotatedTextBox(headline_text, (headline_x, headline_y, headline_width, 100), headline_font_size, headline_angle)
    drawRotatedTextBox(subhead_text, (subhead_x, subhead_y, subhead_width, 60), subhead_font_size, subhead_angle)
    drawRotatedTextBox(body_text, (body_x, body_y, body_width, canvas_height - body_y - margin), body_font_size, body_angle)

# Save the document
drawBot.saveImage("~/Desktop/LayoutStudy_Variations.pdf")

print("100-page layout study document created with all text in black.")

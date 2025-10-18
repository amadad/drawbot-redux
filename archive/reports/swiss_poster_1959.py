# Recreation of 1959 Swiss Design Poster
# Aeschbacher, Bill, Müller, Linck Exhibition Poster
import drawBot as db

# Canvas setup - A3 at 300 DPI
width = 2100
height = 2970
db.newPage(width, height)

# Color palette
red_orange = (255/255, 60/255, 30/255)  # Vibrant red-orange background
black = (0, 0, 0)  # Pure black for text

# Fill background
db.fill(*red_orange)
db.rect(0, 0, width, height)

# Typography settings
db.fill(*black)
db.font("Helvetica-Bold")  # Swiss grotesque typeface

# Layout variables
margin = width * 0.05  # 5% margins for tighter layout
left_margin = margin
right_margin = width - margin
top_margin = height - margin
bottom_margin = margin

# Artist names - Large text
name_size = 450  # Larger text size
db.fontSize(name_size)

# Position calculations
baseline_start = top_margin - 250

# "Aesch-" - positioned at left
db.text("Aesch-", (left_margin, baseline_start))

# "bacher" - on second line, slightly indented
db.text("bacher", (left_margin + 160, baseline_start - name_size * 0.85))

# "Bill" - positioned from right edge
bill_width = db.textSize("Bill")[0]
db.text("Bill", (right_margin - bill_width, baseline_start - name_size * 1.7))

# "Müller" - staggered left position
db.text("Müller", (left_margin, baseline_start - name_size * 2.55))

# "Linck" - indented from left
db.text("Linck", (left_margin + 100, baseline_start - name_size * 3.4))

# Exhibition details - smaller text at bottom
detail_size = 60  # Smaller size for exhibition details
db.fontSize(detail_size)
leading = detail_size * 1.2

# Starting position for bottom text
detail_y = bottom_margin + 400

# "4" with extra spacing
db.text("4", (left_margin + 100, detail_y))

# "Bildhauer"
db.text("Bildhauer", (left_margin + 200, detail_y))

# "Kunsthalle" - new line
db.text("Kunsthalle", (left_margin + 200, detail_y - leading))

# "Basel 12.März" - new line
db.text("Basel 12.März", (left_margin + 200, detail_y - leading * 2))

# "bis 19.April" - new line
db.text("bis 19.April", (left_margin + 200, detail_y - leading * 3))

# "1959" - new line
db.text("1959", (left_margin + 200, detail_y - leading * 4))

# Save the output
db.saveImage("output/swiss_poster_1959.png")
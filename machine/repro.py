import drawBot as db

# Set up the canvas with more accurate proportions
db.size(595, 842)  # A4 size

# Background
db.fill(1)
db.rect(0, 0, db.width(), db.height())

# Text setup
leftText = "typographische"
rightText = "monatsblätter"
combinedText = "typographischemonatsblätter"

# Font settings - using Helvetica with tighter tracking
db.font("Helvetica")
db.fill(0)

# Starting positions
leftX = 80
rightX = db.width() - 300
startY = db.height() - 60

# Create more size variations for denser composition
sizes = [48, 42, 36, 32, 28, 24, 20, 18, 16, 14, 12, 10, 9, 8]
lineSpacing = 0.85  # Tighter line spacing

# Left column
y = startY
for size in sizes:
    db.fontSize(size)
    db.text(leftText.lower(), (leftX, y))
    y -= size * lineSpacing
    # Add extra repetitions for smaller sizes
    if size < 20:
        db.text(leftText.lower(), (leftX, y))
        y -= size * lineSpacing

# Right column
y = startY
for size in sizes:
    db.fontSize(size)
    db.text(rightText.lower(), (rightX, y))
    y -= size * lineSpacing
    # Add extra repetitions for smaller sizes
    if size < 20:
        db.text(rightText.lower(), (rightX, y))
        y -= size * lineSpacing

# Large text at bottom
db.fontSize(52)
db.text(combinedText.lower(), (leftX, 100))
db.text(combinedText.lower(), (leftX, 160))

db.saveImage("typographic_poster.pdf")

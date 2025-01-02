import drawBot as db
def createCover():
    # Create new page
    db.newPage(1000, 1000)

    # Set white background
    db.fill(1, 1, 1)
    db.rect(0, 0, db.width(), db.height())

    # Set text properties
    db.fill(0)
    db.font("Helvetica")

    # Technical info in top right
    db.fontSize(8)
    db.text("TM RSI SGM 6/1974", (db.width() - 150, db.height() - 20))

    # Word to repeat
    word = "typographischemonatsblätter"

    # Left column - getting larger
    startSize = 12
    x = 100
    y = db.height() - 100

    for i in range(8):
        size = startSize + (i * 8)
        db.fontSize(size)
        db.text(word, (x, y - (i * 80)))

    # Right column - getting smaller
    startSize = 60
    x = db.width() - 400
    y = 150

    for i in range(8):
        size = startSize - (i * 6)
        db.fontSize(size)
        db.text(word, (x, y + (i * 80)))


createCover()

db.saveImage(r"/Users/amadad/Projects/drawbot-redux/machine/machine/output/output_v1.png")
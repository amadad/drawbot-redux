from pagebot.document import Document
from pagebot.elements import newRect
from pagebot.conditions import Center2Center, Middle2Middle
from pagebot.toolbox.units import pt
from pagebot.toolbox.color import color

W, H = pt(500, 400)
doc = Document(w=W, h=H, autoPages=1)
page = doc[1]

# Create a new rectangle element with position conditions
newRect(parent=page, fill=color('red'), size=pt(240, 140),
    # Show measure lines on the element.
    showDimensions=True, 
    conditions=[Center2Center(), Middle2Middle()])
# Make the page apply all conditions.
page.solve() 
# Export the document page as png, so it shows as web image.
doc.export('_export/RedSquare.png') 
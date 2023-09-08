
# listing of all function in a class
# from pagebot.elements import Element
# help(Element)

from pagebot.document import Document
from pagebot.style import A4Letter, INCH, CENTER, MIDDLE
from pagebot.elements import *
from pagebot.conditions import *

W, H = A4Letter

def makeDocument():

    doc = Document(w=W, h=H, originTop=False)
    view = doc.getView()
    view.padding = INCH/2
    view.showPageNameInfo = True
    view.showPageCropMarks = True
    view.showPageFrame = True
    view.showPagePadding = True
    view.showPageRegistrationMarks = True
    view.showGrid= True
    view.showGridColumns = True
    view.showElementOrigin = True
    view.showElementInfo = True

    page = doc[0]
    page.padding = INCH
    
    rr = newRect(parent=page, x=100, y=100, w=50, h=50, fill=(1,0,0))
    
    print page.elements
    
    conditions = [Left2Left(), Top2TopSide(), Fit2Width()]
    conditions = [Left2Left(), Top2Top()]
    
    pr = newRect(parent=page, conditions=conditions, w=page.pw*2/3, h= 200, fill=(1,0,1))
    doc.solve()

    rr.left = pr.right
    rr.top = pr.bottom

    return doc

d = makeDocument()
d.export('_export/DemoDocument.pdf')
from pagebot import newFS
from pagebot.document import Document
from pagebot.style import Letter, INCH, CENTER, MIDDLE
from pagebot.elements import *
from pagebot.conditions import *

W, H = Letter
RectSize = 300

def makeDocument():
    
    doc = Document(w=W, h=H, originTop=False)
    view = doc.getView()
    view.padding = INCH/2
    view.showPageNameInfo = True
    view.showPageCropMarks = True
    view.showPagePadding = True
    view.showPageFrame = True
    view.showPageRegistrationMarks = True
    view.showGrid = False
    view.showGridColumns = True
    view.showElementOrigin = False
    view.showElementInfo = False
        
    page = doc[0]
    page.padding = INCH
    
    cc = [Left2Left(), Float2Top()]
    conditions = [Left2Left(), Top2TopSide(), Float2Top(), Middle2Middle()]
    #conditions = [Left2Left(), Float2Top()]

    fs = newFS('Headline', style=dict(font='Verdana', fontSize=30, textFill=0, rLeading=1.2))
    
    # newTextBox(fs, fill=0.8, parent=page, 
    #     w=RectSize, h=RectSize, shadow=shadow, textShadow=textShadow,
    #     conditions=conditions, xAlign=CENTER, yAlign=MIDDLE)
    

    rr = newRect(parent=page, h=100, w=300, conditions=cc, fill=(1, 0, .5))
    pr = newRect(parent=page, conditions=conditions, w=page.pw*1/3, fill=(1, .5, 0))

    
    doc.solve()
    
    #rr.left = pr.right
    #rr.top = pr.bottom
    
    return doc

d = makeDocument()
d.export('_export/DemoDocument.pdf')
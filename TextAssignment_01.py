

from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.style import Letter, INCH, CENTER, MIDDLE



W, H = Letter

doc = Document (w=W, h=H, originTop=False, autoPage=1)

view = doc.getView()
view.showPagePadding = True

page = doc[0]
page.padding = page.h/12, page.w/12 # document height and width / 12

newTextBox('The Best for the Most for the Least', parent=page, x=20, y=220, fill=0, fontSize=50, font='NovaCut',
    conditions=[Fit2Width(), Left2Left(), Top2Top()]) # conditions won't work without calling solve
    
newRect(parent=page, h=page.ph/12, fill=(.1,.4,.3), conditions=[Float2Top(), Left2Left(), Fit2Width()])

newTextBox('Though best known for their furniture designs, Charles and Ray Eames made more than 125 films—striking attempts “to get across an idea.”', w=page.pw/2, parent=page, fill=0, fontSize=24, mr=-10, font='Akkurat-Bold',
    conditions=[Left2Left(), Float2Top(), Fit2Bottom()], nextElement='Column2')

newTextBox('Though best known for their furniture designs, Charles and Ray Eames made more than 125 films—striking attempts “to get across an idea.”', w=page.pw/3, parent=page, fill=0, fontSize=12, font='Akkurat-Bold',
    conditions=[Float2Right(), Float2Top(), Float2Left()])

newRect(parent=page, w=page.pw*.33, fill=(.3,.4,.2), conditions=[Float2Right(), Float2Top(), Float2Left(), Float2Right()])
newRect(parent=page, w=page.pw*.5, h=page.ph*.5, conditions=[Float2Bottom(), Right2Right()], fill=(.25,1,1, 0.5))

doc.solve()
doc.export('_export/TextAssignment.pdf')
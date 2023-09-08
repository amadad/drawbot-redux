
# Demo Spreadsheet Element
     
from pagebot.document import Document
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.style import A5, TOP
from pagebot.contributions.filibuster.blurb import Blurb
from pagebot.toolbox.transformer import pointOffset

class DemoSpreadSheet(Element):
    
    def _drawSpreadSheet(self, p, view):
        print self.css('font
        fill(0, 1, 0)
        rect(p[0],p[1], 100, self.h/2)
        
    def draw(self, origin, view, drawElements=True):
        u"""Default drawing method just drawing the frame. 
        Probably will be redefined by inheriting element classes."""
        
        p = pointOffset(self.oPoint, origin)
        p = self._applyScale(p)    
        px, py, _ = p = self._applyAlignment(p) # Ignore z-axis for now.

        self.drawFrame(p, view) # Draw optional frame or borders.

        if self.drawBefore is not None: # Call if defined
            self.drawBefore(self, p, view)

        self.drawSpreadSheet(origin,view)
        if drawElements:
            # If there are child elements, draw them over the pixel image.
            self._drawElements(p, view)

        if self.drawAfter is not None: # Call if defined
            self.drawAfter(self, p, view)

        self._restoreScale()
        view.drawElementMetaInfo(self, origin) # Depends on css flag 'showElementInfo'

W, H = A5

doc = Document(w=W, h=H, originTop=False, autoPages=1)

view = doc.getView()
view.showPagePadding = True
view.showElementOrigin = True
view.showFlowConnections = True

page = doc[0]
page.padding = int(page.h/12), int(page.w/12)

DemoSpreadSheet(parent=page, width=200, height=200, fill=0.8, 
    conditions=[Left2Left(), Fit2Width(), Top2Top()]
)

#print he.x, he.y 
print page.solve()
#print he.x, he.y 

doc.export('_export/DemoSpreadSheetElement.pdf')
import os
import math

#------------------------------------------------------------
# 0. INTRO
#------------------------------------------------------------ 

# Pattern Generator
# This script is meant to be run in drawbot
# https://www.drawbot.com
#
# This tool was created to be used during 
# 'Designing Type Ornaments' workshop at Typographics 2021
# It is a collaborative work by DJR and Marina Chaccur
#
# Fot the 'text' the MyLeaves fonts should be installed. 

#------------------------------------------------------------
# 1. PATTERNS
#------------------------------------------------------------ 
# determine a base cell size
defaultCellSize = 100
# if nothing is in the UI, the pattern will be this
defaultPattern = """
b
"""
# Extra folder/ files

#------------------------------------------------------------
# 2. INTERFACE
#------------------------------------------------------------

typefaceList = [
    'myleaves curvy', 
    'myleaves myleapoint', 
    'myleaves curvepoint', 
    'myleaves bubble'
    ]


Variable([
    dict(name="basePattern", ui="PopUpButton", args=dict(items=['image', 'text'])),
    dict(name="pattern", ui="EditText", args=dict(text=defaultPattern.strip())),
    dict(name="cellSize", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=defaultCellSize,
                minValue=50,
                maxValue=500,
                tickMarkCount=10, 
                #stopOnTickMarks=True
                )),
    dict(name="Typeface", ui="PopUpButton", args=dict(items=typefaceList)),
    dict(name="totalXSymmetry", ui="CheckBox"),
    dict(name="totalYSymmetry", ui="CheckBox"),  
    dict(name="localXSymmetry", ui="CheckBox"),
    dict(name="localYSymmetry", ui="CheckBox"),
    dict(name="background", ui="ColorWell", args=dict(color=None)),
    dict(name="typeColor", ui="ColorWell"),
    dict(name="showGrid", ui="CheckBox"),
    dict(name="fileName", ui="EditText", args=dict(text="")),
    dict(name="saveFile", ui="CheckBox")
    ], globals())

#------------------------------------------------------------
# 3. ELEMENTS/ DRAW PATTERN
#------------------------------------------------------------

# Background
fill(background)
rect(0, 0, width(), height())
# Type color
fill(typeColor)

# if the pattern field is empty, avoid an error
if not pattern:
    pattern = defaultPattern

# round cell size to the nearest integer
if cellSize:
    cellSize = int(round(cellSize))
else:
    cellSize = 100


if basePattern == 1:
    useText = True
else:
    useText = False

theFontName = typefaceList[Typeface]
theFontSize = cellSize*2.5

# total and local symmetry toggles
# total symmetry flips the whole image

# local symmetry flips each pattern iteration

# draw cell outlines
# DEBUG = False

# collect images in a dictionary
images = {
    'p': 'images/p.png',
    'd': 'images/d.png',
    'b': 'images/b.png',
    'q': 'images/q.png',
    'a': 'images/a.png',
    'c': 'images/c.png',
    'e': 'images/e.png',
    'f': 'images/f.png'
    }
    
# define symmetry
xSymmetryMap = {'p': 'q', 'b': 'd', 'P': 'Q', 'B': 'D', 'A': 'H', 'a': 'h', 'U': 'V', 'u': 'v', 'a' : 'e', 'c' : 'f'}
ySymmetryMap = {'p': 'b', 'q': 'd', 'P': 'B', 'Q': 'D', 'M': 'W', 'm': 'w', 'a' : 'f', 'e' : 'c'}
# add inverse to symmetry
xSymmetryMap.update({v: k for k, v in xSymmetryMap.items()})
ySymmetryMap.update({v: k for k, v in ySymmetryMap.items()})


###
# functions 
###
def getSymmetry(line, symmetryMap):
    output = ''
    for char in line:
        if char in symmetryMap:
            output += symmetryMap[char]
        else:
            output += char
    return output

def parsePattern(pattern):
    """
    given a raw text pattern
    convert it to a list of lines
    """
    rawLines = pattern.strip().split('\n')
    lines = []
    for line in rawLines:
        if localXSymmetry:
            line += getSymmetry(line[::-1], xSymmetryMap)
        lines.append(line)
    if localYSymmetry:
        flipLines = lines.copy()
        flipLines.reverse()
        for line in flipLines:
            lines.append(getSymmetry(line, ySymmetryMap))
    return lines

def drawPattern(lines):
    """
    draw a single iteration of a pattern
    """
    with savedState():
        for line in lines:
            with savedState():
                for char in line:
                    if useText:
                        font(theFontName, theFontSize)
                        text(char, (0, 0))
                    else:
                        imageWidth, imageHeight = imageSize(images[char])
                        with savedState():
                            scale(cellSize/imageWidth)
                            image(images[char], (0, 0))
                    if showGrid:
                        with savedState():
                            stroke(1, 0, 1)
                            strokeWidth(1)
                            fill(None)
                            rect(0, 0, patternWidth, patternHeight)
                    translate(cellSize, 0)
            translate(0, cellSize)
    if showGrid:
        with savedState():
            stroke(0, 0, 1)
            strokeWidth(2)
            fill(None)
            rect(0, 0, patternWidth, patternHeight)

if __name__ == '__main__':

    lines = parsePattern(pattern)

    # get the dimensions of the pattern
    patternHeight = len(lines)*cellSize
    patternWidth = len(lines[0]*cellSize)

    repeatsY = math.ceil( height() / patternHeight )
    if totalYSymmetry:
        repeatsY = math.ceil( height()/2 / patternHeight )
    repeatsX = math.ceil( width() /  patternWidth )
    if totalXSymmetry:
        repeatsX = math.ceil( width()/2 /  patternWidth )

    iterations = [0]
    # if there is total symmetry, iterate for each half or quadrant
    if totalYSymmetry and totalXSymmetry:
        iterations = [0, 1, 2, 3]
    elif totalYSymmetry:
        iterations = [0, 1]
    elif totalXSymmetry:
        iterations = [0, 2]
        
for i in iterations:
        with savedState():
            # do the necessary flipping for each half or quadrant
            if i == 1:
                translate(0, patternHeight*repeatsY*2)
                scale(1, -1)
            elif i == 2:
                translate(patternWidth*repeatsX*2, 0)
                scale(-1, 1)
            elif i == 3:
                translate(patternWidth*repeatsX*2, patternHeight*repeatsY*2)
                scale(-1, -1)
                
            # repeat the pattern a number of times
            for repeatY in range(repeatsY):
                with savedState():
                    for repeatX in range(repeatsX):
                        drawPattern(lines)
                        translate(patternWidth)
                translate(0, patternHeight)

#------------------------------------------------------------
# 4. SAVE FILE
#------------------------------------------------------------
if saveFile:
    saveImage('%s.png' % (fileName))
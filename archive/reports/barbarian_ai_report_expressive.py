# Barbarian Monthly AI Intelligence Brief - Expressive Visual Design
# "The Evolution of Intelligence" - From rigid machine thinking to fluid AI consciousness

import drawBot as db
import os
import math
import random

# Document setup
page_width = 595  # A4 width in points
page_height = 842  # A4 height in points
margin = 40
content_width = page_width - (2 * margin)
content_height = page_height - (2 * margin)

# Color evolution palette
colors = {
    "deep_blue": (10/255, 22/255, 40/255),
    "purple": (74/255, 20/255, 140/255),
    "magenta": (173/255, 20/255, 87/255),
    "orange": (255/255, 111/255, 0/255),
    "warm_yellow": (255/255, 179/255, 0/255),
    "white": (1, 1, 1),
    "black": (0, 0, 0)
}

# Font setup
try:
    db.font("TASA Explorer Black")
    headline_font = "TASA Explorer Black"
except:
    headline_font = "Helvetica-Bold"
    
try:
    db.font("Space Grotesk")
    body_font = "Space Grotesk"
except:
    body_font = "Helvetica"

# Read content
with open("/Users/amadad/Projects/drawbot-redux/barbarian-monthly-ai-intelligence-brief-july2025.md", "r") as f:
    content = f.read()

# Helper functions
def interpolate_color(color1, color2, factor):
    """Interpolate between two colors"""
    return tuple(c1 + (c2 - c1) * factor for c1, c2 in zip(color1, color2))

def draw_gradient_background(color1, color2, complexity=50):
    """Draw complex gradient background"""
    for i in range(complexity):
        factor = i / complexity
        color = interpolate_color(color1, color2, factor)
        db.fill(*color, 0.3)
        y = page_height * factor
        # Add organic variation
        offset = math.sin(factor * math.pi * 4) * 20
        db.rect(-10, y - 20 + offset, page_width + 20, 40)

def draw_neural_network(x, y, size, color, opacity=0.1):
    """Draw abstract neural network pattern"""
    db.fill(*color, opacity)
    nodes = 8
    for i in range(nodes):
        angle = (i / nodes) * math.pi * 2
        nx = x + math.cos(angle) * size
        ny = y + math.sin(angle) * size
        db.oval(nx - 5, ny - 5, 10, 10)
        # Connect to other nodes
        for j in range(i + 1, nodes):
            angle2 = (j / nodes) * math.pi * 2
            nx2 = x + math.cos(angle2) * size
            ny2 = y + math.sin(angle2) * size
            db.stroke(*color, opacity * 0.5)
            db.strokeWidth(0.5)
            path = db.BezierPath()
            path.moveTo((nx, ny))
            path.curveTo((nx + 20, ny + 20), (nx2 - 20, ny2 - 20), (nx2, ny2))
            db.drawPath(path)
            db.stroke(None)

def morph_shape(x, y, size, morph_factor):
    """Morph from square to circle"""
    path = db.BezierPath()
    corners = 4
    for i in range(corners):
        angle = (i / corners) * math.pi * 2 - math.pi / 4
        # Square corners
        sx = x + math.cos(angle) * size * 1.414
        sy = y + math.sin(angle) * size * 1.414
        # Circle points
        cx = x + math.cos(angle + math.pi/4) * size
        cy = y + math.sin(angle + math.pi/4) * size
        # Interpolate
        px = sx + (cx - sx) * morph_factor
        py = sy + (cy - sy) * morph_factor
        if i == 0:
            path.moveTo((px, py))
        else:
            # Add curve for smoother morphing
            ctrl_angle = ((i - 0.5) / corners) * math.pi * 2 - math.pi / 4
            ctrl_x = x + math.cos(ctrl_angle) * size * (1.414 - 0.414 * morph_factor)
            ctrl_y = y + math.sin(ctrl_angle) * size * (1.414 - 0.414 * morph_factor)
            path.curveTo((ctrl_x, ctrl_y), (ctrl_x, ctrl_y), (px, py))
    path.closePath()
    db.drawPath(path)

def draw_breathing_text(text, x, y, base_spacing=0, breath_factor=1):
    """Draw text with variable letter spacing"""
    fs = db.FormattedString()
    for i, char in enumerate(text):
        # Calculate breathing effect
        spacing = base_spacing + math.sin(i * 0.5) * breath_factor
        fs.append(char, font=headline_font, fontSize=48, tracking=spacing)
    db.text(fs, (x, y))

# Page 1: Cover - "Awakening"
db.newPage(page_width, page_height)
draw_gradient_background(colors["deep_blue"], colors["purple"])

# Neural network patterns
for i in range(5):
    x = random.randint(100, page_width - 100)
    y = random.randint(100, page_height - 100)
    size = random.randint(50, 150)
    draw_neural_network(x, y, size, colors["purple"], 0.05)

# Morphing shapes
for i in range(3):
    morph_factor = i / 3
    db.fill(*interpolate_color(colors["deep_blue"], colors["purple"], morph_factor), 0.3)
    morph_shape(page_width/2 - 100 + i * 100, page_height/2, 40, morph_factor)

# Fragmented title
db.fill(*colors["white"])
title_parts = ["Mon", "thly ", "AI", " Int", "elli", "gence"]
x_start = 80
y_pos = page_height - 200
for i, part in enumerate(title_parts):
    db.save()
    rotation = math.sin(i * 0.7) * 5
    db.translate(x_start + i * 70, y_pos)
    db.rotate(rotation)
    db.font(headline_font)
    db.fontSize(48)
    db.text(part, (0, 0))
    db.restore()

# Breathing subtitle
draw_breathing_text("Brief", margin + 50, page_height - 280, 2, 4)

# Subtitle
db.fill(*colors["purple"], 0.8)
db.font(body_font)
db.fontSize(24)
db.text("The Barbarian Group", (margin + 50, page_height - 340))
db.fontSize(18)
db.text("July 2025", (margin + 50, page_height - 380))

# Page 2: Executive Summary - "Pulse"
db.newPage(page_width, page_height)
draw_gradient_background(colors["purple"], colors["magenta"], 30)

# Pulse line
db.stroke(*colors["magenta"], 0.3)
db.strokeWidth(2)
pulse_path = db.BezierPath()
y_center = page_height - 120
for x in range(0, page_width, 5):
    y = y_center + math.sin(x * 0.02) * 20 * math.exp(-x / page_width)
    if x == 0:
        pulse_path.moveTo((x, y))
    else:
        pulse_path.lineTo((x, y))
db.drawPath(pulse_path)
db.stroke(None)

# Title along pulse
db.fill(*colors["white"])
db.font(headline_font)
db.fontSize(36)
db.text("Executive Summary", (margin, y_center))

# Highlights with variable weight
highlights = [
    ("Manus AI", "emerges as a game-changer with $2/task autonomous agents", 1.0),
    ("Midjourney", "launches video capabilities at $10/month", 0.8),
    ("Abacus.AI", "positions as enterprise 'AI Brain' with DeepAgent", 0.9),
    ("Major shift", "toward authentic, less polished content", 0.7)
]

y_pos = page_height - 250
for i, (key, value, importance) in enumerate(highlights):
    # Organic shape background
    db.fill(*colors["white"], 0.1)
    path = db.BezierPath()
    path.moveTo((margin, y_pos - i * 120))
    path.curveTo(
        (margin + 100, y_pos - i * 120 + 20),
        (margin + content_width - 100, y_pos - i * 120 + 10),
        (margin + content_width, y_pos - i * 120)
    )
    path.lineTo((margin + content_width, y_pos - i * 120 - 80))
    path.curveTo(
        (margin + content_width - 100, y_pos - i * 120 - 100),
        (margin + 100, y_pos - i * 120 - 90),
        (margin, y_pos - i * 120 - 80)
    )
    path.closePath()
    db.drawPath(path)
    
    # Variable weight text
    fs = db.FormattedString()
    fs.append(key + " ", font=headline_font, fontSize=16 + importance * 8, fill=colors["magenta"])
    fs.append(value, font=body_font, fontSize=12 + importance * 2, fill=colors["white"])
    
    # Breathing letter spacing
    spacing = math.sin(i * 0.5) * 2
    db.text(fs, (margin + 30, y_pos - i * 120 - 40))

# Page 3: AI Platforms - "Breaking Free"
db.newPage(page_width, page_height)
draw_gradient_background(colors["magenta"], colors["orange"], 40)

# Grid breaking free
db.stroke(*colors["white"], 0.1)
db.strokeWidth(1)
for i in range(0, page_width, 40):
    factor = i / page_width
    offset = math.sin(factor * math.pi) * 50
    path = db.BezierPath()
    path.moveTo((i, 0))
    path.lineTo((i + offset, page_height))
    db.drawPath(path)
db.stroke(None)

# Title with kinetic effect
db.fill(*colors["white"])
title = "AI Agent Platforms Update"
x_pos = margin
y_pos = page_height - 100
for i, char in enumerate(title):
    db.save()
    wave = math.sin(i * 0.3) * 10
    db.font(headline_font)
    db.fontSize(28)
    db.text(char, (x_pos + i * 20, y_pos + wave))
    db.restore()

# Platform information with diagonal momentum
platforms = [
    ("Manus AI", "$2/task", "90% cheaper"),
    ("Abacus.AI", "AI Brain", "Autonomous"),
    ("ChatGPT", "Evolution", "Beyond chat")
]

for i, (name, feature, impact) in enumerate(platforms):
    angle = -15 + i * 10
    x = margin + 50 + i * 150
    y = page_height - 300 - i * 80
    
    db.save()
    db.translate(x, y)
    db.rotate(angle)
    
    # Momentum line
    db.stroke(*colors["orange"], 0.5)
    db.strokeWidth(3)
    db.line((0, 0), (200, 0))
    db.stroke(None)
    
    # Platform info
    db.fill(*colors["white"])
    db.font(headline_font)
    db.fontSize(24)
    db.text(name, (0, 20))
    db.font(body_font)
    db.fontSize(16)
    db.text(feature, (0, -10))
    db.fontSize(12)
    db.fill(*colors["orange"])
    db.text(impact, (0, -30))
    
    db.restore()

# Page 4: Video Revolution - "Motion"
db.newPage(page_width, page_height)
draw_gradient_background(colors["orange"], colors["warm_yellow"], 35)

# Circular composition
center_x = page_width / 2
center_y = page_height / 2 + 100

# Video frames
for i in range(8):
    angle = (i / 8) * math.pi * 2
    frame_x = center_x + math.cos(angle) * 150
    frame_y = center_y + math.sin(angle) * 150
    
    # Transparent frames
    db.fill(*colors["white"], 0.1 + i * 0.05)
    db.rect(frame_x - 40, frame_y - 30, 80, 60)

# Title in motion
db.font(headline_font)
db.fontSize(32)
title = "Creative AI Models: Video Revolution"
# Motion blur effect
for blur in range(5):
    db.fill(*colors["white"], 0.2 - blur * 0.03)
    db.text(title, (margin - blur * 2, page_height - 100))

# Circular text for features
features = [
    "5-21 second clips",
    "Cinema-grade quality",
    "$10/month",
    "Image-to-Video",
    "NeRF-like 3D"
]

for i, feature in enumerate(features):
    angle = (i / len(features)) * math.pi * 2 - math.pi / 2
    x = center_x + math.cos(angle) * 180
    y = center_y + math.sin(angle) * 180
    
    db.save()
    db.translate(x, y)
    db.rotate(angle * 180 / math.pi + 90)
    db.fill(*colors["orange"])
    db.font(body_font)
    db.fontSize(14)
    db.text(feature, (0, 0), align="center")
    db.restore()

# Page 5: Market Trends - "Convergence"
db.newPage(page_width, page_height)
draw_gradient_background(colors["orange"], colors["warm_yellow"], 45)

# Title
db.fill(*colors["white"])
db.font(headline_font)
db.fontSize(32)
db.text("Market Signals & Trends", (margin, page_height - 100))

# Three overlapping thought bubbles
trends = [
    ("Authenticity Movement", "Natural wins", margin + 50, page_height - 300),
    ("China's AI Dominance", "10x advantage", margin + 200, page_height - 250),
    ("Enterprise Adoption", "90% cost cut", margin + 120, page_height - 400)
]

for i, (title, detail, x, y) in enumerate(trends):
    # Thought bubble
    db.fill(*colors["white"], 0.15)
    size = 120 + i * 20
    path = db.BezierPath()
    path.oval(x - size/2, y - size/2, size, size)
    db.drawPath(path)
    
    # Flowing text
    db.fill(*colors["orange"])
    db.font(headline_font)
    db.fontSize(16)
    # Text along wave path
    wave_text = title
    for j, char in enumerate(wave_text):
        char_x = x - len(wave_text) * 4 + j * 8
        char_y = y + math.sin(j * 0.5) * 10
        db.text(char, (char_x, char_y))
    
    db.font(body_font)
    db.fontSize(12)
    db.fill(*colors["white"], 0.8)
    db.text(detail, (x - 30, y - 30))

# Connecting curves
db.stroke(*colors["warm_yellow"], 0.3)
db.strokeWidth(2)
for i in range(len(trends) - 1):
    x1, y1 = trends[i][2], trends[i][3]
    x2, y2 = trends[i + 1][2], trends[i + 1][3]
    path = db.BezierPath()
    path.moveTo((x1, y1))
    path.curveTo((x1 + 50, y1 - 50), (x2 - 50, y2 + 50), (x2, y2))
    db.drawPath(path)
db.stroke(None)

# Page 6: Tools to Test - "Deconstruction"
db.newPage(page_width, page_height)
draw_gradient_background(colors["warm_yellow"], colors["orange"], 30)

# Title
db.fill(*colors["white"])
db.font(headline_font)
db.fontSize(32)
db.text("Tools to Test This Month", (margin, page_height - 100))

# Large background numbers
tools = [
    ("Midjourney V7", "Video prototyping"),
    ("Abacus.AI", "Campaign automation"),
    ("Manus", "$2 task automation")
]

for i, (tool, desc) in enumerate(tools):
    # Giant translucent number
    db.fill(*colors["white"], 0.05)
    db.font(headline_font)
    db.fontSize(200)
    db.text(str(i + 1), (margin + i * 150, page_height - 400))
    
    # Tool info at angle
    angle = -30 + i * 20
    x = margin + 50 + i * 140
    y = page_height - 250 - i * 60
    
    db.save()
    db.translate(x, y)
    db.rotate(angle)
    
    # Brutalist typography with random spacing
    db.fill(*colors["orange"])
    db.font(headline_font)
    fs = db.FormattedString()
    for char in tool:
        spacing = random.uniform(-1, 3)
        fs.append(char, fontSize=20, tracking=spacing)
    db.text(fs, (0, 0))
    
    db.font(body_font)
    db.fontSize(12)
    db.fill(*colors["white"], 0.8)
    db.text(desc, (0, -30))
    
    db.restore()

# Page 7: Action Items - "Temporal Shift"
db.newPage(page_width, page_height)
draw_gradient_background(colors["orange"], colors["warm_yellow"], 25)

# Title
db.fill(*colors["white"])
db.font(headline_font)
db.fontSize(32)
db.text("Action Items for Barbarian", (margin, page_height - 100))

# Time spiral
center_x = page_width / 2
center_y = page_height / 2

categories = [
    ("Immediate", ["Midjourney workflow", "AI pricing model", "Update pitches"], 1.0, 0),
    ("Short-term", ["Abacus pilot", "Copyright guidelines", "Authentic templates"], 0.6, 1),
    ("Strategic", ["AI-First positioning", "Platform partnerships", "Proprietary IP"], 0.3, 2)
]

for cat_idx, (category, items, opacity, time_offset) in enumerate(categories):
    # Category positioning
    angle_offset = cat_idx * 2 * math.pi / 3
    cat_x = center_x + math.cos(angle_offset) * 150
    cat_y = center_y + math.sin(angle_offset) * 150
    
    # Category title with temporal effect
    db.fill(*colors["orange"], opacity)
    db.font(headline_font)
    db.fontSize(18 - time_offset * 2)
    
    # Blur simulation for future items
    if time_offset > 0:
        for blur in range(time_offset * 2):
            db.fill(*colors["orange"], opacity / (blur + 1))
            db.text(category, (cat_x - blur, cat_y + blur))
    else:
        db.text(category, (cat_x, cat_y))
    
    # Items
    db.font(body_font)
    db.fontSize(12 - time_offset)
    for i, item in enumerate(items):
        item_y = cat_y - 30 - i * 25
        db.fill(*colors["white"], opacity)
        db.text("• " + item, (cat_x, item_y))

# Time spiral visualization
db.stroke(*colors["warm_yellow"], 0.2)
db.strokeWidth(1)
spiral = db.BezierPath()
for t in range(0, 360, 5):
    angle = t * math.pi / 180
    radius = 50 + t / 3
    x = center_x + math.cos(angle) * radius
    y = center_y + math.sin(angle) * radius
    if t == 0:
        spiral.moveTo((x, y))
    else:
        spiral.lineTo((x, y))
db.drawPath(spiral)
db.stroke(None)

# Page 8: Cost Analysis - "Crystallization"
db.newPage(page_width, page_height)
draw_gradient_background(colors["warm_yellow"], colors["orange"], 20)

# Title
db.fill(*colors["white"])
db.font(headline_font)
db.fontSize(32)
db.text("Cost Analysis", (margin, page_height - 100))

# Data constellation
data_points = [
    ("API Calls", 5, margin + 100, page_height - 200),
    ("Cost", 0.50, margin + 250, page_height - 250),
    ("Time Saved", 5, margin + 150, page_height - 350),
    ("ROI", 1000, margin + 300, page_height - 300)
]

# Connect points
db.stroke(*colors["orange"], 0.3)
db.strokeWidth(1)
for i in range(len(data_points)):
    for j in range(i + 1, len(data_points)):
        x1, y1 = data_points[i][2], data_points[i][3]
        x2, y2 = data_points[j][2], data_points[j][3]
        db.line((x1, y1), (x2, y2))
db.stroke(None)

# Crystalline nodes
for label, value, x, y in data_points:
    # Crystal shape
    db.fill(*colors["white"], 0.2)
    crystal = db.BezierPath()
    crystal.moveTo((x, y + 20))
    crystal.lineTo((x + 15, y))
    crystal.lineTo((x, y - 20))
    crystal.lineTo((x - 15, y))
    crystal.closePath()
    db.drawPath(crystal)
    
    # Data
    db.fill(*colors["orange"])
    db.font(body_font)
    db.fontSize(10)
    db.text(label, (x - 20, y - 35))
    db.font(headline_font)
    db.fontSize(14)
    db.text(str(value), (x - 10, y - 5))

# ROI explosion
roi_x = margin + 300
roi_y = page_height - 450
db.font(headline_font)
# Fragmenting number
for i in range(8):
    angle = (i / 8) * math.pi * 2
    offset = 30 + i * 5
    x = roi_x + math.cos(angle) * offset
    y = roi_y + math.sin(angle) * offset
    size = 48 - i * 4
    opacity = 0.8 - i * 0.08
    db.fill(*colors["orange"], opacity)
    db.fontSize(size)
    db.text("1000%+", (x, y))

# Final crystallization pattern
db.fill(*colors["warm_yellow"], 0.1)
for i in range(12):
    angle = (i / 12) * math.pi * 2
    x = page_width / 2 + math.cos(angle) * 200
    y = 200 + math.sin(angle) * 200
    crystal = db.BezierPath()
    crystal.moveTo((x, y + 10))
    crystal.lineTo((x + 8, y))
    crystal.lineTo((x, y - 10))
    crystal.lineTo((x - 8, y))
    crystal.closePath()
    db.drawPath(crystal)

# Footer
db.fill(*colors["white"], 0.6)
db.font(body_font)
db.fontSize(10)
db.text("Prepared using AI Intelligence gathering tools", (margin, 40))
db.text("Visual journey from rigid to fluid intelligence", (margin, 20))

# Save the PDF
db.saveImage("/Users/amadad/Projects/drawbot-redux/output/barbarian_ai_report_expressive.pdf")
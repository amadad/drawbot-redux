# Barbarian Monthly AI Intelligence Brief - The Evolution of Intelligence
# An emotionally expressive, visually dynamic multi-page PDF report
# Transforming data into visual poetry using advanced DrawBot techniques

import drawBot as db
import math
import random
from AppKit import NSBezierPath

# Document setup
page_width = 816
page_height = 1056
margin = 72
gutter = 36
gradient_path = "/Users/amadad/Projects/drawbot-redux/files/gradient/"

# Color evolution across pages
color_schemes = [
    # Page 1-2: Deep blue to purple
    {'primary': (0.04, 0.09, 0.16), 'secondary': (0.29, 0.08, 0.55), 'accent': (0.5, 0.3, 0.8)},
    # Page 3-4: Purple to magenta  
    {'primary': (0.29, 0.08, 0.55), 'secondary': (0.68, 0.08, 0.34), 'accent': (0.8, 0.3, 0.6)},
    # Page 5-6: Magenta to orange
    {'primary': (0.68, 0.08, 0.34), 'secondary': (1.0, 0.44, 0.0), 'accent': (1.0, 0.6, 0.3)},
    # Page 7-8: Orange to warm yellow
    {'primary': (1.0, 0.44, 0.0), 'secondary': (1.0, 0.7, 0.0), 'accent': (1.0, 0.85, 0.3)}
]

# Helper functions for organic variations
def breathing_space(base_space, time, amplitude=0.3):
    """Create breathing letter spacing"""
    return base_space + math.sin(time) * amplitude * base_space

def organic_path(x, y, width, height, complexity=5):
    """Create organic bezier path"""
    path = db.BezierPath()
    points = []
    for i in range(complexity):
        angle = (i / complexity) * 2 * math.pi
        rx = width/2 + random.uniform(-20, 20)
        ry = height/2 + random.uniform(-20, 20)
        px = x + width/2 + rx * math.cos(angle)
        py = y + height/2 + ry * math.sin(angle)
        points.append((px, py))
    
    path.moveTo(points[0])
    for i in range(len(points)):
        next_point = points[(i + 1) % len(points)]
        ctrl1 = (points[i][0] + random.uniform(-10, 10), points[i][1] + random.uniform(-10, 10))
        ctrl2 = (next_point[0] + random.uniform(-10, 10), next_point[1] + random.uniform(-10, 10))
        path.curveTo(ctrl1, ctrl2, next_point)
    path.closePath()
    return path

def fragmented_text(txt, x, y, font_size, fragments=5):
    """Create fragmented and reassembling text effect"""
    for i, char in enumerate(txt):
        frag_x = x + i * font_size * 0.6
        frag_y = y
        
        # Create fragment offset
        offset_x = random.uniform(-2, 2) * (1 - i/len(txt))
        offset_y = random.uniform(-2, 2) * (1 - i/len(txt))
        
        db.save()
        db.translate(frag_x + offset_x, frag_y + offset_y)
        db.rotate(random.uniform(-2, 2) * (1 - i/len(txt)))
        
        # Draw character with varying opacity
        opacity = 0.7 + 0.3 * (i/len(txt))
        db.fill(1, 1, 1, opacity)
        db.text(char, (0, 0))
        db.restore()

def neural_network_bg(x, y, width, height, color_scheme):
    """Create neural pathway background pattern"""
    nodes = []
    for _ in range(20):
        node_x = random.uniform(x, x + width)
        node_y = random.uniform(y, y + height)
        nodes.append((node_x, node_y))
    
    # Draw connections
    db.strokeWidth(0.5)
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes[i+1:], i+1):
            distance = math.sqrt((node2[0]-node1[0])**2 + (node2[1]-node1[1])**2)
            if distance < 200:
                opacity = 1 - (distance / 200)
                db.stroke(*color_scheme['accent'], opacity * 0.3)
                db.line(node1, node2)
    
    # Draw nodes
    for node in nodes:
        db.fill(*color_scheme['accent'], 0.4)
        db.oval(node[0]-3, node[1]-3, 6, 6)

# PAGE 1: COVER - "AWAKENING"
db.newPage(page_width, page_height)

# Gradient background
db.image(gradient_path + "RB Gradient Background 045.jpg", (0, 0), (page_width, page_height))

# Neural network overlay
neural_network_bg(0, 0, page_width, page_height, color_schemes[0])

# Fragmenting title
db.font("Helvetica-Bold")
db.fontSize(72)
db.fill(1, 1, 1)

title_parts = ["AI", "INTELLIGENCE", "BRIEF"]
y_pos = page_height - 200

for i, part in enumerate(title_parts):
    x_pos = margin
    y_pos -= 80
    
    # Create fragmented effect
    fragmented_text(part, x_pos, y_pos, 72)

# Morphing geometric shapes
db.save()
db.translate(page_width/2, page_height/2)
for i in range(5):
    rotation = i * 72
    db.rotate(rotation)
    
    # Shape morphs from square to circle
    morph_factor = i / 4
    path = db.BezierPath()
    if morph_factor < 0.5:
        # More square-like
        size = 100 - i * 10
        path.rect(-size/2, -size/2, size, size)
    else:
        # More circle-like
        size = 100 - i * 10
        path.oval(-size/2, -size/2, size, size)
    
    db.fill(*color_schemes[0]['secondary'], 0.3)
    db.drawPath(path)
db.restore()

# Subtitle with breathing typography
db.font("Helvetica")
db.fontSize(24)
formatted = db.FormattedString()
subtitle = "The Evolution of Intelligence"
for i, char in enumerate(subtitle):
    space = breathing_space(0.5, i * 0.3)
    formatted.append(char, font="Helvetica", fontSize=24, 
                    fill=(1, 1, 1, 0.8), tracking=space)
db.text(formatted, (margin, margin + 100))

# Organization and date
db.fontSize(18)
db.fill(1, 1, 1, 0.6)
db.text("The Barbarian Group", (margin, margin + 60))
db.text("July 2025", (margin, margin + 30))

# PAGE 2: EXECUTIVE SUMMARY - "PULSE"
db.newPage(page_width, page_height)

# Different gradient
db.image(gradient_path + "RB Gradient Background 112.jpg", (0, 0), (page_width, page_height))

# Pulse wave path for text
pulse_path = db.BezierPath()
pulse_x = margin
pulse_y = page_height - 200
pulse_width = page_width - 2 * margin

# Create heartbeat pattern
pulse_points = []
for i in range(20):
    x = pulse_x + (i/19) * pulse_width
    if i % 5 == 2:
        y = pulse_y + 30  # Peak
    elif i % 5 == 3:
        y = pulse_y - 20  # Valley
    else:
        y = pulse_y
    pulse_points.append((x, y))

# Draw pulse line
db.stroke(*color_schemes[0]['accent'], 0.5)
db.strokeWidth(2)
db.fill(None)
pulse_path.moveTo(pulse_points[0])
for point in pulse_points[1:]:
    pulse_path.lineTo(point)
db.drawPath(pulse_path)

# Title along pulse
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[0]['secondary'])
db.text("Executive Summary", (margin, page_height - 150))

# Key points with variable weight
key_points = [
    ("AI landscape shifted to autonomous agents", 1.0),
    ("Manus AI: $2/task game-changer", 0.9),
    ("Midjourney launches video at $10/month", 0.8),
    ("Abacus.AI positions as enterprise 'AI Brain'", 0.7),
    ("Shift toward authentic, less polished content", 0.6)
]

y_position = page_height - 300
for point, importance in key_points:
    # Variable weight based on importance
    font_size = 16 + importance * 8
    opacity = 0.5 + importance * 0.5
    
    db.font("Helvetica")
    db.fontSize(font_size)
    db.fill(0, 0, 0, opacity)
    
    # Text with expanding/contracting letter spacing
    formatted = db.FormattedString()
    for i, char in enumerate(point):
        tracking = -0.2 + importance * 0.4
        formatted.append(char, tracking=tracking)
    
    db.text(formatted, (margin + 20, y_position))
    y_position -= font_size * 2

# Overlapping translucent layers
for i in range(3):
    db.save()
    db.fill(*color_schemes[0]['accent'], 0.1)
    path = organic_path(margin + i * 50, 200 + i * 30, 400, 200)
    db.drawPath(path)
    db.restore()

# PAGE 3: AI PLATFORMS - "BREAKING FREE"
db.newPage(page_width, page_height)

# Gradient transition
db.image(gradient_path + "RB Gradient Background 234.jpg", (0, 0), (page_width, page_height))

# Breaking grid effect
grid_size = 60
cols = int((page_width - 2 * margin) / grid_size)
rows = 8

db.font("Helvetica-Bold")
db.fontSize(42)
db.fill(*color_schemes[1]['primary'])
db.text("AI Agent Platforms", (margin, page_height - 120))
db.text("Breaking Free", (margin, page_height - 170))

# Platform information breaking out of grid
platforms = [
    {"name": "MANUS AI", "info": "Autonomous agents\n$2 per task\n90% cheaper", "break": 3},
    {"name": "ABACUS.AI", "info": "DeepAgent\nAI Brain for orgs\nAutonomous creation", "break": 2},
    {"name": "CHATGPT", "info": "Evolution to reasoning\nDeepResearch\nBeyond conversation", "break": 1}
]

for i, platform in enumerate(platforms):
    col = i % cols
    row = i // cols
    
    base_x = margin + col * grid_size * 2
    base_y = page_height - 300 - row * grid_size * 2
    
    # Breaking free animation
    break_factor = platform['break']
    offset_x = random.uniform(-20, 20) * break_factor
    offset_y = random.uniform(-20, 20) * break_factor
    rotation = random.uniform(-10, 10) * break_factor
    
    db.save()
    db.translate(base_x + offset_x, base_y + offset_y)
    db.rotate(rotation)
    
    # Platform name with kinetic effect
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.fill(*color_schemes[1]['secondary'])
    
    # Kinetic typography
    for j, char in enumerate(platform['name']):
        char_x = j * 14
        char_y = math.sin(j * 0.5) * 3
        db.text(char, (char_x, char_y))
    
    # Platform info
    db.font("Helvetica")
    db.fontSize(12)
    db.fill(0, 0, 0, 0.7)
    db.textBox(platform['info'], (0, -60, 150, 50))
    
    db.restore()

# Diagonal momentum lines
db.stroke(*color_schemes[1]['accent'], 0.3)
db.strokeWidth(1)
for i in range(10):
    start_x = random.uniform(0, page_width)
    start_y = random.uniform(0, page_height)
    end_x = start_x + random.uniform(50, 200)
    end_y = start_y - random.uniform(50, 200)
    db.line((start_x, start_y), (end_x, end_y))

# PAGE 4: VIDEO REVOLUTION - "MOTION"
db.newPage(page_width, page_height)

# Motion gradient
db.image(gradient_path + "RB Gradient Background 367.jpg", (0, 0), (page_width, page_height))

# Title
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[1]['secondary'])
db.text("Video Revolution", (margin, page_height - 120))

# Circular text composition for Midjourney
center_x = page_width / 2
center_y = page_height / 2
radius = 150

# Motion blur effect simulation
for blur in range(5):
    opacity = 0.2 - blur * 0.03
    db.fill(*color_schemes[1]['accent'], opacity)
    
    # Circular text
    text_content = "MIDJOURNEY V7 + VIDEO • 5-21 SECONDS • CINEMA GRADE • "
    char_angle = 360 / len(text_content)
    
    db.font("Helvetica-Bold")
    db.fontSize(16)
    
    for i, char in enumerate(text_content):
        angle = i * char_angle + blur * 2
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        
        db.save()
        db.translate(x, y)
        db.rotate(angle + 90)
        db.text(char, (0, 0))
        db.restore()

# Overlapping video frames
frame_data = [
    "Image-to-Video Animation",
    "$10/month tier",
    "NeRF-like 3D capabilities",
    "60-second videos possible",
    "Real-time generation coming"
]

for i, data in enumerate(frame_data):
    frame_x = margin + i * 30
    frame_y = 300 - i * 20
    frame_width = 300
    frame_height = 180
    
    # Transparent frame
    db.fill(*color_schemes[1]['primary'], 0.1 + i * 0.05)
    db.rect(frame_x, frame_y, frame_width, frame_height)
    
    # Frame content
    db.fill(0, 0, 0, 0.7)
    db.font("Helvetica")
    db.fontSize(14)
    db.textBox(data, (frame_x + 20, frame_y + 20, frame_width - 40, frame_height - 40))

# Legal alert box
db.fill(1, 0, 0, 0.1)
db.rect(margin, 100, page_width - 2 * margin, 80)
db.fill(1, 0, 0, 0.8)
db.font("Helvetica-Bold")
db.fontSize(16)
db.text("⚠️ LEGAL ALERT", (margin + 20, 150))
db.font("Helvetica")
db.fontSize(12)
db.fill(0, 0, 0, 0.8)
db.text("Disney/Universal lawsuit - agencies need clear usage policies", (margin + 20, 120))

# PAGE 5: MARKET TRENDS - "CONVERGENCE"
db.newPage(page_width, page_height)

# Convergence gradient
db.image(gradient_path + "RB Gradient Background 489.jpg", (0, 0), (page_width, page_height))

# Title
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[2]['primary'])
db.text("Market Signals", (margin, page_height - 120))

# Three overlapping thought bubbles
trends = [
    {"title": "Authenticity Movement", 
     "content": "Over-produced content\nlosing engagement\nNatural style winning"},
    {"title": "China's AI Dominance",
     "content": "10x cost advantages\nPractical applications\nPartnership opportunities"},
    {"title": "Enterprise Adoption",
     "content": "Autonomous HR/dev/CS\n90% cost reduction\n'AI employees' pitch"}
]

bubble_centers = [
    (page_width * 0.3, page_height * 0.6),
    (page_width * 0.5, page_height * 0.5),
    (page_width * 0.7, page_height * 0.6)
]

for i, (trend, center) in enumerate(zip(trends, bubble_centers)):
    # Thought bubble shape
    db.save()
    
    # Main bubble
    db.fill(*color_schemes[2]['accent'], 0.15)
    bubble_path = organic_path(center[0] - 120, center[1] - 80, 240, 160, complexity=8)
    db.drawPath(bubble_path)
    
    # Title with variable weight
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.fill(*color_schemes[2]['secondary'])
    db.text(trend['title'], (center[0] - 80, center[1] + 20))
    
    # Flowing text
    db.font("Helvetica")
    db.fontSize(12)
    db.fill(0, 0, 0, 0.7)
    
    # Text following stream path
    lines = trend['content'].split('\n')
    for j, line in enumerate(lines):
        wave_offset = math.sin(j * 0.5) * 10
        db.text(line, (center[0] - 80 + wave_offset, center[1] - 20 - j * 18))
    
    db.restore()

# Connecting streams between bubbles
db.stroke(*color_schemes[2]['accent'], 0.3)
db.strokeWidth(2)
db.fill(None)
for i in range(len(bubble_centers) - 1):
    path = db.BezierPath()
    start = bubble_centers[i]
    end = bubble_centers[i + 1]
    
    # Curved connection
    ctrl1 = (start[0] + 50, start[1] - 30)
    ctrl2 = (end[0] - 50, end[1] - 30)
    
    path.moveTo(start)
    path.curveTo(ctrl1, ctrl2, end)
    db.drawPath(path)

# Abstract patterns in negative space
for _ in range(20):
    x = random.uniform(margin, page_width - margin)
    y = random.uniform(200, page_height - 200)
    size = random.uniform(5, 15)
    
    db.fill(*color_schemes[2]['primary'], random.uniform(0.05, 0.15))
    db.oval(x, y, size, size)

# PAGE 6: TOOLS TO TEST - "DECONSTRUCTION"
db.newPage(page_width, page_height)

# Deconstructed gradient
db.image(gradient_path + "RB Gradient Background 612.jpg", (0, 0), (page_width, page_height))

# Title
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[2]['secondary'])
db.text("Tools to Test", (margin, page_height - 120))

# Deconstructed grid
tools = [
    {"number": "1", "name": "Midjourney V7", "action": "Set up team account for video prototyping"},
    {"number": "2", "name": "Abacus.AI Trial", "action": "Test DeepAgent for campaign automation"},
    {"number": "3", "name": "Manus Waitlist", "action": "Join for early access to $2 task automation"}
]

for i, tool in enumerate(tools):
    # Large translucent number background
    db.save()
    
    # Random angle for deconstruction
    angle = random.uniform(-15, 15)
    x_base = margin + (i % 2) * 300
    y_base = page_height - 300 - (i // 2) * 200
    
    db.translate(x_base, y_base)
    db.rotate(angle)
    
    # Big number
    db.font("Helvetica-Bold")
    db.fontSize(120)
    db.fill(*color_schemes[2]['accent'], 0.1)
    db.text(tool['number'], (0, 0))
    
    # Tool name - brutalist spacing
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.fill(*color_schemes[2]['primary'])
    
    formatted = db.FormattedString()
    for char in tool['name']:
        tracking = random.uniform(-0.5, 2)
        formatted.append(char, tracking=tracking)
    db.text(formatted, (40, 40))
    
    # Action - non-linear path
    db.font("Helvetica")
    db.fontSize(12)
    db.fill(0, 0, 0, 0.7)
    
    # Text on curve
    action_path = db.BezierPath()
    action_path.moveTo((40, 0))
    action_path.curveTo((100, -10), (150, 10), (200, 0))
    
    db.textBox(tool['action'], (40, -20, 250, 60))
    
    db.restore()

# PAGE 7: ACTION ITEMS - "TEMPORAL SHIFT"
db.newPage(page_width, page_height)

# Temporal gradient
db.image(gradient_path + "RB Gradient Background 745.jpg", (0, 0), (page_width, page_height))

# Title
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[3]['primary'])
db.text("Action Items", (margin, page_height - 120))

# Time categories with different visual treatments
timeframes = [
    {
        "title": "IMMEDIATE",
        "items": [
            "Create Midjourney video workflow",
            "Develop AI agent pricing model",
            "Update pitch decks with AI capabilities"
        ],
        "style": {"weight": "Bold", "opacity": 1.0, "blur": 0}
    },
    {
        "title": "SHORT-TERM",
        "items": [
            "Run pilot project with Abacus.AI",
            "Develop AI copyright guidelines",
            "Create 'authentic content' template"
        ],
        "style": {"weight": "Regular", "opacity": 0.7, "blur": 1}
    },
    {
        "title": "STRATEGIC",
        "items": [
            "Position as 'AI-First Creative Agency'",
            "Build AI platform partnerships",
            "Develop proprietary AI workflow IP"
        ],
        "style": {"weight": "Light", "opacity": 0.4, "blur": 2}
    }
]

y_position = page_height - 200

for timeframe in timeframes:
    # Section title
    db.font(f"Helvetica-{timeframe['style']['weight']}")
    db.fontSize(24)
    db.fill(*color_schemes[3]['secondary'], timeframe['style']['opacity'])
    db.text(timeframe['title'], (margin, y_position))
    
    y_position -= 40
    
    # Items with temporal effects
    for item in timeframe['items']:
        # Simulate blur with multiple overlays
        for blur in range(timeframe['style']['blur'] + 1):
            offset = blur * 0.5
            opacity = timeframe['style']['opacity'] / (blur + 1)
            
            db.font("Helvetica")
            db.fontSize(14)
            db.fill(0, 0, 0, opacity)
            db.text(f"□ {item}", (margin + 20 + offset, y_position))
        
        y_position -= 25
    
    y_position -= 20

# Temporal visualization
db.save()
db.translate(page_width - 200, page_height/2)

# Time spiral
for i in range(50):
    angle = i * 10
    radius = i * 2
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    
    opacity = 1 - (i / 50)
    size = 5 - (i / 50) * 4
    
    db.fill(*color_schemes[3]['accent'], opacity * 0.3)
    db.oval(x - size/2, y - size/2, size, size)

db.restore()

# PAGE 8: COST ANALYSIS - "CRYSTALLIZATION"
db.newPage(page_width, page_height)

# Final gradient - warm crystallization
db.image(gradient_path + "RB Gradient Background 867.jpg", (0, 0), (page_width, page_height))

# Title
db.font("Helvetica-Bold")
db.fontSize(48)
db.fill(*color_schemes[3]['secondary'])
db.text("Cost Analysis", (margin, page_height - 120))

# Data constellation
data_points = [
    {"label": "API Calls", "value": "5", "x": 0.3, "y": 0.7},
    {"label": "Cost", "value": "$0.50", "x": 0.5, "y": 0.6},
    {"label": "Time Saved", "value": "4-6 hrs", "x": 0.7, "y": 0.7},
    {"label": "ROI", "value": "1000%+", "x": 0.5, "y": 0.8}
]

# Draw constellation connections
db.stroke(*color_schemes[3]['accent'], 0.3)
db.strokeWidth(1)
for i in range(len(data_points)):
    for j in range(i + 1, len(data_points)):
        start = (data_points[i]['x'] * page_width, data_points[i]['y'] * page_height)
        end = (data_points[j]['x'] * page_width, data_points[j]['y'] * page_height)
        db.line(start, end)

# Draw data points
for point in data_points:
    x = point['x'] * page_width
    y = point['y'] * page_height
    
    # Crystalline node
    db.fill(*color_schemes[3]['primary'], 0.8)
    for angle in range(0, 360, 60):
        db.save()
        db.translate(x, y)
        db.rotate(angle)
        db.rect(-2, -10, 4, 20)
        db.restore()
    
    # Label
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.fill(*color_schemes[3]['secondary'])
    db.text(point['label'], (x - 30, y + 20))
    
    # Value
    db.font("Helvetica")
    db.fontSize(18)
    db.fill(0, 0, 0, 0.8)
    db.text(point['value'], (x - 30, y - 5))

# ROI fragmentation effect
roi_x = page_width/2
roi_y = 300

db.font("Helvetica-Bold")
db.fontSize(72)

# Fragment the ROI number into particles
for i in range(30):
    particle_x = roi_x + random.uniform(-100, 100)
    particle_y = roi_y + random.uniform(-50, 50)
    size = random.uniform(2, 8)
    opacity = random.uniform(0.1, 0.4)
    
    db.fill(*color_schemes[3]['accent'], opacity)
    db.oval(particle_x, particle_y, size, size)

# Central ROI text
db.fill(*color_schemes[3]['secondary'], 0.8)
db.text("1000%+", (roi_x - 100, roi_y))

# Footer
db.font("Helvetica")
db.fontSize(12)
db.fill(0, 0, 0, 0.6)
db.textBox("Prepared using AI Intelligence gathering tools. For questions or deep dives on any topic, contact your innovation team.",
          (margin, margin, page_width - 2 * margin, 50))

# Final crystallization pattern
for _ in range(50):
    x = random.uniform(0, page_width)
    y = random.uniform(0, 200)
    
    # Crystal shape
    db.save()
    db.translate(x, y)
    db.rotate(random.uniform(0, 360))
    db.fill(*color_schemes[3]['accent'], random.uniform(0.05, 0.2))
    db.rect(-1, -5, 2, 10)
    db.rotate(90)
    db.rect(-1, -5, 2, 10)
    db.restore()

# Save the PDF
db.saveImage("/Users/amadad/Projects/drawbot-redux/output/barbarian_ai_report.pdf")
print("PDF report generated successfully!")
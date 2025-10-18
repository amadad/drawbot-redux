import drawBot as db
import math

# Letter size dimensions
WIDTH = 612
HEIGHT = 792

# Grid settings
MARGIN = 50
COLS = 2
ROWS = 3
GUTTER = 30

# Calculate cell dimensions - leave more room at bottom
CELL_WIDTH = (WIDTH - 2 * MARGIN - (COLS - 1) * GUTTER) / COLS
CELL_HEIGHT = (HEIGHT - 2 * MARGIN - 150 - (ROWS - 1) * GUTTER) / ROWS  # More space for header and footer

# Color palette based on emotional valence
COLORS = {
    "joy": (1, 0.8, 0.2),      # Bright yellow
    "sadness": (0.2, 0.3, 0.7),  # Deep blue
    "anger": (0.9, 0.2, 0.2),    # Red
    "fear": (0.3, 0.2, 0.4),     # Dark purple
    "surprise": (1, 0.5, 0.2),   # Orange
    "calm": (0.3, 0.7, 0.6)      # Teal
}

# Emotion data
EMOTIONS = [
    {
        "name": "Joy",
        "scientific": "Euphoria Circularis",
        "description": "Expansive radial energy",
        "color": COLORS["joy"]
    },
    {
        "name": "Sadness", 
        "scientific": "Melancholia Descendens",
        "description": "Downward gravitational pull",
        "color": COLORS["sadness"]
    },
    {
        "name": "Anger",
        "scientific": "Ira Angularis", 
        "description": "Sharp angular disruption",
        "color": COLORS["anger"]
    },
    {
        "name": "Fear",
        "scientific": "Timor Fragmentalis",
        "description": "Fragmented scatter pattern",
        "color": COLORS["fear"]
    },
    {
        "name": "Surprise",
        "scientific": "Stupor Explosiva",
        "description": "Outward burst dynamics",
        "color": COLORS["surprise"]
    },
    {
        "name": "Calm",
        "scientific": "Tranquillitas Fluida",
        "description": "Smooth wave oscillation",
        "color": COLORS["calm"]
    }
]


def draw_joy_shape(x, y, size):
    """Draw expanding circular forms with radiating elements"""
    # Central circle
    db.fill(*COLORS["joy"], 0.8)
    db.stroke(None)
    db.oval(x - size/4, y - size/4, size/2, size/2)
    
    # Radiating elements
    for i in range(12):
        angle = i * (360 / 12)
        rad = math.radians(angle)
        
        # Calculate positions
        start_x = x + math.cos(rad) * size/4
        start_y = y + math.sin(rad) * size/4
        end_x = x + math.cos(rad) * size/2
        end_y = y + math.sin(rad) * size/2
        
        # Draw radiating lines
        db.stroke(*COLORS["joy"])
        db.strokeWidth(2)
        db.fill(None)
        db.line((start_x, start_y), (end_x, end_y))
        
        # Draw circles at ends
        db.stroke(None)
        db.fill(*COLORS["joy"], 0.4)
        db.oval(end_x - 5, end_y - 5, 10, 10)
    
    # Reset
    db.stroke(None)
    db.fill(None)


def draw_sadness_shape(x, y, size):
    """Draw drooping, curved forms suggesting weight"""
    db.stroke(None)
    db.fill(*COLORS["sadness"], 0.8)
    
    # Main drooping shape
    path = db.BezierPath()
    path.moveTo((x - size/3, y + size/4))
    path.curveTo((x - size/3, y), (x, y - size/4), (x + size/3, y))
    path.curveTo((x + size/3, y - size/4), (x, y - size/2), (x, y - size/2))
    path.curveTo((x, y - size/2), (x - size/2, y - size/3), (x - size/3, y + size/4))
    db.drawPath(path)
    
    # Falling drops
    for i in range(3):
        drop_x = x - size/4 + i * size/4
        drop_y = y - size/2 - i * 10
        
        db.fill(*COLORS["sadness"], 0.4)
        db.oval(drop_x - 5, drop_y - 10, 10, 20)
    
    db.fill(None)


def draw_anger_shape(x, y, size):
    """Draw sharp, angular zigzag patterns"""
    db.stroke(None)
    db.fill(*COLORS["anger"], 0.8)
    
    # Zigzag pattern
    path = db.BezierPath()
    points = []
    segments = 8
    
    for i in range(segments + 1):
        px = x - size/2 + (i * size / segments)
        if i % 2 == 0:
            py = y - size/3
        else:
            py = y + size/3
        points.append((px, py))
    
    path.moveTo(points[0])
    for point in points[1:]:
        path.lineTo(point)
    
    # Add sharp spikes
    for i in range(1, len(points) - 1):
        if i % 2 == 1:
            spike_x = points[i][0]
            spike_y = points[i][1] + size/6
            path.moveTo(points[i])
            path.lineTo((spike_x - size/12, spike_y))
            path.lineTo((spike_x + size/12, spike_y))
            path.lineTo(points[i])
    
    db.drawPath(path)
    db.fill(None)


def draw_fear_shape(x, y, size):
    """Draw fragmented, scattered elements"""
    db.stroke(None)
    
    # Scattered fragments
    fragments = 15
    for i in range(fragments):
        # Random-like distribution using golden angle
        angle = i * 137.5
        distance = (i / fragments) * size/2
        frag_x = x + math.cos(math.radians(angle)) * distance
        frag_y = y + math.sin(math.radians(angle)) * distance
        
        # Fragment size decreases with distance
        frag_size = 8 - (i / fragments) * 5
        
        # Draw irregular fragment
        path = db.BezierPath()
        path.moveTo((frag_x, frag_y))
        path.lineTo((frag_x + frag_size, frag_y + frag_size/2))
        path.lineTo((frag_x + frag_size/2, frag_y + frag_size))
        path.lineTo((frag_x - frag_size/2, frag_y + frag_size/3))
        path.closePath()
        
        db.fill(*COLORS["fear"], 0.8 - (i / fragments) * 0.4)
        db.drawPath(path)
    
    db.fill(None)


def draw_surprise_shape(x, y, size):
    """Draw burst pattern with dynamic lines"""
    # Central burst point
    db.stroke(None)
    db.fill(*COLORS["surprise"], 0.8)
    db.oval(x - size/8, y - size/8, size/4, size/4)
    
    # Burst lines
    bursts = 16
    for i in range(bursts):
        angle = i * (360 / bursts)
        rad = math.radians(angle)
        
        # Alternating lengths
        if i % 2 == 0:
            length = size/2
            width = 3
        else:
            length = size/3
            width = 2
        
        # Draw burst line
        end_x = x + math.cos(rad) * length
        end_y = y + math.sin(rad) * length
        
        db.fill(None)
        db.stroke(*COLORS["surprise"])
        db.strokeWidth(width)
        db.line((x, y), (end_x, end_y))
        
        # Add emphasis dots
        if i % 4 == 0:
            db.stroke(None)
            db.fill(*COLORS["surprise"])
            db.oval(end_x - 4, end_y - 4, 8, 8)
    
    # Clear all states
    db.stroke(None)
    db.fill(None)


def draw_calm_shape(x, y, size):
    """Draw smooth, flowing wave forms"""
    db.stroke(None)
    
    # Multiple wave layers
    for layer in range(3):
        path = db.BezierPath()
        wave_height = size/6 - layer * 5
        wave_y = y - layer * 15
        
        # Start point
        path.moveTo((x - size/2, wave_y))
        
        # Create smooth wave
        control_offset = size/6
        path.curveTo(
            (x - size/4, wave_y + wave_height),
            (x - control_offset, wave_y + wave_height),
            (x, wave_y)
        )
        path.curveTo(
            (x + control_offset, wave_y - wave_height),
            (x + size/4, wave_y - wave_height),
            (x + size/2, wave_y)
        )
        
        db.fill(*COLORS["calm"], 0.8 - layer * 0.2)
        db.drawPath(path)
    
    db.fill(None)


def draw_emotion_cell(x, y, emotion_data, index):
    """Draw a single emotion cell with shape and labels"""
    # Save state
    db.save()
    
    # Draw subtle background
    db.stroke(None)
    db.fill(0.97)
    db.rect(x, y, CELL_WIDTH, CELL_HEIGHT)
    
    # Draw border
    db.fill(None)
    db.stroke(0.9)
    db.strokeWidth(1)
    db.rect(x, y, CELL_WIDTH, CELL_HEIGHT)
    
    # Clear stroke and fill
    db.stroke(None)
    db.fill(None)
    
    # Calculate center for shape
    center_x = x + CELL_WIDTH / 2
    center_y = y + CELL_HEIGHT / 2 + 20
    
    # Draw the appropriate shape
    shape_size = min(CELL_WIDTH, CELL_HEIGHT) * 0.5
    
    if index == 0:
        draw_joy_shape(center_x, center_y, shape_size)
    elif index == 1:
        draw_sadness_shape(center_x, center_y, shape_size)
    elif index == 2:
        draw_anger_shape(center_x, center_y, shape_size)
    elif index == 3:
        draw_fear_shape(center_x, center_y, shape_size)
    elif index == 4:
        draw_surprise_shape(center_x, center_y, shape_size)
    elif index == 5:
        draw_calm_shape(center_x, center_y, shape_size)
    
    # Draw labels
    # Scientific name
    db.stroke(None)
    db.font("Helvetica-Oblique", 12)
    db.fill(0.3)
    db.text(emotion_data["scientific"], (center_x, y + 30), align="center")
    
    # Common name
    db.font("Helvetica-Bold", 16)
    db.fill(0.1)
    db.text(emotion_data["name"], (center_x, y + 50), align="center")
    
    # Description
    db.font("Helvetica", 10)
    db.fill(0.5)
    db.text(emotion_data["description"], (center_x, y + 15), align="center")
    
    # Restore state
    db.restore()


# Create the PDF
db.newPage(WIDTH, HEIGHT)

# White background
db.fill(1)
db.stroke(None)
db.rect(0, 0, WIDTH, HEIGHT)

# Draw title
db.font("Helvetica-Bold", 24)
db.fill(0.1)
db.text("Emotional Geometry: A Visual Classification", (WIDTH/2, HEIGHT - 40), align="center")

# Draw subtitle
db.font("Helvetica", 12)
db.fill(0.4)
db.text("Abstract representations of human emotional states", (WIDTH/2, HEIGHT - 65), align="center")

# Draw emotion grid
for row in range(ROWS):
    for col in range(COLS):
        index = row * COLS + col
        if index < len(EMOTIONS):
            x = MARGIN + col * (CELL_WIDTH + GUTTER)
            y = HEIGHT - MARGIN - 100 - (row + 1) * (CELL_HEIGHT + GUTTER)
            draw_emotion_cell(x, y, EMOTIONS[index], index)

# Clear any remaining graphics state
db.stroke(None)
db.fill(None)

# Draw intensity scale legend in a clear area
legend_y = 70
db.font("Helvetica", 10)
db.fill(0.3)
db.text("Emotional Intensity Scale:", (MARGIN, legend_y))

# Draw gradient bar
gradient_width = 200
gradient_height = 10
gradient_x = MARGIN + 140

# Draw gradient with proper background
db.save()
db.fill(0.95)
db.stroke(None)
db.rect(gradient_x - 2, legend_y - 20, gradient_width + 4, gradient_height + 4)

# Draw the gradient itself
for i in range(gradient_width):
    intensity = i / gradient_width
    gray = 0.9 - intensity * 0.7
    db.fill(gray)
    db.rect(gradient_x + i, legend_y - 18, 1, gradient_height)

# Scale labels
db.fill(0.4)
db.font("Helvetica", 8)
db.text("Low", (gradient_x - 10, legend_y - 15), align="right")
db.text("High", (gradient_x + gradient_width + 10, legend_y - 15), align="left")
db.restore()

# Footer - ensure it's in a clear area
db.font("Helvetica", 8)
db.fill(0.6)
db.text("Figure 1. Geometric abstraction of primary emotional states", (WIDTH/2, 25), align="center")

# Save as PDF
db.saveImage("output/emotional_geometry_fixed.pdf")
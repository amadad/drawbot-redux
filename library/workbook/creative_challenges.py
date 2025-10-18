"""
Creative DrawBot Challenges
===========================
Open-ended design challenges to push your creative boundaries.
These exercises focus on conceptual thinking and artistic expression.

Each challenge includes:
- Creative brief
- Technical requirements
- Inspiration/references
- Example approach (not the only solution!)
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
import random
import math
import colorsys

# CHALLENGE 1: Emotional Geometry
# Brief: Create an abstract composition that expresses an emotion using only geometric shapes
# Requirements: Use at least 5 different shapes, limited color palette (3 colors max)
# Emotions to choose from: Joy, Anxiety, Calm, Anger, Love

def challenge_1_joy():
    """Example: Joy through upward movement and warm colors"""
    db.newPage(600, 800)
    
    # Warm, bright palette
    colors = [
        (1, 0.8, 0.2),     # Yellow
        (1, 0.4, 0.3),     # Orange
        (1, 0.95, 0.8)     # Light
    ]
    
    # Background
    db.fill(*colors[2])
    db.rect(0, 0, 600, 800)
    
    # Upward flowing circles
    for i in range(50):
        x = random.randint(50, 550)
        y = random.randint(0, 700)
        size = random.randint(20, 120)
        
        db.fill(*colors[random.randint(0, 1)], random.uniform(0.3, 0.8))
        db.oval(x - size/2, y - size/2, size, size)
    
    # Dynamic triangles pointing up
    for i in range(20):
        x = random.randint(100, 500)
        y = random.randint(100, 600)
        
        with db.savedState():
            db.translate(x, y)
            db.rotate(random.uniform(-15, 15))
            
            db.fill(*colors[0], 0.6)
            path = db.BezierPath()
            path.moveTo((0, 0))
            path.lineTo((-30, -80))
            path.lineTo((30, -80))
            path.closePath()
            db.drawPath(path)

# CHALLENGE 2: Typographic Landscape
# Brief: Create a landscape/cityscape using only letters and words
# Requirements: No shapes allowed, only typography. Create depth and perspective
# Inspiration: ASCII art, concrete poetry, typographic illustrations

def challenge_2_example():
    """Example: City skyline from letters"""
    db.newPage(800, 600)
    
    # Sky gradient using periods
    for y in range(40):
        gray = 0.9 - y * 0.01
        db.fill(gray)
        db.font("Courier")
        db.fontSize(8)
        db.text("." * 133, (0, 600 - y * 15))
    
    # Buildings using different characters
    buildings = [
        ("H", 120, 300), ("I", 80, 400), ("M", 150, 350),
        ("T", 100, 380), ("A", 140, 320), ("N", 110, 360)
    ]
    
    db.font("Helvetica-Bold")
    for char, width, height in buildings:
        x = random.randint(50, 650)
        
        # Building body
        for y in range(0, height, 20):
            size = 40 - y // 20
            db.fontSize(size)
            gray = 0.2 + y / height * 0.3
            db.fill(gray)
            
            # Stack characters
            for i in range(width // 20):
                db.text(char, (x + i * 20, y))

# CHALLENGE 3: Sound Visualization
# Brief: Visualize a piece of music or sound without hearing it
# Requirements: Create rhythm, tempo, dynamics through visual elements
# Consider: Loud/soft, fast/slow, smooth/staccato, harmony/dissonance

def challenge_3_jazz():
    """Example: Jazz improvisation visualization"""
    db.newPage(1000, 400)
    
    # Dark background for club atmosphere
    db.fill(0.05, 0.05, 0.1)
    db.rect(0, 0, 1000, 400)
    
    # Base rhythm section
    for x in range(0, 1000, 40):
        db.stroke(0.3, 0.3, 0.5)
        db.strokeWidth(2)
        db.line((x, 0), (x, 400))
    
    # Melodic lines
    db.stroke(None)
    for i in range(5):
        path = db.BezierPath()
        path.moveTo((0, 200))
        
        # Improvised melody
        for x in range(0, 1000, 20):
            y = 200 + math.sin(x * 0.02 + i) * 100 * random.uniform(0.5, 1.5)
            y += random.uniform(-20, 20)  # Jazz "swing"
            
            if x == 0:
                path.moveTo((x, y))
            else:
                # Smooth curves for fluid jazz lines
                path.curveTo(
                    (x - 10, prev_y),
                    (x - 10, y),
                    (x, y)
                )
            prev_y = y
        
        # Each instrument a different color
        colors = [
            (0.9, 0.7, 0.2),  # Brass
            (0.2, 0.5, 0.9),  # Piano
            (0.9, 0.3, 0.3),  # Sax
            (0.4, 0.9, 0.4),  # Bass
            (0.9, 0.5, 0.9)   # Drums
        ]
        
        db.stroke(*colors[i % len(colors)], 0.7)
        db.strokeWidth(3)
        db.fill(None)
        db.drawPath(path)

# CHALLENGE 4: Nature Algorithm
# Brief: Create organic, natural forms using mathematical algorithms
# Requirements: Use recursion, fractals, or L-systems. Make it feel alive
# Examples: Trees, coral, clouds, mountains, rivers

def challenge_4_tree():
    """Example: Recursive tree generation"""
    db.newPage(600, 800)
    
    # Sky gradient
    for y in range(800):
        blue = 0.7 - y / 800 * 0.4
        db.fill(0.9 - y / 800 * 0.1, 0.95 - y / 800 * 0.1, blue)
        db.rect(0, y, 600, 1)
    
    def draw_branch(x, y, length, angle, depth):
        if depth <= 0 or length < 2:
            # Leaf
            db.fill(0.2, 0.6 + random.uniform(-0.1, 0.1), 0.2, 0.8)
            db.oval(x - 3, y - 3, 6, 6)
            return
        
        # Branch color gets lighter with depth
        brown = 0.3 + depth * 0.05
        db.stroke(brown, brown * 0.8, brown * 0.6)
        db.strokeWidth(depth * 0.5)
        
        # Calculate end point
        end_x = x + math.cos(math.radians(angle)) * length
        end_y = y + math.sin(math.radians(angle)) * length
        
        db.line((x, y), (end_x, end_y))
        
        # Recursion with variation
        variation = random.uniform(0.7, 0.9)
        angle_variation = random.uniform(-30, 30)
        
        # Main branches
        draw_branch(end_x, end_y, length * variation, 
                   angle + 25 + angle_variation, depth - 1)
        draw_branch(end_x, end_y, length * variation, 
                   angle - 25 + angle_variation, depth - 1)
        
        # Occasional third branch
        if random.random() > 0.7:
            draw_branch(end_x, end_y, length * variation * 0.8, 
                       angle + random.uniform(-10, 10), depth - 1)
    
    # Draw tree
    random.seed(42)  # For reproducibility
    draw_branch(300, 100, 120, 90, 12)
    db.stroke(None)

# CHALLENGE 5: Time Visualization
# Brief: Visualize the passage of time in a single image
# Requirements: Show past, present, future. Make time tangible
# Consider: Cycles, decay, growth, memory, anticipation

def challenge_5_day_cycle():
    """Example: 24-hour cycle in one image"""
    db.newPage(800, 800)
    
    # Center point
    cx, cy = 400, 400
    
    # Hours as segments
    for hour in range(24):
        angle = hour * 15 - 90  # Start at top
        
        # Time of day colors
        if 6 <= hour < 12:  # Morning
            base_color = (1, 0.8, 0.4)
        elif 12 <= hour < 18:  # Afternoon
            base_color = (0.4, 0.7, 1)
        elif 18 <= hour < 22:  # Evening
            base_color = (0.8, 0.4, 0.6)
        else:  # Night
            base_color = (0.1, 0.1, 0.3)
        
        # Draw hour segment
        with db.savedState():
            db.translate(cx, cy)
            db.rotate(angle)
            
            # Fade based on distance from "now" (let's say 15:00)
            current_hour = 15
            distance = min(abs(hour - current_hour), 
                          24 - abs(hour - current_hour))
            opacity = 1 - distance / 12
            
            db.fill(*base_color, opacity)
            
            # Hour wedge
            path = db.BezierPath()
            path.moveTo((0, 0))
            path.lineTo((300, 0))
            path.arc((0, 0), radius=300, startAngle=0, endAngle=15, clockwise=False)
            path.closePath()
            db.drawPath(path)
            
            # Hour markers
            db.fill(1, 1, 1, opacity)
            db.fontSize(12)
            db.text(str(hour), (250, -5))

# CHALLENGE 6: Impossible Architecture
# Brief: Design architectural structures that couldn't exist in reality
# Requirements: Play with perspective, physics, and perception
# Inspiration: M.C. Escher, Monument Valley game, optical illusions

def challenge_6_infinite_stairs():
    """Example: Penrose stairs variation"""
    db.newPage(800, 800)
    
    # Background
    db.fill(0.95)
    db.rect(0, 0, 800, 800)
    
    # Isometric projection helpers
    def iso_project(x, y, z):
        """Convert 3D to 2D isometric"""
        iso_x = 400 + (x - y) * math.cos(math.radians(30))
        iso_y = 400 - (x + y) * math.sin(math.radians(30)) - z
        return iso_x, iso_y
    
    # Draw impossible stairs
    step_width = 40
    step_height = 20
    steps = 16
    
    for i in range(steps):
        # Calculate position in "impossible" loop
        angle = i * 360 / steps
        radius = 150
        
        x = math.cos(math.radians(angle)) * radius
        y = math.sin(math.radians(angle)) * radius
        # Impossible z that creates illusion
        z = i * step_height % (step_height * 4)
        
        # Project to screen
        sx1, sy1 = iso_project(x, y, z)
        sx2, sy2 = iso_project(x + step_width, y, z)
        sx3, sy3 = iso_project(x + step_width, y + step_width, z)
        sx4, sy4 = iso_project(x, y + step_width, z)
        
        # Top of step
        db.fill(0.8)
        path = db.BezierPath()
        path.moveTo((sx1, sy1))
        path.lineTo((sx2, sy2))
        path.lineTo((sx3, sy3))
        path.lineTo((sx4, sy4))
        path.closePath()
        db.drawPath(path)
        
        # Step face
        db.fill(0.6)
        sx5, sy5 = iso_project(x, y, z - step_height)
        sx6, sy6 = iso_project(x + step_width, y, z - step_height)
        
        face = db.BezierPath()
        face.moveTo((sx1, sy1))
        face.lineTo((sx2, sy2))
        face.lineTo((sx6, sy6))
        face.lineTo((sx5, sy5))
        face.closePath()
        db.drawPath(face)

# CHALLENGE 7: Data Portraits
# Brief: Create abstract portraits using personal data
# Requirements: Transform numbers into visual personality
# Data ideas: Daily routines, music taste, communication patterns, movement

def challenge_7_daily_rhythm():
    """Example: Visualize a person's daily activities"""
    db.newPage(600, 600)
    
    # Sample daily data (24 hours)
    activities = {
        "sleep": [(0, 6), (22, 24)],
        "work": [(9, 12), (13, 17)],
        "commute": [(8, 9), (17, 18)],
        "meals": [(7, 7.5), (12, 13), (18, 19)],
        "exercise": [(6, 7)],
        "leisure": [(19, 22)],
        "morning": [(7.5, 8)]
    }
    
    colors = {
        "sleep": (0.2, 0.2, 0.4),
        "work": (0.8, 0.3, 0.3),
        "commute": (0.6, 0.6, 0.6),
        "meals": (0.9, 0.7, 0.3),
        "exercise": (0.3, 0.8, 0.3),
        "leisure": (0.3, 0.6, 0.9),
        "morning": (0.9, 0.9, 0.6)
    }
    
    # Circular 24-hour visualization
    cx, cy = 300, 300
    radius = 200
    
    # Background circles
    db.fill(0.95)
    db.oval(cx - radius - 50, cy - radius - 50, 
            radius * 2 + 100, radius * 2 + 100)
    
    # Hour marks
    db.stroke(0.8)
    db.strokeWidth(1)
    for hour in range(24):
        angle = hour * 15 - 90
        x1 = cx + math.cos(math.radians(angle)) * (radius - 10)
        y1 = cy + math.sin(math.radians(angle)) * (radius - 10)
        x2 = cx + math.cos(math.radians(angle)) * radius
        y2 = cy + math.sin(math.radians(angle)) * radius
        db.line((x1, y1), (x2, y2))
    db.stroke(None)
    
    # Draw activities as arcs
    for activity, times in activities.items():
        db.fill(*colors[activity], 0.8)
        
        for start, end in times:
            # Convert to angles
            start_angle = start * 15 - 90
            end_angle = end * 15 - 90
            
            # Create arc
            path = db.BezierPath()
            path.moveTo((cx, cy))
            
            # Inner radius varies by activity type
            if activity == "sleep":
                inner_radius = 50
            elif activity == "work":
                inner_radius = 100
            else:
                inner_radius = 150
            
            # Draw wedge
            x1 = cx + math.cos(math.radians(start_angle)) * inner_radius
            y1 = cy + math.sin(math.radians(start_angle)) * inner_radius
            path.lineTo((x1, y1))
            
            x2 = cx + math.cos(math.radians(start_angle)) * radius
            y2 = cy + math.sin(math.radians(start_angle)) * radius
            path.lineTo((x2, y2))
            
            path.arc((cx, cy), radius=radius, startAngle=start_angle, 
                    endAngle=end_angle, clockwise=False)
            
            x3 = cx + math.cos(math.radians(end_angle)) * radius
            y3 = cy + math.sin(math.radians(end_angle)) * radius
            x4 = cx + math.cos(math.radians(end_angle)) * inner_radius
            y4 = cy + math.sin(math.radians(end_angle)) * inner_radius
            path.lineTo((x4, y4))
            
            path.arc((cx, cy), radius=inner_radius, startAngle=end_angle,
                    endAngle=start_angle, clockwise=True)
            
            path.closePath()
            db.drawPath(path)

# CHALLENGE 8: Synesthetic Design
# Brief: Translate one sense into another (sound to sight, taste to color, etc.)
# Requirements: Create a system that consistently maps sensory experiences
# Example: What does "sweet" look like? How does "rough" sound visually?

def challenge_8_taste_palette():
    """Example: Visualizing taste profiles"""
    db.newPage(800, 600)
    
    # Background
    db.fill(0.98)
    db.rect(0, 0, 800, 600)
    
    # Taste profiles
    tastes = {
        "sweet": {
            "color": (1, 0.8, 0.9),
            "shape": "circle",
            "pattern": "smooth",
            "position": (200, 400)
        },
        "sour": {
            "color": (0.9, 0.9, 0.2),
            "shape": "star",
            "pattern": "sharp",
            "position": (400, 450)
        },
        "bitter": {
            "color": (0.3, 0.2, 0.1),
            "shape": "angular",
            "pattern": "rough",
            "position": (600, 400)
        },
        "salty": {
            "color": (0.7, 0.8, 0.9),
            "shape": "crystal",
            "pattern": "granular",
            "position": (300, 200)
        },
        "umami": {
            "color": (0.8, 0.4, 0.2),
            "shape": "organic",
            "pattern": "layered",
            "position": (500, 200)
        }
    }
    
    # Draw each taste
    for taste, props in tastes.items():
        x, y = props["position"]
        
        with db.savedState():
            db.translate(x, y)
            
            if props["shape"] == "circle":
                # Sweet - soft circles
                for i in range(5):
                    size = 100 - i * 15
                    db.fill(*props["color"], 0.3)
                    db.oval(-size/2, -size/2, size, size)
            
            elif props["shape"] == "star":
                # Sour - sharp star
                db.fill(*props["color"])
                points = 8
                outer = 60
                inner = 20
                
                path = db.BezierPath()
                for i in range(points * 2):
                    angle = i * 360 / (points * 2)
                    if i % 2 == 0:
                        r = outer
                    else:
                        r = inner
                    px = math.cos(math.radians(angle)) * r
                    py = math.sin(math.radians(angle)) * r
                    
                    if i == 0:
                        path.moveTo((px, py))
                    else:
                        path.lineTo((px, py))
                path.closePath()
                db.drawPath(path)
            
            elif props["shape"] == "angular":
                # Bitter - harsh angles
                db.fill(*props["color"])
                for i in range(3):
                    db.rotate(random.randint(0, 360))
                    db.rect(-50, -10, 100, 20)
            
            elif props["shape"] == "crystal":
                # Salty - crystalline structure
                db.stroke(*props["color"])
                db.strokeWidth(2)
                db.fill(None)
                for angle in range(0, 360, 60):
                    db.rotate(angle)
                    db.line((0, 0), (40, 0))
                    db.rect(-5, 35, 10, 10)
                db.stroke(None)
            
            elif props["shape"] == "organic":
                # Umami - complex layers
                for i in range(4):
                    db.fill(*props["color"], 0.4 - i * 0.1)
                    
                    path = db.BezierPath()
                    points = []
                    for a in range(0, 360, 30):
                        r = 40 + random.uniform(-10, 20) + i * 10
                        px = math.cos(math.radians(a)) * r
                        py = math.sin(math.radians(a)) * r
                        points.append((px, py))
                    
                    path.moveTo(points[0])
                    for j in range(len(points)):
                        next_point = points[(j + 1) % len(points)]
                        cp1 = points[j]
                        cp2 = next_point
                        path.curveTo(cp1, cp2, next_point)
                    path.closePath()
                    db.drawPath(path)
        
        # Label
        db.fill(0.2)
        db.font("Helvetica")
        db.fontSize(14)
        db.text(taste, (x - 30, y - 80))

# Run examples (uncomment to execute)
# challenge_1_joy()
# challenge_2_example()
# challenge_3_jazz()
# challenge_4_tree()
# challenge_5_day_cycle()
# challenge_6_infinite_stairs()
# challenge_7_daily_rhythm()
# challenge_8_taste_palette()

# Save the output
db.saveImage("creative_challenges.pdf")
print("Creative challenges created! Pick one and make it your own.")

# ADDITIONAL CHALLENGES TO TRY:
# =============================
# 
# 9. Generative Portraits: Create faces using only mathematical functions
# 10. Movement Notation: Visualize dance or sports movements
# 11. Dream Logic: Design impossible but believable scenarios
# 12. Micro/Macro: Show the same subject at vastly different scales
# 13. Cultural Remix: Blend visual languages from different cultures
# 14. Future Artifacts: Design objects from 100 years in the future
# 15. Emotional Weather: Create weather systems based on moods
# 16. Digital Garden: Grow algorithmic plants that evolve
# 17. Memory Palace: Visualize how memories interconnect
# 18. Rhythm Patterns: Create visual polyrhythms and syncopation
#
# Remember: There's no "right" answer to these challenges.
# The goal is to explore, experiment, and express!
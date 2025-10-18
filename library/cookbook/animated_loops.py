"""
Animated Loops Cookbook
=======================
Create perfect loops for GIFs and videos.

Animation concepts:
- Frame-based animation
- Seamless loops
- Easing functions
- Motion patterns
- Morphing shapes
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

import math

# Animation settings
FRAMES = 60  # Total frames for one loop
WIDTH = 400
HEIGHT = 400
FPS = 30

# Easing functions for smooth animation
def ease_in_out_sine(t):
    """Smooth acceleration and deceleration"""
    return -(math.cos(math.pi * t) - 1) / 2

def ease_in_out_cubic(t):
    """Stronger acceleration/deceleration"""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2

def ease_in_out_elastic(t):
    """Elastic bounce effect"""
    c5 = (2 * math.pi) / 4.5
    
    if t == 0 or t == 1:
        return t
    elif t < 0.5:
        return -(pow(2, 20 * t - 10) * math.sin((20 * t - 11.125) * c5)) / 2
    else:
        return (pow(2, -20 * t + 10) * math.sin((20 * t - 11.125) * c5)) / 2 + 1

# ANIMATION 1: Rotating Square
print("Creating rotating square animation...")

for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background
    db.fill(0.1)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Calculate rotation
    t = frame / FRAMES  # 0 to 1
    rotation = t * 360  # Full rotation
    
    # Draw rotating square
    db.save()
    db.translate(WIDTH/2, HEIGHT/2)
    db.rotate(rotation)
    
    db.fill(1, 0.3, 0.3)
    size = 100
    db.rect(-size/2, -size/2, size, size)
    
    db.restore()

# Save as GIF
db.saveImage("output/rotating_square.gif")

# ANIMATION 2: Breathing Circle
print("Creating breathing circle animation...")

# Clear previous animation
for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background
    db.fill(0.95)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Calculate scale with easing
    t = frame / FRAMES
    # Use sine for smooth breathing
    scale = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
    
    # Draw circle
    db.fill(0.2, 0.6, 0.9)
    base_size = 150
    current_size = base_size * (0.5 + scale * 0.5)
    
    x = WIDTH/2 - current_size/2
    y = HEIGHT/2 - current_size/2
    db.oval(x, y, current_size, current_size)

db.saveImage("output/breathing_circle.gif")

# ANIMATION 3: Wave Pattern
print("Creating wave pattern animation...")

for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background
    db.fill(0)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Wave parameters
    wave_count = 5
    amplitude = 30
    t = frame / FRAMES
    
    db.stroke(1)
    db.strokeWidth(2)
    db.fill(None)
    
    # Draw multiple waves
    for i in range(wave_count):
        db.newPath()
        
        # Start position
        y_base = HEIGHT / (wave_count + 1) * (i + 1)
        db.moveTo((0, y_base))
        
        # Draw wave
        steps = 50
        for x in range(steps + 1):
            x_pos = x * WIDTH / steps
            # Phase shift for animation
            phase = t * 2 * math.pi + i * math.pi / wave_count
            y_pos = y_base + amplitude * math.sin(x * math.pi * 4 / steps + phase)
            db.lineTo((x_pos, y_pos))
        
        db.drawPath()
    
    db.stroke(None)

db.saveImage("output/wave_animation.gif")

# ANIMATION 4: Morphing Shapes
print("Creating morphing shapes animation...")

def lerp_point(p1, p2, t):
    """Linear interpolation between two points"""
    return (
        p1[0] + (p2[0] - p1[0]) * t,
        p1[1] + (p2[1] - p1[1]) * t
    )

# Define shape vertices
square_points = [
    (150, 150), (250, 150), (250, 250), (150, 250)
]

# Convert square to circle points
circle_points = []
for i in range(4):
    angle = i * math.pi / 2 + math.pi / 4  # 45° offset
    x = 200 + 70.7 * math.cos(angle)  # 70.7 ≈ 50√2
    y = 200 + 70.7 * math.sin(angle)
    circle_points.append((x, y))

for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background
    db.fill(0.15)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Calculate morph progress
    t = frame / FRAMES
    # Use easing for smooth morph
    morph_t = ease_in_out_sine(t)
    
    # Interpolate between shapes
    db.fill(0.9, 0.5, 0.2)
    db.newPath()
    
    for i in range(4):
        if t < 0.5:
            # Square to circle
            progress = morph_t * 2  # 0 to 1 in first half
            p1 = square_points[i]
            p2 = circle_points[i]
        else:
            # Circle back to square
            progress = (morph_t - 0.5) * 2  # 0 to 1 in second half
            p1 = circle_points[i]
            p2 = square_points[i]
        
        point = lerp_point(p1, p2, ease_in_out_cubic(progress))
        
        if i == 0:
            db.moveTo(point)
        else:
            db.lineTo(point)
    
    db.closePath()
    db.drawPath()

db.saveImage("output/morphing_shapes.gif")

# ANIMATION 5: Particle System
print("Creating particle system animation...")

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = (math.random() - 0.5) * 4
        self.vy = math.random() * 2 + 1
        self.life = 1.0
        self.decay = 0.02
        self.size = math.random() * 10 + 5
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= 0.1  # Gravity
        self.life -= self.decay
        
        # Wrap around horizontally
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
    
    def draw(self):
        if self.life > 0:
            db.fill(1, 0.7, 0.2, self.life)
            db.oval(self.x - self.size/2, self.y - self.size/2, 
                   self.size, self.size)

# Initialize particles
import random
random.seed(42)
particles = []

for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background with fade effect
    db.fill(0, 0, 0, 0.1)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Add new particles
    if frame % 2 == 0:
        particles.append(Particle(WIDTH/2 + random.randint(-50, 50), 50))
    
    # Update and draw particles
    for particle in particles[:]:
        particle.update()
        particle.draw()
        
        # Remove dead particles
        if particle.life <= 0 or particle.y < 0:
            particles.remove(particle)

db.saveImage("output/particle_system.gif")

# ANIMATION 6: Clock Animation
print("Creating clock animation...")

for frame in range(FRAMES):
    db.newPage(WIDTH, HEIGHT)
    
    # Background
    db.fill(0.9)
    db.rect(0, 0, WIDTH, HEIGHT)
    
    # Clock center
    cx, cy = WIDTH/2, HEIGHT/2
    radius = 150
    
    # Draw clock face
    db.fill(1)
    db.stroke(0)
    db.strokeWidth(3)
    db.oval(cx - radius, cy - radius, radius * 2, radius * 2)
    
    # Draw hour markers
    db.stroke(0)
    db.strokeWidth(2)
    for i in range(12):
        angle = i * math.pi * 2 / 12 - math.pi / 2
        x1 = cx + (radius - 20) * math.cos(angle)
        y1 = cy + (radius - 20) * math.sin(angle)
        x2 = cx + (radius - 10) * math.cos(angle)
        y2 = cy + (radius - 10) * math.sin(angle)
        db.line((x1, y1), (x2, y2))
    
    # Calculate hand positions
    t = frame / FRAMES
    
    # Hour hand (moves 1/12 of circle)
    hour_angle = t * math.pi * 2 / 12 - math.pi / 2
    hour_length = radius * 0.5
    hx = cx + hour_length * math.cos(hour_angle)
    hy = cy + hour_length * math.sin(hour_angle)
    
    db.strokeWidth(6)
    db.line((cx, cy), (hx, hy))
    
    # Minute hand (full rotation)
    minute_angle = t * math.pi * 2 - math.pi / 2
    minute_length = radius * 0.7
    mx = cx + minute_length * math.cos(minute_angle)
    my = cy + minute_length * math.sin(minute_angle)
    
    db.strokeWidth(4)
    db.line((cx, cy), (mx, my))
    
    # Second hand (smooth sweep)
    second_angle = t * math.pi * 2 * 2 - math.pi / 2  # 2 rotations
    second_length = radius * 0.8
    sx = cx + second_length * math.cos(second_angle)
    sy = cy + second_length * math.sin(second_angle)
    
    db.stroke(1, 0, 0)
    db.strokeWidth(2)
    db.line((cx, cy), (sx, sy))
    
    # Center dot
    db.fill(0)
    db.stroke(None)
    db.oval(cx - 5, cy - 5, 10, 10)

db.saveImage("output/clock_animation.gif")

print("All animations saved!")

# 🎯 ANIMATION EXERCISES:
# ----------------------
# 1. Create a loading spinner with multiple rotating elements
# 2. Animate text appearing letter by letter
# 3. Create a bouncing ball with realistic physics
# 4. Make a kaleidoscope pattern animation
# 5. Animate a logo reveal with multiple elements

# 💡 ANIMATION TIPS:
# ------------------
# - Always loop back to frame 0 for seamless loops
# - Use easing functions for natural motion
# - sin() and cos() are your friends for circular motion
# - Keep frame count reasonable for file size
# - Test with fewer frames first, then increase

# 🔍 ADVANCED TECHNIQUES:
# -----------------------
# - Use noise functions for organic motion
# - Implement spring physics for bouncy effects
# - Create motion blur by drawing multiple frames with transparency
# - Use color transitions for mood changes
# - Combine multiple simple animations for complex effects
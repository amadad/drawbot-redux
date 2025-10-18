# COLORED LAYOUT GUIDE - Zone-Based Design System
# Creates numbered, colored zones for systematic layout design

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
from drawBotGrid import Grid, ColumnGrid, RowGrid, BaselineGrid

# Document setup
page_width = 612  # US Letter width in points (8.5 inches)
page_height = 792  # US Letter height in points (11 inches)

# Grid setup
margins = (72, 72, 72, 72)  # 1 inch margins all around
baseline_unit = 8

# Typography
fonts = {
    'heading': 'SpaceGrotesk-Bold',
    'body': 'TASAOrbiterDeck-Regular',
    'body_bold': 'TASAOrbiterDeck-Bold',
}

sizes = {
    'large': 48,
    'small': 24,
    'body': 12,
    'caption': 11,
}

def setup_grids():
    """Create column and baseline grids"""
    columns = ColumnGrid.from_margins(margins, subdivisions=12, gutter=12)
    baseline = BaselineGrid.from_margins(margins, line_height=baseline_unit)
    return columns, baseline

# Color system for zones
zone_colors = {
    1: (0.85, 0.95, 1.0, 0.6),      # Light blue - Header/Title
    2: (0.85, 1.0, 0.85, 0.6),     # Light green - Navigation/Meta
    3: (1.0, 0.9, 0.8, 0.6),       # Light orange - Hero/Feature
    4: (0.95, 0.85, 1.0, 0.6),     # Light purple - Content Columns
    5: (1.0, 1.0, 0.8, 0.6),       # Light yellow - Sidebar
    6: (1.0, 0.85, 0.85, 0.6),     # Light red - Footer
}

zone_names = {
    1: "HEADER/TITLE",
    2: "NAVIGATION/META", 
    3: "HERO/FEATURE",
    4: "CONTENT COLUMNS",
    5: "SIDEBAR/SECONDARY",
    6: "FOOTER/CREDITS"
}

def draw_zone(zone_num, x, y, width, height, label=True):
    """Draw a colored zone with number and label"""
    # Fill zone with color
    db.fill(*zone_colors[zone_num])
    db.stroke(None)
    db.rect(x, y, width, height)
    
    # Add border
    db.fill(None)
    db.stroke(0.4, 0.4, 0.4)
    db.strokeWidth(1)
    db.rect(x, y, width, height)
    
    if label:
        # Add zone number (large)
        db.fill(0.2, 0.2, 0.2)
        db.stroke(None)
        db.font(fonts['heading'])
        db.fontSize(24)
        db.text(str(zone_num), (x + 10, y + height - 35))
        
        # Add zone name
        db.font(fonts['body_bold'])
        db.fontSize(10)
        db.text(zone_names[zone_num], (x + 10, y + height - 55))
        
        # Add dimensions
        db.font(fonts['body'])
        db.fontSize(8)
        db.fill(0.5, 0.5, 0.5)
        db.text(f"{width:.0f} × {height:.0f}pt", (x + 10, y + 10))

def draw_layout_pattern(pattern_name, zones_config):
    """Draw a complete layout pattern with multiple zones"""
    # Draw each zone in the configuration
    for zone_num, (x, y, width, height) in zones_config.items():
        draw_zone(zone_num, x, y, width, height)
    
    # Add pattern title
    db.fill(0, 0, 0)
    db.font(fonts['heading'])
    db.fontSize(16)
    db.text(pattern_name, (margins[3], page_height - margins[0] + 20))

# ============================================================================
# PAGE 1: LAYOUT PATTERN A - "REPORT LAYOUT"
# ============================================================================
columns, baseline = setup_grids()
db.newPage(page_width, page_height)

# White background
db.fill(1, 1, 1)
db.rect(0, 0, page_width, page_height)

# Calculate available space
content_width = page_width - margins[1] - margins[3]  # 468pt
content_height = page_height - margins[0] - margins[2]  # 648pt

# PATTERN A: Traditional Report Layout
pattern_a = {
    1: (margins[3], page_height - margins[0] - 80, content_width, 80),  # Header
    2: (margins[3], page_height - margins[0] - 120, content_width, 40),  # Meta
    3: (margins[3], page_height - margins[0] - 280, content_width, 160),  # Feature
    4: (margins[3], page_height - margins[0] - 520, content_width * 0.65, 240),  # Main content
    5: (margins[3] + content_width * 0.7, page_height - margins[0] - 520, content_width * 0.3, 240),  # Sidebar
    6: (margins[3], margins[2], content_width, 60),  # Footer
}

draw_layout_pattern("PATTERN A: REPORT LAYOUT", pattern_a)

# Draw underlying grid lightly
db.stroke(0.9, 0.9, 0.9, 0.3)
db.strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 2: LAYOUT PATTERN B - "MAGAZINE LAYOUT"  
# ============================================================================
db.newPage(page_width, page_height)
db.fill(1, 1, 1)
db.rect(0, 0, page_width, page_height)

# PATTERN B: Magazine/Editorial Layout
pattern_b = {
    1: (margins[3], page_height - margins[0] - 120, content_width * 0.6, 120),  # Header
    2: (margins[3] + content_width * 0.65, page_height - margins[0] - 60, content_width * 0.35, 60),  # Meta
    3: (margins[3], page_height - margins[0] - 380, content_width, 260),  # Hero feature
    4: (margins[3], page_height - margins[0] - 580, content_width * 0.48, 200),  # Content col 1
    4: (margins[3] + content_width * 0.52, page_height - margins[0] - 580, content_width * 0.48, 200),  # Content col 2
    6: (margins[3], margins[2], content_width, 40),  # Footer
}

draw_layout_pattern("PATTERN B: MAGAZINE LAYOUT", pattern_b)

# Draw underlying grid lightly
db.stroke(0.9, 0.9, 0.9, 0.3)
db.strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 3: LAYOUT PATTERN C - "DASHBOARD LAYOUT"
# ============================================================================
db.newPage(page_width, page_height)
db.fill(1, 1, 1)
db.rect(0, 0, page_width, page_height)

# PATTERN C: Dashboard/Data Layout
pattern_c = {
    1: (margins[3], page_height - margins[0] - 60, content_width, 60),  # Header bar
    2: (margins[3], page_height - margins[0] - 100, content_width * 0.7, 40),  # Navigation
    5: (margins[3] + content_width * 0.75, page_height - margins[0] - 400, content_width * 0.25, 300),  # Sidebar
    3: (margins[3], page_height - margins[0] - 240, content_width * 0.7, 140),  # Feature widget
    4: (margins[3], page_height - margins[0] - 400, content_width * 0.35, 160),  # Content block 1
    4: (margins[3] + content_width * 0.37, page_height - margins[0] - 400, content_width * 0.35, 160),  # Content block 2
    6: (margins[3], margins[2], content_width, 30),  # Footer
}

draw_layout_pattern("PATTERN C: DASHBOARD LAYOUT", pattern_c)

# Draw underlying grid lightly
db.stroke(0.9, 0.9, 0.9, 0.3)
db.strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 4: ZONE REFERENCE GUIDE
# ============================================================================
db.newPage(page_width, page_height)
db.fill(1, 1, 1)
db.rect(0, 0, page_width, page_height)

# Title
db.fill(0, 0, 0)
db.font(fonts['heading'])
db.fontSize(24)
db.text("ZONE REFERENCE GUIDE", (margins[3], page_height - margins[0] - 40))

# Zone legend with color swatches
legend_y = page_height - margins[0] - 100
legend_x = margins[3]

for zone_num, color in zone_colors.items():
    # Color swatch
    db.fill(*color)
    db.stroke(0.4, 0.4, 0.4)
    db.strokeWidth(1)
    db.rect(legend_x, legend_y, 40, 30)
    
    # Zone number
    db.fill(0, 0, 0)
    db.stroke(None)
    db.font(fonts['heading'])
    db.fontSize(18)
    db.text(str(zone_num), (legend_x + 15, legend_y + 8))
    
    # Zone name and description
    db.font(fonts['body_bold'])
    db.fontSize(12)
    db.text(zone_names[zone_num], (legend_x + 50, legend_y + 20))
    
    # Usage description
    db.font(fonts['body'])
    db.fontSize(10)
    descriptions = {
        1: "Page titles, branding, main headers",
        2: "Navigation, metadata, secondary info", 
        3: "Hero content, featured items, key messages",
        4: "Main text content, articles, descriptions",
        5: "Supporting content, sidebars, related info",
        6: "Footer info, credits, page numbers"
    }
    db.text(descriptions[zone_num], (legend_x + 50, legend_y + 5))
    
    legend_y -= 50

# Grid specifications
spec_y = legend_y - 60
db.font(fonts['heading'])
db.fontSize(14)
db.fill(0, 0, 0)
db.text("GRID SPECIFICATIONS", (margins[3], spec_y))

spec_y -= 30
db.font(fonts['body'])
db.fontSize(11)
specs = [
    f"Page Size: {page_width} × {page_height} points (US Letter)",
    f"Margins: {margins[0]}pt all around (1 inch)",
    f"Content Area: {content_width} × {content_height} points", 
    f"Column Grid: 12 columns with 12pt gutters",
    f"Baseline Grid: {baseline_unit}pt intervals",
    f"Typography: Based on Hochuli principles"
]

for spec in specs:
    db.text(spec, (margins[3], spec_y))
    spec_y -= 20

# Save output
db.saveImage("output/grid_layout_guide.pdf")
print("Colored layout guide generated: output/grid_layout_guide.pdf")
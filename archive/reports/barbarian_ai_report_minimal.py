# Barbarian Monthly AI Intelligence Brief - Minimal Modern Design
# Clean, professional report design with excellent readability

import drawBot as db
import math

# Document setup
page_width = 816  # US Letter width in points
page_height = 1056  # US Letter height in points
margin = 72
small_margin = 36
gutter = 24

# Color palette - minimal and modern
colors = {
    'black': (0, 0, 0),
    'white': (1, 1, 1),
    'accent': (0, 0.4, 1),  # Modern blue
    'light_gray': (0.95, 0.95, 0.95),
    'medium_gray': (0.7, 0.7, 0.7),
    'dark_gray': (0.3, 0.3, 0.3)
}

# Typography settings
fonts = {
    'heading': 'Helvetica-Bold',
    'subheading': 'Helvetica',
    'body': 'Helvetica',
    'body_bold': 'Helvetica-Bold'
}

# Helper functions
def draw_divider(y, width=None):
    """Draw a subtle divider line"""
    if width is None:
        width = page_width - 2 * margin
    db.stroke(*colors['medium_gray'])
    db.strokeWidth(0.5)
    db.line((margin, y), (margin + width, y))

def draw_accent_block(x, y, width, height):
    """Draw an accent color block"""
    db.fill(*colors['accent'])
    db.rect(x, y, width, height)

def draw_stat_card(x, y, label, value, width=150):
    """Draw a minimal stat card"""
    # Background
    db.fill(*colors['light_gray'])
    db.rect(x, y, width, 80)
    
    # Value
    db.fill(*colors['black'])
    db.font(fonts['heading'])
    db.fontSize(28)
    db.text(value, (x + 20, y + 45))
    
    # Label
    db.font(fonts['body'])
    db.fontSize(12)
    db.fill(*colors['dark_gray'])
    db.text(label, (x + 20, y + 20))

# PAGE 1: TITLE PAGE
db.newPage(page_width, page_height)

# White background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Accent line at top
draw_accent_block(0, page_height - 8, page_width, 8)

# The Barbarian Group - small, top
db.font(fonts['body'])
db.fontSize(14)
db.fill(*colors['dark_gray'])
db.text("THE BARBARIAN GROUP", (margin, page_height - 120))

# Main title
db.font(fonts['heading'])
db.fontSize(72)
db.fill(*colors['black'])
db.text("AI News", (margin, page_height - 200))

# Subtitle
db.fontSize(48)
db.fill(*colors['accent'])
db.text("July 2025", (margin, page_height - 270))

# Report type
db.font(fonts['body'])
db.fontSize(18)
db.fill(*colors['dark_gray'])
db.text("Monthly Intelligence Brief", (margin, page_height - 320))

# Date
db.fontSize(14)
db.text("Report Generated: July 26, 2025", (margin, page_height - 360))

# Bottom accent
draw_divider(margin + 50)

# Geometric element - minimal circles
for i in range(3):
    db.fill(*colors['accent'], 0.1 + i * 0.1)
    db.oval(page_width - 200 + i * 30, 200 + i * 30, 100 - i * 20, 100 - i * 20)

# PAGE 2: EXECUTIVE SUMMARY
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Executive Summary", (margin, page_height - 120))

# Divider
draw_divider(page_height - 140)

# Key insight
db.font(fonts['body'])
db.fontSize(18)
db.fill(*colors['dark_gray'])
db.textBox("The AI landscape has fundamentally shifted from conversational assistants to autonomous agents capable of completing complex tasks independently.",
          (margin, page_height - 220, page_width - 2 * margin, 100))

# Key developments
y_pos = page_height - 320
developments = [
    ("Manus AI", "Game-changer with $2/task autonomous agents"),
    ("Midjourney", "Launches video capabilities at $10/month"),
    ("Abacus.AI", "Positions as enterprise 'AI Brain' with DeepAgent"),
    ("Content Shift", "Move toward authentic, less polished content")
]

for title, desc in developments:
    # Bullet point
    db.fill(*colors['accent'])
    db.oval(margin, y_pos + 6, 8, 8)
    
    # Title
    db.font(fonts['body_bold'])
    db.fontSize(16)
    db.fill(*colors['black'])
    db.text(title, (margin + 20, y_pos))
    
    # Description
    db.font(fonts['body'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(desc, (margin + 20, y_pos - 20))
    
    y_pos -= 60

# Stats cards
stat_y = 200
stats = [
    ("X Posts Analyzed", "40+"),
    ("News Sources", "20+"),
    ("Cost Reduction", "90%"),
    ("ROI", "1000%+")
]

for i, (label, value) in enumerate(stats):
    stat_x = margin + (i % 2) * 300
    stat_y_pos = stat_y - (i // 2) * 100
    draw_stat_card(stat_x, stat_y_pos, label, value)

# PAGE 3: AI TWITTER/X RECAP
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("AI Twitter/X Recap", (margin, page_height - 120))

# Subtitle
db.font(fonts['body'])
db.fontSize(16)
db.fill(*colors['dark_gray'])
db.text("Agent Platforms & Video Generation", (margin, page_height - 150))

draw_divider(page_height - 170)

# Platform cards
platforms = [
    {
        "name": "Manus AI",
        "tag": "GAME CHANGER",
        "points": [
            "Chinese startup with autonomous AI agents",
            "~$2 per task (90% cheaper)",
            "$75M raised, expanding globally",
            "Analyzes resumes, builds websites autonomously"
        ]
    },
    {
        "name": "Abacus.AI DeepAgent",
        "tag": "ENTERPRISE",
        "points": [
            "AI Brain for organizations",
            "Creates apps, videos, presentations",
            "Focus: marketing, tech support, sales",
            "Automated campaign asset generation"
        ]
    },
    {
        "name": "ChatGPT Evolution",
        "tag": "SHIFT",
        "points": [
            "OpenAI retired GPT-4",
            "Moving to reasoning-based tools",
            "DeepResearch for autonomous research",
            "Conversational AI now table stakes"
        ]
    }
]

y_pos = page_height - 220
for platform in platforms:
    # Platform name
    db.font(fonts['heading'])
    db.fontSize(24)
    db.fill(*colors['black'])
    db.text(platform["name"], (margin, y_pos))
    
    # Tag
    db.font(fonts['body'])
    db.fontSize(12)
    db.fill(*colors['white'])
    # Tag background
    tag_width = db.textSize(platform["tag"])[0] + 16
    db.fill(*colors['accent'])
    db.rect(margin + db.textSize(platform["name"])[0] + 20, y_pos, tag_width, 20)
    db.fill(*colors['white'])
    db.text(platform["tag"], (margin + db.textSize(platform["name"])[0] + 28, y_pos + 4))
    
    # Points
    y_pos -= 35
    for point in platform["points"]:
        db.font(fonts['body'])
        db.fontSize(13)
        db.fill(*colors['dark_gray'])
        db.text(f"• {point}", (margin + 20, y_pos))
        y_pos -= 20
    
    y_pos -= 20

# PAGE 4: VIDEO REVOLUTION
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Creative AI: Video Revolution", (margin, page_height - 120))

draw_divider(page_height - 140)

# Midjourney section
db.font(fonts['heading'])
db.fontSize(28)
db.fill(*colors['accent'])
db.text("Midjourney V7 + Video", (margin, page_height - 200))

# Features grid
features = [
    ("Duration", "5-21 seconds"),
    ("Cost", "~8x image generation"),
    ("Quality", "Cinema-grade"),
    ("Capability", "NeRF-like 3D")
]

feature_y = page_height - 250
for i, (label, value) in enumerate(features):
    x = margin + (i % 2) * 300
    y = feature_y - (i // 2) * 60
    
    db.font(fonts['body_bold'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(label, (x, y))
    
    db.font(fonts['body'])
    db.fontSize(18)
    db.fill(*colors['black'])
    db.text(value, (x, y - 25))

# Production capabilities
db.font(fonts['body_bold'])
db.fontSize(16)
db.fill(*colors['black'])
db.text("Production Capabilities", (margin, page_height - 380))

capabilities = [
    "• Image-to-Video animation",
    "• 60-second videos from 6 images (~3 hours)",
    "• Future: Real-time generation, 3D renderings",
    "• Rapid prototyping for agency pitches"
]

y_pos = page_height - 410
for cap in capabilities:
    db.font(fonts['body'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(cap, (margin, y_pos))
    y_pos -= 25

# Legal alert box
alert_y = 250
db.fill(*colors['accent'], 0.1)
db.rect(margin, alert_y, page_width - 2 * margin, 80)

db.font(fonts['body_bold'])
db.fontSize(16)
db.fill(*colors['accent'])
db.text("⚠️ LEGAL ALERT", (margin + 20, alert_y + 50))

db.font(fonts['body'])
db.fontSize(14)
db.fill(*colors['dark_gray'])
db.text("Disney/Universal lawsuit against Midjourney - agencies need clear usage policies", 
        (margin + 20, alert_y + 25))

# PAGE 5: MARKET SIGNALS & TRENDS
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Market Signals & Trends", (margin, page_height - 120))

draw_divider(page_height - 140)

# Three trend columns
trends = [
    {
        "title": "Authenticity Movement",
        "points": [
            "Over-produced content losing engagement",
            "Natural, conversational style winning",
            "Less polish, more personality"
        ]
    },
    {
        "title": "China's AI Dominance",
        "points": [
            "Manus, DeepSeek: 10x cost advantages",
            "Focus on practical applications",
            "Partner for price-sensitive projects"
        ]
    },
    {
        "title": "Enterprise Adoption",
        "points": [
            "Autonomous agents in HR, dev, CS",
            "ROI clear: 90% cost reduction",
            "'AI employees' not 'AI tools'"
        ]
    }
]

col_width = (page_width - 2 * margin - 2 * gutter) / 3
for i, trend in enumerate(trends):
    x = margin + i * (col_width + gutter)
    
    # Column header
    db.font(fonts['heading'])
    db.fontSize(20)
    db.fill(*colors['black'])
    db.text(trend["title"], (x, page_height - 200))
    
    # Accent line
    db.fill(*colors['accent'])
    db.rect(x, page_height - 210, 60, 3)
    
    # Points
    y_pos = page_height - 250
    for point in trend["points"]:
        db.font(fonts['body'])
        db.fontSize(13)
        db.fill(*colors['dark_gray'])
        db.textBox(point, (x, y_pos - 50, col_width, 50))
        y_pos -= 60

# Strategy shift callout
callout_y = 300
db.fill(*colors['light_gray'])
db.rect(margin, callout_y, page_width - 2 * margin, 100)

db.font(fonts['body_bold'])
db.fontSize(18)
db.fill(*colors['accent'])
db.text("STRATEGY SHIFT", (margin + 30, callout_y + 65))

db.font(fonts['body'])
db.fontSize(16)
db.fill(*colors['black'])
db.text("From polished perfection to authentic connection", (margin + 30, callout_y + 35))

# PAGE 6: SOCIAL PLATFORMS OVERVIEW
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Social Platform Insights", (margin, page_height - 120))

draw_divider(page_height - 140)

# Platform sections
platforms = [
    {
        "name": "LinkedIn",
        "focus": "Professional Insights",
        "key": "Agency case studies showing real ROI"
    },
    {
        "name": "TikTok",
        "focus": "Viral AI Trends",
        "key": "AI-generated content going mainstream"
    },
    {
        "name": "Instagram",
        "focus": "AI Art Showcases",
        "key": "Visual storytelling with AI tools"
    },
    {
        "name": "Reddit",
        "focus": "Deep Technical Dive",
        "key": "Developer insights and warnings"
    }
]

y_pos = page_height - 200
for platform in platforms:
    # Platform name with accent
    db.font(fonts['heading'])
    db.fontSize(24)
    db.fill(*colors['accent'])
    db.text(platform["name"], (margin, y_pos))
    
    # Focus area
    db.font(fonts['body_bold'])
    db.fontSize(16)
    db.fill(*colors['black'])
    db.text(platform["focus"], (margin + 150, y_pos))
    
    # Key insight
    db.font(fonts['body'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(platform["key"], (margin + 20, y_pos - 25))
    
    y_pos -= 80

# PAGE 7: ACTION ITEMS
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Action Items for The Barbarian Group", (margin, page_height - 120))

draw_divider(page_height - 140)

# Timeline sections
timelines = [
    {
        "title": "Immediate (This Week)",
        "color": colors['accent'],
        "items": [
            "Create Midjourney video workflow for creative team",
            "Develop AI agent pricing model for clients",
            "Update pitch decks with autonomous agent capabilities"
        ]
    },
    {
        "title": "Short-term (This Month)",
        "color": colors['dark_gray'],
        "items": [
            "Run pilot project with Abacus.AI",
            "Develop AI copyright guidelines",
            "Create 'authentic content' creative brief template"
        ]
    },
    {
        "title": "Strategic (Q3 2025)",
        "color": colors['medium_gray'],
        "items": [
            "Position as 'AI-First Creative Agency'",
            "Build partnerships with AI agent platforms",
            "Develop proprietary AI workflow IP"
        ]
    }
]

y_pos = page_height - 200
for timeline in timelines:
    # Section header with color coding
    db.font(fonts['heading'])
    db.fontSize(20)
    db.fill(*timeline["color"])
    db.text(timeline["title"], (margin, y_pos))
    
    y_pos -= 35
    
    # Checklist items
    for item in timeline["items"]:
        # Checkbox
        db.stroke(*timeline["color"])
        db.strokeWidth(2)
        db.fill(None)
        db.rect(margin + 20, y_pos - 12, 12, 12)
        
        # Item text
        db.font(fonts['body'])
        db.fontSize(14)
        db.fill(*colors['dark_gray'])
        db.text(item, (margin + 40, y_pos - 10))
        
        y_pos -= 30
    
    y_pos -= 20

# PAGE 8: TOOLS TO TEST & COST ANALYSIS
db.newPage(page_width, page_height)

# Background
db.fill(*colors['white'])
db.rect(0, 0, page_width, page_height)

# Header
db.font(fonts['heading'])
db.fontSize(36)
db.fill(*colors['black'])
db.text("Tools to Test", (margin, page_height - 120))

draw_divider(page_height - 140)

# Tools list
tools = [
    {
        "name": "Midjourney V7",
        "action": "Set up team account for video prototyping",
        "priority": "HIGH"
    },
    {
        "name": "Abacus.AI Trial",
        "action": "Test DeepAgent for campaign automation",
        "priority": "HIGH"
    },
    {
        "name": "Manus Waitlist",
        "action": "Join for early access to $2 task automation",
        "priority": "MEDIUM"
    }
]

y_pos = page_height - 200
for i, tool in enumerate(tools, 1):
    # Number circle
    db.fill(*colors['accent'])
    db.oval(margin, y_pos - 15, 30, 30)
    db.fill(*colors['white'])
    db.font(fonts['heading'])
    db.fontSize(18)
    db.text(str(i), (margin + 10, y_pos - 10))
    
    # Tool name
    db.font(fonts['heading'])
    db.fontSize(18)
    db.fill(*colors['black'])
    db.text(tool["name"], (margin + 50, y_pos))
    
    # Priority tag
    if tool["priority"] == "HIGH":
        tag_color = colors['accent']
    else:
        tag_color = colors['medium_gray']
    
    db.font(fonts['body'])
    db.fontSize(12)
    db.fill(*tag_color)
    db.text(tool["priority"], (margin + 250, y_pos))
    
    # Action
    db.font(fonts['body'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(tool["action"], (margin + 50, y_pos - 20))
    
    y_pos -= 70

# Cost Analysis section
db.font(fonts['heading'])
db.fontSize(28)
db.fill(*colors['black'])
db.text("Intelligence Gathering Cost Analysis", (margin, page_height - 500))

draw_divider(page_height - 520)

# Cost breakdown
cost_y = page_height - 570
costs = [
    ("API Calls Used", "5"),
    ("Estimated Cost", "~$0.50"),
    ("Time Saved", "4-6 hours"),
    ("ROI", "1000%+")
]

for label, value in costs:
    db.font(fonts['body'])
    db.fontSize(14)
    db.fill(*colors['dark_gray'])
    db.text(label, (margin, cost_y))
    
    db.font(fonts['heading'])
    db.fontSize(18)
    db.fill(*colors['black'])
    db.text(value, (margin + 200, cost_y))
    
    cost_y -= 30

# Footer
db.font(fonts['body'])
db.fontSize(12)
db.fill(*colors['medium_gray'])
db.textBox("Prepared using AI Intelligence gathering tools. For questions or deep dives on any topic, contact your innovation team.",
          (margin, 80, page_width - 2 * margin, 50))

# Bottom accent line
draw_accent_block(0, 0, page_width, 8)

# Save the PDF
output_path = "/Users/amadad/Projects/drawbot-redux/output/barbarian_ai_report_minimal.pdf"
db.saveImage(output_path)
print(f"Minimal modern PDF report generated: {output_path}")
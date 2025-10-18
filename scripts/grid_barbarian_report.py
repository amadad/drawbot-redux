# BARBARIAN AI INTELLIGENCE REPORT LAYOUTS
# Based on the July 2025 AI Intelligence Report content
# Each page follows a different layout pattern inspired by the report structure

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from drawBot import *
print("Using drawbot-skia for headless rendering")

try:
    from drawBotGrid import Grid, ColumnGrid, RowGrid, BaselineGrid
except ImportError:
    print("DrawBotGrid not available, using basic grid functionality")
    # Create basic grid classes as fallback
    class ColumnGrid:
        @classmethod
        def from_margins(cls, margins, subdivisions=12, gutter=12):
            return cls()
        def draw(self):
            pass
    
    class BaselineGrid:
        @classmethod
        def from_margins(cls, margins, line_height=8):
            return cls()
        def draw(self):
            pass

# Document setup
page_width = 612  # US Letter width in points (8.5 inches)
page_height = 792  # US Letter height in points (11 inches)

# Grid setup with margins
margins = (72, 72, 72, 72)  # 1 inch margins all around (top, right, bottom, left)
baseline_unit = 8

# Typography
fonts = {
    'heading': 'SpaceGrotesk-Bold',
    'body': 'TASAOrbiterDeck-Regular',
    'body_bold': 'TASAOrbiterDeck-Bold',
}

sizes = {
    'large': 48,
    'medium': 36,
    'small': 24,
    'body': 12,
    'caption': 11,
}

def setup_grids():
    """Create column and baseline grids"""
    columns = ColumnGrid.from_margins(margins, subdivisions=12, gutter=12)
    baseline = BaselineGrid.from_margins(margins, line_height=baseline_unit)
    return columns, baseline

# Color system for content zones
zone_colors = {
    1: (0.85, 0.95, 1.0, 0.6),      # Light blue - Headers/Titles
    2: (0.85, 1.0, 0.85, 0.6),     # Light green - Meta info/Navigation
    3: (1.0, 0.9, 0.8, 0.6),       # Light orange - Hero/Feature content
    4: (0.95, 0.85, 1.0, 0.6),     # Light purple - Main content
    5: (1.0, 1.0, 0.8, 0.6),       # Light yellow - Sidebar/Secondary
    6: (1.0, 0.85, 0.85, 0.6),     # Light red - Footer/Actions
}

zone_names = {
    1: "HEADER/TITLE",
    2: "META/NAVIGATION", 
    3: "HERO/FEATURE",
    4: "CONTENT",
    5: "SIDEBAR",
    6: "FOOTER/ACTIONS"
}

def draw_zone(zone_num, x, y, width, height, label=True, content_text=""):
    """Draw a colored zone with number, label, and content preview"""
    # Fill zone with color
    fill(*zone_colors[zone_num])
    stroke(None)
    rect(x, y, width, height)
    
    # Add border
    fill(None)
    stroke(0.4, 0.4, 0.4)
    strokeWidth(1)
    rect(x, y, width, height)
    
    if label:
        # Add zone number (large)
        fill(0.2, 0.2, 0.2)
        stroke(None)
        font(fonts['heading'])
        fontSize(18)
        text(str(zone_num), (x + 10, y + height - 25))
        
        # Add zone name
        font(fonts['body_bold'])
        fontSize(9)
        text(zone_names[zone_num], (x + 10, y + height - 40))
        
        # Add content preview
        if content_text:
            font(fonts['body'])
            fontSize(8)
            fill(0.3, 0.3, 0.3)
            # Wrap text within zone bounds
            text_width = width - 20
            lines = []
            words = content_text.split()
            current_line = ""
            
            for word in words:
                test_line = current_line + " " + word if current_line else word
                if textSize(test_line)[0] < text_width:
                    current_line = test_line
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word
                    
            if current_line:
                lines.append(current_line)
            
            # Draw wrapped text
            text_y = y + height - 55
            for i, line in enumerate(lines[:3]):  # Max 3 lines
                if text_y > y + 10:
                    text(line, (x + 10, text_y))
                    text_y -= 12
        
        # Add dimensions
        font(fonts['body'])
        fontSize(7)
        fill(0.6, 0.6, 0.6)
        text(f"{width:.0f} × {height:.0f}pt", (x + 10, y + 5))

def draw_layout_pattern(pattern_name, zones_config, page_subtitle=""):
    """Draw a complete layout pattern with multiple zones"""
    # Draw each zone in the configuration
    for zone_data in zones_config:
        zone_num, x, y, width, height, content = zone_data
        draw_zone(zone_num, x, y, width, height, True, content)
    
    # Add pattern title
    fill(0, 0, 0)
    font(fonts['heading'])
    fontSize(16)
    text(pattern_name, (margins[3], page_height - margins[0] + 20))
    
    # Add subtitle if provided
    if page_subtitle:
        font(fonts['body'])
        fontSize(12)
        fill(0.4, 0.4, 0.4)
        text(page_subtitle, (margins[3], page_height - margins[0] + 5))

# Calculate available content space
content_width = page_width - margins[1] - margins[3]  # 468pt
content_height = page_height - margins[0] - margins[2]  # 648pt

# ============================================================================
# PAGE 1: AI AGENT PLATFORMS - News Article Layout
# ============================================================================
columns, baseline = setup_grids()
newPage(page_width, page_height)

# White background
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# PAGE 1: News Article Layout for AI Agent Platforms
pattern_1 = [
    # Zone, X, Y, Width, Height, Content
    (1, margins[3], page_height - margins[0] - 60, content_width, 60, "AI News for July 2025 - The Barbarian Group"),
    (2, margins[3], page_height - margins[0] - 90, content_width, 30, "Date: July 29, 2025 | Research cost: $0.40 | 845 minutes saved"),
    (3, margins[3], page_height - margins[0] - 200, content_width, 110, "🚀 AI Twitter/X Recap - Major Agent Platform Releases"),
    (4, margins[3], page_height - margins[0] - 350, content_width * 0.6, 150, "OpenAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor..."),
    (5, margins[3] + content_width * 0.65, page_height - margins[0] - 350, content_width * 0.35, 150, "The Manus AI 'ChatGPT Killer' Narrative: Beta testers are going wild for Manus AI, calling it the 'first general AI agent.'"),
    (6, margins[3], margins[2], content_width, 40, "Action Items: Try Midjourney V1 Video ($10/month) • Test ChatGPT Agent Mode"),
]

draw_layout_pattern("PAGE 1: AI AGENT PLATFORMS - NEWS LAYOUT", pattern_1, "Major releases and market disruption")

# Draw underlying grid lightly
stroke(0.9, 0.9, 0.9, 0.3)
strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 2: VIDEO GENERATION - Magazine Feature Layout
# ============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# PAGE 2: Magazine Feature Layout for Video Generation
pattern_2 = [
    (1, margins[3], page_height - margins[0] - 80, content_width * 0.7, 80, "The Video Generation Revolution"),
    (2, margins[3] + content_width * 0.72, page_height - margins[0] - 50, content_width * 0.28, 50, "July 2025 Update"),
    (3, margins[3], page_height - margins[0] - 260, content_width, 180, "Midjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, brings AI video to the masses at $10/month with seamless looping, frame control, and Discord integration."),
    (4, margins[3], page_height - margins[0] - 420, content_width * 0.48, 160, "July updates include: • Seamless looping with --loop command • Start/end frame control • Direct Discord integration • 720p resolution 'coming soon'"),
    (4, margins[3] + content_width * 0.52, page_height - margins[0] - 420, content_width * 0.48, 160, "Runway Maintains Pro Workflow Leadership: While Midjourney democratizes, Runway focuses on professional features—longer clips, better motion consistency."),
    (6, margins[3], margins[2], content_width, 35, "The Pattern: Midjourney for ideation → Runway for refinement"),
]

draw_layout_pattern("PAGE 2: VIDEO GENERATION - MAGAZINE LAYOUT", pattern_2, "Democratization meets professional workflow")

# Draw underlying grid lightly
stroke(0.9, 0.9, 0.9, 0.3)
strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 3: SOCIAL MEDIA TRENDS - Dashboard Layout
# ============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# PAGE 3: Dashboard Layout for Social Media Trends
pattern_3 = [
    (1, margins[3], page_height - margins[0] - 50, content_width, 50, "🎵 TikTok & 📸 Instagram AI Trends Dashboard"),
    (2, margins[3], page_height - margins[0] - 85, content_width * 0.7, 35, "July 2025 Viral Content Analysis"),
    (5, margins[3] + content_width * 0.72, page_height - margins[0] - 280, content_width * 0.28, 195, "Top Creators: @AIArtWizard @ChatbotComedy @DeepfakeDaily @AIMusicMashup"),
    (3, margins[3], page_height - margins[0] - 200, content_width * 0.7, 115, "The 'AI Gold Rush' Phenomenon: Natural disaster clips generated by AI hitting 100M+ views. 10x engagement when mixing AI with personal storytelling."),
    (4, margins[3], page_height - margins[0] - 340, content_width * 0.35, 140, "TikTok Integration: Over 4 million TikTok Shop sellers leverage AI for 'shoppertainment' content. Key trend: AI voiceovers + trending sounds = viral discovery."),
    (4, margins[3] + content_width * 0.37, page_height - margins[0] - 340, content_width * 0.33, 140, "Instagram Showcase: Creative agencies like Wieden+Kennedy sharing AI-integrated projects. Midjourney V1 pilots for quick prototyping."),
    (6, margins[3], margins[2], content_width, 30, "Trending: #MidjourneyV1 #AIVideoArt #MidjourneyVideo"),
]

draw_layout_pattern("PAGE 3: SOCIAL MEDIA TRENDS - DASHBOARD LAYOUT", pattern_3, "Viral content and platform integration")

# Draw underlying grid lightly
stroke(0.9, 0.9, 0.9, 0.3)
strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 4: PROFESSIONAL INSIGHTS - Report Layout
# ============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# PAGE 4: Report Layout for Professional Insights
pattern_4 = [
    (1, margins[3], page_height - margins[0] - 70, content_width, 70, "🔗 LinkedIn Professional Insights & 🤖 Reddit Deep Dive"),
    (2, margins[3], page_height - margins[0] - 100, content_width, 30, "Enterprise adoption and authentic user feedback"),
    (3, margins[3], page_height - margins[0] - 200, content_width, 100, "Agency Transformation Numbers: 35% ROI increase in competitive analysis • 30% faster hiring cycles • 25% uplift in client engagement • 2x efficiency in lead qualification"),
    (4, margins[3], page_height - margins[0] - 380, content_width * 0.65, 180, "Reddit's Unfiltered Truth: Mixed reactions to Manus AI vs ChatGPT. Users praise Manus for 'feeling like having a junior assistant' in research. ChatGPT still wins for creative writing, Manus excels in 'agentic' tasks."),
    (5, margins[3] + content_width * 0.67, page_height - margins[0] - 380, content_width * 0.33, 180, "Platform Scores: • Manus AI: 4-5/5 innovation • ChatGPT: 4.5/5 accessibility • Midjourney V1: Revolutionary but early"),
    (6, margins[3], margins[2], content_width, 50, "Professional Verdict: Use agents for 80% automation, human oversight for final 20%"),
]

draw_layout_pattern("PAGE 4: PROFESSIONAL INSIGHTS - REPORT LAYOUT", pattern_4, "Enterprise reality vs. consumer hype")

# Draw underlying grid lightly
stroke(0.9, 0.9, 0.9, 0.3)
strokeWidth(0.25)
columns.draw()

# ============================================================================
# PAGE 5: LAYOUT REFERENCE GUIDE
# ============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Title
fill(0, 0, 0)
font(fonts['heading'])
fontSize(24)
text("BARBARIAN AI REPORT LAYOUT GUIDE", (margins[3], page_height - margins[0] - 40))

# Zone legend with color swatches
legend_y = page_height - margins[0] - 100
legend_x = margins[3]

for zone_num, color in zone_colors.items():
    # Color swatch
    fill(*color)
    stroke(0.4, 0.4, 0.4)
    strokeWidth(1)
    rect(legend_x, legend_y, 40, 30)
    
    # Zone number
    fill(0, 0, 0)
    stroke(None)
    font(fonts['heading'])
    fontSize(18)
    text(str(zone_num), (legend_x + 15, legend_y + 8))
    
    # Zone name and description
    font(fonts['body_bold'])
    fontSize(12)
    text(zone_names[zone_num], (legend_x + 50, legend_y + 20))
    
    # Usage description for report layouts
    font(fonts['body'])
    fontSize(10)
    descriptions = {
        1: "Report titles, publication info, main headers",
        2: "Metadata, publication dates, source attribution", 
        3: "Featured stories, key findings, hero content",
        4: "Main article content, analysis, case studies",
        5: "Supporting data, related insights, sidebars",
        6: "Action items, next steps, footer information"
    }
    text(descriptions[zone_num], (legend_x + 50, legend_y + 5))
    
    legend_y -= 50

# Layout specifications
spec_y = legend_y - 60
font(fonts['heading'])
fontSize(14)
fill(0, 0, 0)
text("LAYOUT SPECIFICATIONS", (margins[3], spec_y))

spec_y -= 30
font(fonts['body'])
fontSize(11)
specs = [
    f"Page Size: {page_width} × {page_height} points (US Letter)",
    f"Margins: {margins[0]}pt all around (1 inch)",
    f"Content Area: {content_width} × {content_height} points", 
    f"Column Grid: 12 columns with 12pt gutters",
    f"Baseline Grid: {baseline_unit}pt intervals",
    f"Content Source: Barbarian AI Intelligence Report July 2025"
]

for spec in specs:
    text(spec, (margins[3], spec_y))
    spec_y -= 20

# Layout pattern summary
pattern_y = spec_y - 40
font(fonts['heading'])
fontSize(14)
fill(0, 0, 0)
text("LAYOUT PATTERNS USED", (margins[3], pattern_y))

pattern_y -= 30
font(fonts['body'])
fontSize(11)
patterns = [
    "Page 1: News Article Layout - Header, meta, feature, two-column content",
    "Page 2: Magazine Feature Layout - Asymmetric header, hero content, balanced columns",
    "Page 3: Dashboard Layout - Header bar, sidebar, content blocks, trending footer",
    "Page 4: Report Layout - Title, meta, key findings, detailed analysis, summary"
]

for pattern in patterns:
    text(pattern, (margins[3], pattern_y))
    pattern_y -= 20

# Save output
saveImage("output/barbarian_ai_report_layouts.pdf")
print("Barbarian AI report layouts generated: output/barbarian_ai_report_layouts.pdf")
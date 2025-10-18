# BARBARIAN AI INTELLIGENCE REPORT - ENHANCED EDITORIAL TYPOGRAPHY
# Simplified version with working typography enhancements

import sys
import os
import re

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from drawBot import *
print("Creating enhanced editorial typography")

# Document setup
page_width = 612
page_height = 792
margins = (54, 54, 54, 54)
content_width = page_width - margins[1] - margins[3]
content_height = page_height - margins[0] - margins[2]

# Enhanced Typography System
fonts = {
    'display': 'SpaceGrotesk-Bold',
    'headline': 'SpaceGrotesk-Bold',
    'subhead': 'SpaceGrotesk-Medium',
    'kicker': 'SpaceGrotesk-Regular',
    'body': 'TASAOrbiterDeck-Regular',
    'body_bold': 'TASAOrbiterDeck-Bold',
    'body_italic': 'TASAOrbiterDeck-Italic',
    'pullquote': 'SpaceGrotesk-Medium',
    'social_handle': 'SpaceGrotesk-Regular',
    'small_caps': 'TASAOrbiterDeck-Bold',
}

sizes = {
    'display': 36,
    'headline': 22,
    'subhead': 16,
    'kicker': 10,
    'body': 11,
    'pullquote': 18,
    'social': 10,
    'small_caps': 9,
}

leading = {
    'display': 40,
    'headline': 26,
    'subhead': 19,
    'kicker': 13,
    'body': 15,
    'pullquote': 22,
    'social': 13,
    'small_caps': 12,
}

colors = {
    'black': (0, 0, 0),
    'dark_gray': (0.15, 0.15, 0.15),
    'medium_gray': (0.4, 0.4, 0.4),
    'light_gray': (0.6, 0.6, 0.6),
    'accent_blue': (0.2, 0.4, 0.8),
    'accent_red': (0.8, 0.2, 0.2),
}

def enhance_text(text):
    """Apply basic editorial enhancements"""
    # Format numbers with commas
    text = re.sub(r'\b(\d{4,})\b', lambda m: f"{int(m.group(1)):,}", text)
    # Proper percentage spacing
    text = re.sub(r'(\d+)\s*%', r'\1%', text)
    return text

def draw_enhanced_text(text_content, x, y, width, font_name, font_size, line_height, color=(0,0,0)):
    """Draw text with enhanced formatting"""
    enhanced_text = enhance_text(text_content)
    
    fill(*color)
    font(font_name)
    fontSize(font_size)
    
    words = enhanced_text.split()
    lines = []
    current_line = ""
    
    for word in words:
        # Check for social handles
        if word.startswith('@') or word.startswith('#'):
            # Handle social media elements with different styling
            test_line = current_line + " " + word if current_line else word
        else:
            test_line = current_line + " " + word if current_line else word
        
        test_width = textSize(test_line)[0]
        
        if test_width <= width - 20:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
                current_line = word
            else:
                lines.append(word)
    
    if current_line:
        lines.append(current_line)
    
    current_y = y
    for line in lines:
        # Draw social handles in blue
        if '@' in line or '#' in line:
            words_in_line = line.split()
            line_x = x + 10
            for word in words_in_line:
                if word.startswith('@') or word.startswith('#'):
                    fill(*colors['accent_blue'])
                    font(fonts['social_handle'])
                    fontSize(sizes['social'])
                else:
                    fill(*color)
                    font(font_name)
                    fontSize(font_size)
                
                text(word + " ", (line_x, current_y))
                line_x += textSize(word + " ")[0]
        else:
            text(line, (x + 10, current_y))
        current_y -= line_height
    
    return current_y - 5

def draw_drop_cap(letter, x, y):
    """Draw an editorial drop cap"""
    fill(*colors['accent_red'])
    font(fonts['display'])
    fontSize(sizes['display'] * 2)
    text(letter, (x, y))
    return textSize(letter)[0] + 8

def draw_pullquote_zone(text_content, x, y, width, height):
    """Draw text as a pullquote with editorial styling"""
    # Add pullquote line
    stroke(*colors['accent_blue'])
    strokeWidth(3)
    line((x, y), (x, y - height))
    stroke(None)
    
    return draw_enhanced_text(
        text_content, x + 15, y, width - 15,
        fonts['pullquote'], sizes['pullquote'], leading['pullquote'], colors['dark_gray']
    )

# =============================================================================
# PAGE 1: ENHANCED COVER LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Title with display typography
current_y = draw_enhanced_text(
    "AI News for July 2025",
    margins[3], page_height - margins[0] - 40, content_width,
    fonts['display'], sizes['display'], leading['display'], colors['black']
)

# Byline with kicker styling
current_y = draw_enhanced_text(
    "For: The Barbarian Group | Date: July 29, 2025",
    margins[3], current_y - 20, content_width,
    fonts['kicker'], sizes['kicker'], leading['kicker'], colors['medium_gray']
)

# Executive summary with drop cap
drop_cap_width = draw_drop_cap("W", margins[3], current_y - 40)
summary_text = "e checked 40+ X posts, 20+ news sources, 15 LinkedIn case studies, 10 TikTok creators, 10 Instagram showcases, and multiple Reddit threads for you. Estimated reading time saved (at 200wpm): 845 minutes. Total research cost: $0.40. It's worth looking at ChatGPT Agent's rocky launch, Midjourney's video democratization at $10/month, and the authentic Reddit verdict on Manus AI."

current_y = draw_enhanced_text(
    summary_text,
    margins[3] + drop_cap_width, current_y - 40, content_width - drop_cap_width,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Key findings as pullquote
highlights_text = "KEY FINDINGS: ChatGPT Agent launches with mixed reception • Midjourney V1 Video at $10/month democratizes AI video • Manus AI emerges as potential ChatGPT killer • $50B agent economy predicted by 2030 • Agencies report 30-40% cost reductions"

current_y = draw_pullquote_zone(
    highlights_text,
    margins[3], current_y - 30, content_width * 0.6, 120
)

# Research methodology
methodology_text = "RESEARCH SCOPE: 20 X/Twitter posts analyzed • 19 news/blog sources • 15 LinkedIn case studies • 10 TikTok viral creators • 10 Instagram showcases • Multiple Reddit threads • Period: July 1-29, 2025"

draw_enhanced_text(
    methodology_text,
    margins[3] + content_width * 0.65, page_height - margins[0] - 350, content_width * 0.35,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Footer
fill(*colors['medium_gray'])
font(fonts['body_italic'])
fontSize(sizes['body'])
text("The shift from 'AI that talks' to 'AI that does' — but supervision recommended", (margins[3], margins[2] + 10))

# =============================================================================
# PAGE 2: AI TWITTER/X RECAP WITH ENHANCED TYPOGRAPHY
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Section header
current_y = draw_enhanced_text(
    "🚀 AI Twitter/X Recap",
    margins[3], page_height - margins[0] - 20, content_width,  
    fonts['headline'], sizes['headline'], leading['headline'], colors['black']
)

# Subheading
current_y = draw_enhanced_text(
    "Major Agent Platform Releases (The Good, The Bad, The Hype)",
    margins[3], current_y - 20, content_width,
    fonts['subhead'], sizes['subhead'], leading['subhead'], colors['dark_gray']
)

# Feature story with drop cap
drop_cap_width = draw_drop_cap("O", margins[3], current_y - 40)
chatgpt_text = "penAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor. Initially for Pro subscribers, it promises 'deep research' tools and browser control via 'Operator' mode. Reception has been mixed. While Reuters calls it a milestone, Actuia notes it's 'far from an on-demand workforce' after just 12 hours in the wild."

current_y = draw_enhanced_text(
    chatgpt_text,
    margins[3] + drop_cap_width, current_y - 40, content_width - drop_cap_width,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Left column - Manus AI
manus_text = "The Manus AI 'ChatGPT Killer' Narrative: Beta testers are going wild for Manus AI, calling it the 'first general AI agent.' @JulianGoldieSEO claims users are canceling ChatGPT subs after demos showing multi-browser control and autonomous website building. Free tier available now, with premium expected under $200/month."

current_y = draw_enhanced_text(
    manus_text,
    margins[3], current_y - 30, content_width * 0.48,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Right column - Abacus AI  
abacus_text = "Abacus AI's Steady Enterprise Play: While others chase hype, Abacus AI quietly dominates enterprise automation. Their $10/month 'Super Assistant' builds SaaS apps and dashboards from prompts. CEO @bindureddy's approach: focus on monitoring and running agents, not just chatting."

draw_enhanced_text(
    abacus_text,
    margins[3] + content_width * 0.52, page_height - margins[0] - 280, content_width * 0.48,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# =============================================================================
# PAGE 3: VIDEO GENERATION REVOLUTION
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)  
rect(0, 0, page_width, page_height)

# Large magazine-style headline
current_y = draw_enhanced_text(
    "The Video Generation Revolution",
    margins[3], page_height - margins[0] - 20, content_width * 0.7,
    fonts['display'], sizes['display'], leading['display'], colors['black']
)

# Date context
draw_enhanced_text(
    "July 2025 Updates",
    margins[3] + content_width * 0.72, page_height - margins[0] - 40, content_width * 0.28,
    fonts['kicker'], sizes['kicker'], leading['kicker'], colors['medium_gray']
)

# Hero content with drop cap
drop_cap_width = draw_drop_cap("M", margins[3], current_y - 40)
midjourney_text = "idjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, Midjourney's video model brings AI video to the masses at $10/month. July updates include seamless looping with --loop command, start/end frame control, direct Discord integration, 720p resolution 'coming soon' (currently 480p, 24fps, 5-second clips)."

current_y = draw_enhanced_text(
    midjourney_text,
    margins[3] + drop_cap_width, current_y - 40, content_width - drop_cap_width,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Features as pullquote
features_text = "July Updates Include: • Seamless looping with --loop command • Start/end frame control • Direct Discord integration • 720p resolution 'coming soon' • Currently: 480p, 24fps, 5-second clips. The democratization is real — $10/month puts AI video creation in everyone's hands."

current_y = draw_pullquote_zone(
    features_text,
    margins[3], current_y - 30, content_width * 0.48, 120
)

# Runway comparison
runway_text = "Runway Maintains Pro Workflow Leadership: While Midjourney democratizes, Runway focuses on professional features—longer clips, better motion consistency. The emerging pattern: Midjourney for ideation → Runway for refinement. This two-tier approach is becoming the industry standard."

draw_enhanced_text(
    runway_text,
    margins[3] + content_width * 0.52, page_height - margins[0] - 280, content_width * 0.48,
    fonts['body'], sizes['body'], leading['body'], colors['black']
)

# Save the enhanced report
saveImage("output/barbarian_ai_enhanced_simple.pdf")
print("Enhanced editorial report with improved typography generated: output/barbarian_ai_enhanced_simple.pdf")
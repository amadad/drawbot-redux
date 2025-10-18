# BARBARIAN AI INTELLIGENCE REPORT - ENHANCED EDITORIAL TYPOGRAPHY
# Sophisticated editorial typography with content-aware formatting
# Following Hochuli principles with modern editorial flair

import sys
import os
import re

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from drawBot import *
print("Creating enhanced editorial typography with content-aware formatting")

# Document setup
page_width = 612
page_height = 792
margins = (54, 54, 54, 54)
content_width = page_width - margins[1] - margins[3]
content_height = page_height - margins[0] - margins[2]

# Enhanced Typography System - Editorial Focused
fonts = {
    # Display & Headlines
    'display': 'SpaceGrotesk-Bold',           # Big impact headlines
    'headline': 'SpaceGrotesk-Bold',          # Section headers
    'subhead': 'SpaceGrotesk-Medium',         # Subheadings
    'kicker': 'SpaceGrotesk-Regular',         # Small intro text above headlines
    
    # Body Text System
    'body': 'TASAOrbiterDeck-Regular',        # Main text
    'body_bold': 'TASAOrbiterDeck-Bold',      # Emphasis
    'body_italic': 'TASAOrbiterDeck-Italic',  # Light emphasis
    'body_medium': 'TASAOrbiterDeck-Medium',  # Semi-bold for contrast
    
    # Editorial Elements
    'pullquote': 'SpaceGrotesk-Medium',       # Large quotes
    'caption': 'TASAOrbiterDeck-Regular',     # Photo captions
    'byline': 'TASAOrbiterDeck-Medium',       # Author names
    'dateline': 'TASAOrbiterDeck-Regular',    # Dates and locations
    
    # Special Treatments
    'social_handle': 'SpaceGrotesk-Regular',  # @handles, #hashtags
    'small_caps': 'TASAOrbiterDeck-Bold',     # Acronyms, proper nouns
}

# Editorial-focused type sizes
sizes = {
    'display': 36,      # Big headlines
    'headline': 22,     # Section headers
    'subhead': 16,      # Subheadings
    'kicker': 10,       # Small intro text
    'body': 11,         # Main text
    'caption': 9,       # Captions
    'pullquote': 18,    # Large quotes
    'social': 10,       # Social handles
    'small_caps': 9,    # Small caps
}

# Proper leading following Hochuli
leading = {
    'display': 40,      # Generous for impact
    'headline': 26,     # Clear separation
    'subhead': 19,      # Proper hierarchy
    'kicker': 13,       # Tight for intro text
    'body': 15,         # Optimal readability
    'caption': 12,      # Compact but readable
    'pullquote': 22,    # Generous for quotes
    'social': 13,       # Consistent with body
    'small_caps': 12,   # Slightly tighter
}

# Editorial color palette
colors = {
    'black': (0, 0, 0),
    'dark_gray': (0.15, 0.15, 0.15),
    'medium_gray': (0.4, 0.4, 0.4),
    'light_gray': (0.6, 0.6, 0.6),
    'accent_blue': (0.2, 0.4, 0.8),      # For links/handles
    'accent_red': (0.8, 0.2, 0.2),       # For emphasis
}

class EditorialFormatter:
    """Content-aware formatter for editorial typography"""
    
    @staticmethod
    def format_numbers(text):
        """Format numbers according to editorial standards"""
        # Add commas to large numbers
        text = re.sub(r'\b(\d{1,3})(\d{3})\+', r'\1,\2+', text)  # 100M+ -> 100,000+
        text = re.sub(r'\b(\d{4,})\b', lambda m: f"{int(m.group(1)):,}", text)
        
        # Proper percentage spacing
        text = re.sub(r'(\d+)\s*%', r'\1%', text)
        
        # Currency formatting
        text = re.sub(r'\$(\d+)/month', r'$\1/month', text)
        
        return text
    
    @staticmethod
    def format_social_handles(text):
        """Identify and mark social handles for special styling"""
        # Mark Twitter/X handles
        text = re.sub(r'(@\w+)', r'[HANDLE]\1[/HANDLE]', text)
        
        # Mark hashtags
        text = re.sub(r'(#\w+)', r'[HASHTAG]\1[/HASHTAG]', text)
        
        return text
    
    @staticmethod
    def format_quotes(text):
        """Convert straight quotes to proper typographic quotes"""
        # Convert straight quotes to curly quotes (simplified for now)
        text = text.replace('"', '"').replace('"', '"')
        
        # Mark pullquotes
        text = re.sub(r'"([^"]*)"', r'[QUOTE]"\1"[/QUOTE]', text)
        
        return text
    
    @staticmethod
    def format_emphasis(text):
        """Mark text for proper emphasis styling"""
        # Mark company names and proper nouns for small caps
        companies = ['OpenAI', 'ChatGPT', 'GPT', 'AI', 'CEO', 'API', 'SaaS', 'B2B', 'ROI', 'DM', 'DMs']
        for company in companies:
            text = re.sub(f'\\b{company}\\b', f'[SMALLCAPS]{company}[/SMALLCAPS]', text)
        
        return text
    
    @staticmethod
    def process_text(text):
        """Apply all editorial formatting"""
        text = EditorialFormatter.format_numbers(text)
        text = EditorialFormatter.format_social_handles(text)
        text = EditorialFormatter.format_quotes(text)
        text = EditorialFormatter.format_emphasis(text)
        return text

def draw_formatted_text(text_content, x, y, width, base_font, base_size, base_leading, base_color=(0,0,0)):
    """Draw text with editorial formatting applied"""
    
    # Process text for formatting
    formatted_text = EditorialFormatter.process_text(text_content)
    
    # Split text into segments with different formatting
    segments = []
    current_text = ""
    current_format = "normal"
    
    i = 0
    while i < len(formatted_text):
        if formatted_text[i:i+8] == "[HANDLE]":
            if current_text:
                segments.append((current_text, current_format))
                current_text = ""
            current_format = "handle"
            i += 8
        elif formatted_text[i:i+9] == "[/HANDLE]":
            segments.append((current_text, current_format))
            current_text = ""
            current_format = "normal"
            i += 9
        elif formatted_text[i:i+11] == "[SMALLCAPS]":
            if current_text:
                segments.append((current_text, current_format))
                current_text = ""
            current_format = "smallcaps"
            i += 11
        elif formatted_text[i:i+12] == "[/SMALLCAPS]":
            segments.append((current_text, current_format))
            current_text = ""
            current_format = "normal"
            i += 12
        elif formatted_text[i:i+7] == "[QUOTE]":
            if current_text:
                segments.append((current_text, current_format))
                current_text = ""
            current_format = "quote"
            i += 7
        elif formatted_text[i:i+8] == "[/QUOTE]":
            segments.append((current_text, current_format))
            current_text = ""
            current_format = "normal"
            i += 8
        else:
            current_text += formatted_text[i]
            i += 1
    
    if current_text:
        segments.append((current_text, current_format))
    
    # Draw segments with appropriate formatting
    current_y = y
    line_text = ""
    line_segments = []
    
    for segment_text, segment_format in segments:
        words = segment_text.split()
        
        for word in words:
            test_line = line_text + " " + word if line_text else word
            
            # Calculate width with mixed formatting (simplified)
            font(base_font)
            fontSize(base_size)
            test_width = textSize(test_line)[0]
            
            if test_width <= width - 20:
                line_text = test_line
                line_segments.append((word + " ", segment_format))
            else:
                # Draw current line
                if line_text:
                    draw_formatted_line(line_segments, x + 10, current_y, base_font, base_size, base_color)
                    current_y -= base_leading
                
                # Start new line
                line_text = word
                line_segments = [(word + " ", segment_format)]
    
    # Draw remaining line
    if line_text:
        draw_formatted_line(line_segments, x + 10, current_y, base_font, base_size, base_color)
        current_y -= base_leading
    
    return current_y - 5

def draw_formatted_line(segments, x, y, base_font, base_size, base_color):
    """Draw a line with mixed formatting"""
    current_x = x
    
    for text, format_type in segments:
        if format_type == "handle":
            fill(*colors['accent_blue'])
            font(fonts['social_handle'])
            fontSize(sizes['social'])
        elif format_type == "smallcaps":
            fill(*base_color)
            font(fonts['small_caps'])
            fontSize(sizes['small_caps'])
            text = text.upper()  # Convert to uppercase for small caps effect
        elif format_type == "quote":
            fill(*colors['dark_gray'])
            font(fonts['body_italic'])
            fontSize(base_size)
        else:
            fill(*base_color)
            font(base_font)
            fontSize(base_size)
        
        text(text, (current_x, y))
        current_x += textSize(text)[0]

def draw_editorial_zone(text_content, x, y, width, height, style="body"):
    """Draw text in a zone with editorial styling"""
    
    if style == "display":
        return draw_formatted_text(
            text_content, x, y, width,
            fonts['display'], sizes['display'], leading['display'], colors['black']
        )
    elif style == "headline":
        return draw_formatted_text(
            text_content, x, y, width,
            fonts['headline'], sizes['headline'], leading['headline'], colors['black']
        )
    elif style == "subhead":
        return draw_formatted_text(
            text_content, x, y, width,
            fonts['subhead'], sizes['subhead'], leading['subhead'], colors['dark_gray']
        )
    elif style == "kicker":
        return draw_formatted_text(
            text_content, x, y, width,
            fonts['kicker'], sizes['kicker'], leading['kicker'], colors['medium_gray']
        )
    elif style == "pullquote":
        # Add special pullquote styling
        stroke(*colors['light_gray'])
        strokeWidth(2)
        line((x, y), (x, y - height))
        stroke(None)
        
        return draw_formatted_text(
            text_content, x + 15, y, width - 15,
            fonts['pullquote'], sizes['pullquote'], leading['pullquote'], colors['dark_gray']
        )
    else:  # body
        return draw_formatted_text(
            text_content, x, y, width,
            fonts['body'], sizes['body'], leading['body'], colors['black']
        )

def draw_drop_cap(letter, x, y, body_font, body_size):
    """Draw a drop cap"""
    fill(*colors['accent_red'])
    font(fonts['display'])
    fontSize(body_size * 3)
    text(letter, (x, y))
    return textSize(letter)[0] + 5

# =============================================================================
# PAGE 1: ENHANCED COVER LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Display title with proper spacing
title_zone = (margins[3], page_height - margins[0] - 120, content_width, 120)
current_y = draw_editorial_zone(
    "AI News for July 2025",
    *title_zone, "display"
)

# Zone 2: Styled byline with small caps
byline_zone = (margins[3], page_height - margins[0] - 160, content_width, 40)
current_y = draw_editorial_zone(
    "For: The Barbarian Group | Date: July 29, 2025",
    *byline_zone, "kicker"
)

# Zone 3: Executive summary with drop cap and enhanced formatting
summary_zone = (margins[3], page_height - margins[0] - 400, content_width, 240)
summary_text = """We checked 40+ X posts, 20+ news sources, 15 LinkedIn case studies, 10 TikTok creators, 10 Instagram showcases, and multiple Reddit threads for you. Estimated reading time saved (at 200wpm): 845 minutes. Total research cost: $0.40. It's worth looking at ChatGPT Agent's rocky launch, Midjourney's video democratization at $10/month, and the authentic Reddit verdict on Manus AI."""

# Draw drop cap
drop_cap_width = draw_drop_cap("W", margins[3], page_height - margins[0] - 180, fonts['body'], sizes['body'])

# Draw body text with drop cap offset
current_y = draw_editorial_zone(
    "e checked 40+ X posts, 20+ news sources, 15 LinkedIn case studies, 10 TikTok creators, 10 Instagram showcases, and multiple Reddit threads for you. Estimated reading time saved (at 200wpm): 845 minutes. Total research cost: $0.40. It's worth looking at ChatGPT Agent's rocky launch, Midjourney's video democratization at $10/month, and the authentic Reddit verdict on Manus AI.",
    margins[3] + drop_cap_width, page_height - margins[0] - 180, content_width - drop_cap_width, 220, "body"
)

# Zone 4: Key highlights as pullquote
highlights_zone = (margins[3], page_height - margins[0] - 580, content_width * 0.45, 180)
highlights_text = """KEY FINDINGS: ChatGPT Agent launches with mixed reception • Midjourney V1 Video at $10/month democratizes AI video • Manus AI emerges as potential "ChatGPT killer" • $50B agent economy predicted by 2030 • Agencies report 30-40% cost reductions"""

current_y = draw_editorial_zone(
    highlights_text,
    *highlights_zone, "pullquote"
)

# Zone 5: Research methodology with small caps
methodology_zone = (margins[3] + content_width * 0.55, page_height - margins[0] - 580, content_width * 0.45, 180)
methodology_text = """RESEARCH SCOPE: 20 X/Twitter posts analyzed • 19 news/blog sources • 15 LinkedIn case studies • 10 TikTok viral creators • 10 Instagram showcases • Multiple Reddit threads • Period: July 1-29, 2025"""

current_y = draw_editorial_zone(
    methodology_text,
    *methodology_zone, "body"
)

# Zone 6: Footer tagline in italic
footer_zone = (margins[3], margins[2], content_width, 40)
fill(*colors['medium_gray'])
font(fonts['body_italic'])
fontSize(sizes['body'])
text("The shift from 'AI that talks' to 'AI that does' — but supervision recommended", (margins[3], margins[2] + 10))

# =============================================================================
# PAGE 2: AI TWITTER/X RECAP - ENHANCED NEWS LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Section header with emoji and proper spacing
header_zone = (margins[3], page_height - margins[0] - 60, content_width, 60)
current_y = draw_editorial_zone(
    "🚀 AI Twitter/X Recap",
    *header_zone, "headline"
)

# Zone 2: Stylized subheading
subhead_zone = (margins[3], page_height - margins[0] - 100, content_width, 40)
current_y = draw_editorial_zone(
    "Major Agent Platform Releases (The Good, The Bad, The Hype)",
    *subhead_zone, "subhead"
)

# Zone 3: Feature story with enhanced formatting
feature_zone = (margins[3], page_height - margins[0] - 280, content_width, 180)
chatgpt_text = """OpenAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor. Initially for Pro subscribers, it promises "deep research" tools and browser control via "Operator" mode. Reception has been... mixed. While Reuters calls it a milestone, Actuia notes it's "far from an on-demand workforce" after just 12 hours in the wild. Use cases include crypto trading automation and research reports, but creative tasks remain a struggle."""

# Add drop cap for feature story
drop_cap_width = draw_drop_cap("O", margins[3], page_height - margins[0] - 200, fonts['body'], sizes['body'])
current_y = draw_editorial_zone(
    "penAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor. Initially for Pro subscribers, it promises "deep research" tools and browser control via "Operator" mode. Reception has been... mixed. While Reuters calls it a milestone, Actuia notes it's "far from an on-demand workforce" after just 12 hours in the wild. Use cases include crypto trading automation and research reports, but creative tasks remain a struggle.",
    margins[3] + drop_cap_width, page_height - margins[0] - 200, content_width - drop_cap_width, 180, "body"
)

# Zone 4: Left column with Manus AI story
left_col_zone = (margins[3], page_height - margins[0] - 480, content_width * 0.48, 200)
manus_text = """The Manus AI "ChatGPT Killer" Narrative: Beta testers are going wild for Manus AI, calling it the "first general AI agent." @JulianGoldieSEO claims users are canceling ChatGPT subs after demos showing multi-browser control and autonomous website building. Free tier available now, with premium expected under $200/month. The hype is real, but it's still beta—treat claims of "ChatGPT killer" status with caution."""

current_y = draw_editorial_zone(
    manus_text,
    *left_col_zone, "body"
)

# Zone 5: Right column with Abacus AI story
right_col_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 480, content_width * 0.48, 200)
abacus_text = """Abacus AI's Steady Enterprise Play: While others chase hype, Abacus AI quietly dominates enterprise automation. Their $10/month "Super Assistant" builds SaaS apps and dashboards from prompts. Featured in Daily AI Agent News (July 24), it's positioned as the practical alternative. CEO @bindureddy's approach: focus on monitoring and running agents, not just chatting."""

current_y = draw_editorial_zone(
    abacus_text,
    *right_col_zone, "body"
)

# Zone 6: Enhanced footer with proper typography
fill(*colors['light_gray'])
font(fonts['caption'])
fontSize(sizes['caption'])
text("Continued: Video Generation Revolution, Viral Content & Agency Insights →", (margins[3], margins[2] + 10))

# =============================================================================
# PAGE 3: VIDEO GENERATION - ENHANCED MAGAZINE LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Large magazine-style headline
headline_zone = (margins[3], page_height - margins[0] - 80, content_width * 0.7, 80)
current_y = draw_editorial_zone(
    "The Video Generation Revolution",
    *headline_zone, "display"
)

# Zone 2: Date/context in kicker style
context_zone = (margins[3] + content_width * 0.72, page_height - margins[0] - 60, content_width * 0.28, 60)
current_y = draw_editorial_zone(
    "July 2025 Updates",
    *context_zone, "kicker"
)

# Zone 3: Hero content with enhanced formatting
hero_zone = (margins[3], page_height - margins[0] - 240, content_width, 160)
midjourney_text = """Midjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, Midjourney's video model brings AI video to the masses at $10/month. July updates include: Seamless looping with --loop command, Start/end frame control, Direct Discord integration, 720p resolution "coming soon" (currently 480p, 24fps, 5-second clips). The elephant in the room? Disney's plagiarism lawsuit, which could reshape content generation limits."""

# Add drop cap
drop_cap_width = draw_drop_cap("M", margins[3], page_height - margins[0] - 180, fonts['body'], sizes['body'])
current_y = draw_editorial_zone(
    "idjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, Midjourney's video model brings AI video to the masses at $10/month. July updates include: Seamless looping with --loop command, Start/end frame control, Direct Discord integration, 720p resolution "coming soon" (currently 480p, 24fps, 5-second clips). The elephant in the room? Disney's plagiarism lawsuit, which could reshape content generation limits.",
    margins[3] + drop_cap_width, page_height - margins[0] - 180, content_width - drop_cap_width, 160, "body"
)

# Zone 4: Features as pullquote style
left_features_zone = (margins[3], page_height - margins[0] - 420, content_width * 0.48, 180)
features_text = """July Updates Include: • Seamless looping with --loop command • Start/end frame control • Direct Discord integration • 720p resolution "coming soon" • Currently: 480p, 24fps, 5-second clips. The democratization is real — $10/month puts AI video creation in everyone's hands."""

current_y = draw_editorial_zone(
    features_text,
    *left_features_zone, "pullquote"
)

# Zone 5: Runway comparison
right_runway_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 420, content_width * 0.48, 180)
runway_text = """Runway Maintains Pro Workflow Leadership: While Midjourney democratizes, Runway focuses on professional features—longer clips, better motion consistency. The emerging pattern: Midjourney for ideation → Runway for refinement. This two-tier approach is becoming the industry standard for video generation workflows."""

current_y = draw_editorial_zone(
    runway_text,
    *right_runway_zone, "body"
)

# Zone 6: Bottom insight in italic
fill(*colors['medium_gray'])
font(fonts['body_italic'])
fontSize(sizes['body'])
text("Disney lawsuit outcome will set precedents for all AI video generation", (margins[3], margins[2] + 10))

# =============================================================================
# PAGE 4: VIRAL CONTENT - ENHANCED DASHBOARD STYLE
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Dashboard header with enhanced styling
dash_header_zone = (margins[3], page_height - margins[0] - 50, content_width, 50)
current_y = draw_editorial_zone(
    "Viral AI Content & Platform Buzz",
    *dash_header_zone, "headline"
)

# Zone 2: Trending topics with kicker treatment
trending_header_zone = (margins[3], page_height - margins[0] - 85, content_width * 0.7, 35)
current_y = draw_editorial_zone(
    "Top Trending Topics (July 2025)",
    *trending_header_zone, "subhead"
)

# Zone 3: Main trending content with sophisticated formatting
trending_zone = (margins[3], page_height - margins[0] - 280, content_width * 0.65, 195)
trending_text = """1. AI + Astrology Goes Mainstream: @hotgirltarotsha's July predictions hit millions of views. Water signs warned about "toxic friends," fire signs promised "financial glow-ups." Why it matters: AI personalization meets human desire for meaning.

2. TikTok's "AI Gold Rush": Natural disaster clips generated by AI are hitting 100M+ views. Creators leverage AI for viral content at unprecedented scale. The platform's "Aura Farming" dance trend adds another layer of AI-human creative fusion.

3. The $50B Agent Economy Prediction: Market analysts project AI agents will create a $50B+ market by 2030. Agencies report 30-40% cost reductions already. @sidhant notes the shift from "AI as tool" to "AI as workforce."

4. Quantum + AI Convergence: Posts about solid-state batteries and quantum computing breakthroughs signal hardware catching up to software ambitions. "Agentic AI" becomes the buzzword of July."""

# Add drop cap
drop_cap_width = draw_drop_cap("1", margins[3], page_height - margins[0] - 200, fonts['body'], sizes['body'])
current_y = draw_editorial_zone(
    ". AI + Astrology Goes Mainstream: @hotgirltarotsha's July predictions hit millions of views. Water signs warned about "toxic friends," fire signs promised "financial glow-ups." Why it matters: AI personalization meets human desire for meaning. 2. TikTok's "AI Gold Rush": Natural disaster clips generated by AI are hitting 100M+ views. Creators leverage AI for viral content at unprecedented scale. The platform's "Aura Farming" dance trend adds another layer of AI-human creative fusion. 3. The $50B Agent Economy Prediction: Market analysts project AI agents will create a $50B+ market by 2030. Agencies report 30-40% cost reductions already. @sidhant notes the shift from "AI as tool" to "AI as workforce." 4. Quantum + AI Convergence: Posts about solid-state batteries and quantum computing breakthroughs signal hardware catching up to software ambitions. "Agentic AI" becomes the buzzword of July.",
    margins[3] + drop_cap_width, page_height - margins[0] - 200, content_width * 0.65 - drop_cap_width, 195, "body"
)

# Zone 5: Sidebar with key stats as pullquote
sidebar_zone = (margins[3] + content_width * 0.7, page_height - margins[0] - 280, content_width * 0.3, 195)
stats_text = """KEY METRICS: 100M+ views on AI disaster clips • $50B market predicted by 2030 • 30-40% agency cost reductions • "Agentic AI" trending buzzword. TOP CREATORS: @hotgirltarotsha @sidhant @bindureddy @JulianGoldieSEO. PLATFORMS: TikTok: AI Gold Rush • X/Twitter: Agent buzz • Instagram: Video showcases"""

current_y = draw_editorial_zone(
    stats_text,
    *sidebar_zone, "pullquote"
)

# Zone 4: Agency transformation in enhanced body text
agency_zone = (margins[3], page_height - margins[0] - 450, content_width, 120)
agency_text = """Agency Transformation Insights — Real Cost Savings (Not Just Hype): Production costs down 50% with AI tools. Campaign turnaround 40% faster with automated workflows. Manual design time 60% reduction reported. One agency case study: $500K+ annual savings from automated research. Success patterns from early adopters: AI as "creative partner" not replacement, predictive analytics for trend forecasting working, personalization at scale finally achievable, human creativity + machine efficiency = winning combo."""

current_y = draw_editorial_zone(
    agency_text,
    *agency_zone, "body"
)

# Save the enhanced editorial report
saveImage("output/barbarian_ai_enhanced_editorial.pdf")
print("Enhanced editorial report with sophisticated typography generated: output/barbarian_ai_enhanced_editorial.pdf")
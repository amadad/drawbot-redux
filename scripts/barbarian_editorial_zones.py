# BARBARIAN AI INTELLIGENCE REPORT - PROPER EDITORIAL LAYOUTS
# Using zone-based grid system with varied layouts per page
# ALL content from the report properly laid out in editorial zones

import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from drawBot import *
print("Creating proper editorial layouts with zone system")

# Document setup
page_width = 612
page_height = 792
margins = (54, 54, 54, 54)
content_width = page_width - margins[1] - margins[3]
content_height = page_height - margins[0] - margins[2]

# Typography following Hochuli
fonts = {
    'title': 'SpaceGrotesk-Bold',
    'heading': 'SpaceGrotesk-Bold', 
    'subhead': 'SpaceGrotesk-Medium',
    'body': 'TASAOrbiterDeck-Regular',
    'body_bold': 'TASAOrbiterDeck-Bold',
    'body_italic': 'TASAOrbiterDeck-Italic',
}

sizes = {
    'title': 32,
    'heading': 18,
    'subhead': 14,
    'body': 11,
    'caption': 9,
}

leading = {
    'title': 38,
    'heading': 22,
    'subhead': 17,
    'body': 15,
    'caption': 12,
}

def draw_text_in_zone(text_content, x, y, width, height, font_name, font_size, line_height, color=(0,0,0)):
    """Draw text within a specific zone"""
    fill(*color)
    font(font_name)
    fontSize(font_size)
    
    words = text_content.split()
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_width = textSize(test_line)[0]
        
        if test_width <= width - 20:  # margin within zone
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
                current_line = word
            else:
                lines.append(word)
    
    if current_line:
        lines.append(current_line)
    
    # Draw lines within zone height
    current_y = y + height - line_height - 10
    lines_drawn = 0
    max_lines = int((height - 20) / line_height)
    
    for line in lines[:max_lines]:
        if current_y > y + 10:
            text(line, (x + 10, current_y))
            current_y -= line_height
            lines_drawn += 1
    
    return lines_drawn < len(lines)  # Return True if text was truncated

# =============================================================================
# PAGE 1: COVER/TITLE LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Main Title (top, full width)
title_zone = (margins[3], page_height - margins[0] - 120, content_width, 120)
draw_text_in_zone(
    "AI News for July 2025",
    *title_zone,
    fonts['title'], sizes['title'], leading['title'], (0, 0, 0)
)

# Zone 2: Subtitle/Client info (below title)
subtitle_zone = (margins[3], page_height - margins[0] - 180, content_width, 60)
draw_text_in_zone(
    "For: The Barbarian Group | Date: July 29, 2025",
    *subtitle_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.3, 0.3, 0.3)
)

# Zone 3: Executive Summary (large central area)
summary_zone = (margins[3], page_height - margins[0] - 400, content_width, 220)
summary_text = """We checked 40+ X posts, 20+ news sources, 15 LinkedIn case studies, 10 TikTok creators, 10 Instagram showcases, and multiple Reddit threads for you. Estimated reading time saved (at 200wpm): 845 minutes. Total research cost: $0.40. It's worth looking at ChatGPT Agent's rocky launch, Midjourney's video democratization at $10/month, and the authentic Reddit verdict on Manus AI."""

draw_text_in_zone(
    summary_text,
    *summary_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Key highlights sidebar
highlights_zone = (margins[3], page_height - margins[0] - 580, content_width * 0.45, 180)
highlights_text = """KEY FINDINGS:

• ChatGPT Agent launches with mixed reception
• Midjourney V1 Video at $10/month democratizes AI video
• Manus AI emerges as potential "ChatGPT killer"
• $50B agent economy predicted by 2030
• Agencies report 30-40% cost reductions"""

draw_text_in_zone(
    highlights_text,
    *highlights_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Research methodology
methodology_zone = (margins[3] + content_width * 0.55, page_height - margins[0] - 580, content_width * 0.45, 180)
methodology_text = """RESEARCH SCOPE:

• 20 X/Twitter posts analyzed
• 19 news/blog sources
• 15 LinkedIn case studies
• 10 TikTok viral creators
• 10 Instagram showcases
• Multiple Reddit threads
• Period: July 1-29, 2025"""

draw_text_in_zone(
    methodology_text,
    *methodology_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 6: Footer tagline
footer_zone = (margins[3], margins[2], content_width, 40)
draw_text_in_zone(
    "The shift from 'AI that talks' to 'AI that does' — but supervision recommended",
    *footer_zone,
    fonts['body_italic'], sizes['body'], leading['body'], (0.4, 0.4, 0.4)
)

# =============================================================================
# PAGE 2: AI TWITTER/X RECAP - NEWS LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Section header
header_zone = (margins[3], page_height - margins[0] - 60, content_width, 60)
draw_text_in_zone(
    "🚀 AI Twitter/X Recap",
    *header_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: Subheading
subhead_zone = (margins[3], page_height - margins[0] - 100, content_width, 40)
draw_text_in_zone(
    "Major Agent Platform Releases (The Good, The Bad, The Hype)",
    *subhead_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.2, 0.2, 0.2)
)

# Zone 3: Feature story - ChatGPT Agent
feature_zone = (margins[3], page_height - margins[0] - 280, content_width, 180)
chatgpt_text = """OpenAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor. Initially for Pro subscribers, it promises "deep research" tools and browser control via "Operator" mode. Reception has been... mixed. While Reuters calls it a milestone, Actuia notes it's "far from an on-demand workforce" after just 12 hours in the wild. Use cases include crypto trading automation and research reports, but creative tasks remain a struggle."""

draw_text_in_zone(
    chatgpt_text,
    *feature_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Left column - Manus AI story
left_col_zone = (margins[3], page_height - margins[0] - 480, content_width * 0.48, 200)
manus_text = """The Manus AI "ChatGPT Killer" Narrative: Beta testers are going wild for Manus AI, calling it the "first general AI agent." @JulianGoldieSEO claims users are canceling ChatGPT subs after demos showing multi-browser control and autonomous website building. Free tier available now, with premium expected under $200/month. The hype is real, but it's still beta—treat claims of "ChatGPT killer" status with caution."""

draw_text_in_zone(
    manus_text,
    *left_col_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Right column - Abacus AI story
right_col_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 480, content_width * 0.48, 200)
abacus_text = """Abacus AI's Steady Enterprise Play: While others chase hype, Abacus AI quietly dominates enterprise automation. Their $10/month "Super Assistant" builds SaaS apps and dashboards from prompts. Featured in Daily AI Agent News (July 24), it's positioned as the practical alternative. CEO @bindureddy's approach: focus on monitoring and running agents, not just chatting."""

draw_text_in_zone(
    abacus_text,
    *right_col_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 6: Footer - section continuation note
footer_zone = (margins[3], margins[2], content_width, 30)
draw_text_in_zone(
    "Continued: Video Generation Revolution, Viral Content & Agency Insights →",
    *footer_zone,
    fonts['body_italic'], sizes['caption'], leading['caption'], (0.5, 0.5, 0.5)
)

# =============================================================================
# PAGE 3: VIDEO GENERATION - MAGAZINE LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Large headline (asymmetric)
headline_zone = (margins[3], page_height - margins[0] - 80, content_width * 0.7, 80)
draw_text_in_zone(
    "The Video Generation Revolution",
    *headline_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: Date/context (top right)
context_zone = (margins[3] + content_width * 0.72, page_height - margins[0] - 60, content_width * 0.28, 60)
draw_text_in_zone(
    "July 2025 Updates",
    *context_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.4, 0.4, 0.4)
)

# Zone 3: Hero content - Midjourney story
hero_zone = (margins[3], page_height - margins[0] - 240, content_width, 160)
midjourney_text = """Midjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, Midjourney's video model brings AI video to the masses at $10/month. July updates include: Seamless looping with --loop command, Start/end frame control, Direct Discord integration, 720p resolution "coming soon" (currently 480p, 24fps, 5-second clips). The elephant in the room? Disney's plagiarism lawsuit, which could reshape content generation limits."""

draw_text_in_zone(
    midjourney_text,
    *hero_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Left column - Features
left_features_zone = (margins[3], page_height - margins[0] - 420, content_width * 0.48, 180)
features_text = """July Updates Include:

• Seamless looping with --loop command
• Start/end frame control  
• Direct Discord integration
• 720p resolution "coming soon"
• Currently: 480p, 24fps, 5-second clips

The democratization is real - $10/month puts AI video creation in everyone's hands."""

draw_text_in_zone(
    features_text,
    *left_features_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Right column - Runway comparison
right_runway_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 420, content_width * 0.48, 180)
runway_text = """Runway Maintains Pro Workflow Leadership: While Midjourney democratizes, Runway focuses on professional features—longer clips, better motion consistency. 

The emerging pattern: 
Midjourney for ideation → Runway for refinement.

This two-tier approach is becoming the industry standard for video generation workflows."""

draw_text_in_zone(
    runway_text,
    *right_runway_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 6: Bottom note
bottom_zone = (margins[3], margins[2] + 20, content_width, 40)
draw_text_in_zone(
    "Disney lawsuit outcome will set precedents for all AI video generation",
    *bottom_zone,
    fonts['body_italic'], sizes['body'], leading['body'], (0.4, 0.4, 0.4)
)

# =============================================================================
# PAGE 4: VIRAL CONTENT - DASHBOARD STYLE
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Dashboard header
dash_header_zone = (margins[3], page_height - margins[0] - 50, content_width, 50)
draw_text_in_zone(
    "Viral AI Content & Platform Buzz",
    *dash_header_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: Trending topics header
trending_header_zone = (margins[3], page_height - margins[0] - 85, content_width * 0.7, 35)
draw_text_in_zone(
    "Top Trending Topics (July 2025)",
    *trending_header_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.2, 0.2, 0.2)
)

# Zone 3: Main trending content
trending_zone = (margins[3], page_height - margins[0] - 280, content_width * 0.65, 195)
trending_text = """1. AI + Astrology Goes Mainstream: @hotgirltarotsha's July predictions hit millions of views. Water signs warned about "toxic friends," fire signs promised "financial glow-ups." Why it matters: AI personalization meets human desire for meaning.

2. TikTok's "AI Gold Rush": Natural disaster clips generated by AI are hitting 100M+ views. Creators leverage AI for viral content at unprecedented scale. The platform's "Aura Farming" dance trend adds another layer of AI-human creative fusion.

3. The $50B Agent Economy Prediction: Market analysts project AI agents will create a $50B+ market by 2030. Agencies report 30-40% cost reductions already. @sidhant notes the shift from "AI as tool" to "AI as workforce."

4. Quantum + AI Convergence: Posts about solid-state batteries and quantum computing breakthroughs signal hardware catching up to software ambitions. "Agentic AI" becomes the buzzword of July."""

draw_text_in_zone(
    trending_text,
    *trending_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Sidebar - Key Stats
sidebar_zone = (margins[3] + content_width * 0.7, page_height - margins[0] - 280, content_width * 0.3, 195)
stats_text = """KEY METRICS:

• 100M+ views on AI disaster clips
• $50B market predicted by 2030
• 30-40% agency cost reductions
• "Agentic AI" trending buzzword

TOP CREATORS:
@hotgirltarotsha
@sidhant
@bindureddy
@JulianGoldieSEO

PLATFORMS:
TikTok: AI Gold Rush
X/Twitter: Agent buzz
Instagram: Video showcases"""

draw_text_in_zone(
    stats_text,
    *sidebar_zone,
    fonts['body'], sizes['caption'], leading['caption'], (0, 0, 0)
)

# Zone 4: Agency transformation (bottom wide)
agency_zone = (margins[3], page_height - margins[0] - 450, content_width, 120)
agency_text = """Agency Transformation Insights - Real Cost Savings (Not Just Hype): Production costs down 50% with AI tools. Campaign turnaround 40% faster with automated workflows. Manual design time 60% reduction reported. One agency case study: $500K+ annual savings from automated research. Success patterns from early adopters: AI as "creative partner" not replacement, predictive analytics for trend forecasting working, personalization at scale finally achievable, human creativity + machine efficiency = winning combo."""

draw_text_in_zone(
    agency_text,
    *agency_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 6: Dashboard footer
dash_footer_zone = (margins[3], margins[2], content_width, 30)
draw_text_in_zone(
    "What's working: Structured workflows • What's struggling: Fully autonomous creative work",
    *dash_footer_zone,
    fonts['body_italic'], sizes['caption'], leading['caption'], (0.5, 0.5, 0.5)
)

# =============================================================================
# PAGE 5: PROFESSIONAL INSIGHTS - REPORT LAYOUT
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Section title
title_zone = (margins[3], page_height - margins[0] - 70, content_width, 70)
draw_text_in_zone(
    "🔗 LinkedIn Professional Insights & 🤖 Reddit Deep Dive",
    *title_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: Subtitle
subtitle_zone = (margins[3], page_height - margins[0] - 110, content_width, 40)
draw_text_in_zone(
    "Enterprise adoption and authentic user feedback",
    *subtitle_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.3, 0.3, 0.3)
)

# Zone 3: Key findings (wide banner)
findings_zone = (margins[3], page_height - margins[0] - 200, content_width, 90)
findings_text = """Agency Transformation Numbers: Marketing agencies using ChatGPT Agent for competitive analysis: 35% ROI increase. Recruiting agencies with AI-powered LinkedIn sourcing: 30% faster hiring cycles. Digital agencies automating LinkedIn DMs and follow-ups: 25% uplift in client engagement. Healthcare and legal agencies using agents for lead qualification: 2x efficiency gains."""

draw_text_in_zone(
    findings_text,
    *findings_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Main content - LinkedIn insights
linkedin_zone = (margins[3], page_height - margins[0] - 380, content_width * 0.6, 180)
linkedin_text = """ChatGPT Agent in the Enterprise Wild: LinkedIn professionals are sharing mixed but revealing experiences with OpenAI's new agent. Medium case studies show 50% faster job placement rates through automated outreach. A B2B SaaS agency reported 3x boost in leads using agent-automated LinkedIn ad campaigns, with 40% higher conversion rates. But professionals warn about the "2% error rate" in complex multi-step processes—enough to erode trust in client-facing work."""

draw_text_in_zone(
    linkedin_text,
    *linkedin_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Reddit insights sidebar
reddit_zone = (margins[3] + content_width * 0.65, page_height - margins[0] - 380, content_width * 0.35, 180)
reddit_text = """Reddit's Unfiltered Truth:

r/AI_Agents on Manus AI: Users praise it for "feeling like having a junior assistant" in research. "ChatGPT better for creative writing; Manus shines in agentic stuff."

r/ChatGPTCoding: Developers say Manus excels at multi-file projects where ChatGPT struggles.

Platform Scores:
• Manus AI: 4-5/5 innovation
• ChatGPT: 4.5/5 accessibility  
• Midjourney V1: Revolutionary but early"""

draw_text_in_zone(
    reddit_text,
    *reddit_zone,
    fonts['body'], sizes['caption'], leading['caption'], (0, 0, 0)
)

# Zone 6: Professional verdict
verdict_zone = (margins[3], margins[2] + 10, content_width, 50)
draw_text_in_zone(
    "Professional Verdict: Use agents for 80% automation, human oversight for final 20%",
    *verdict_zone,
    fonts['body_bold'], sizes['body'], leading['body'], (0, 0, 0)
)

# =============================================================================
# PAGE 6: SOCIAL PLATFORMS - MULTI-COLUMN
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Double header
double_header_zone = (margins[3], page_height - margins[0] - 60, content_width, 60)
draw_text_in_zone(
    "🎵 TikTok Viral AI Trends & 📸 Instagram AI Art Showcases",
    *double_header_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: TikTok section header
tiktok_header_zone = (margins[3], page_height - margins[0] - 95, content_width * 0.5, 35)
draw_text_in_zone(
    "The AI Content Creator Revolution",
    *tiktok_header_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.2, 0.2, 0.2)
)

# Zone 3: TikTok content (left column)
tiktok_zone = (margins[3], page_height - margins[0] - 320, content_width * 0.48, 225)
tiktok_text = """Top AI Creators Exploding in July:

1. @AIArtWizard: "AI vs. Reality" challenges transforming user photos into surreal art—tens of millions of views per post

2. @ChatbotComedy: AI chatbot skits mimicking celebrity interviews, remixed thousands of times

3. @DeepfakeDaily: Ethical parodies sparking authenticity debates (NPR coverage)

4. @AIMusicMashup: AI-composed songs driving dance challenges with TikTok Shop integration

The "AI Gold Rush" Phenomenon: Natural disaster clips generated by AI hitting 100M+ views. Creators report 10x engagement when mixing AI with personal storytelling. The algorithm loves it: short-form series under 60 seconds with hooks like "What if AI redesigned your life?"

E-Commerce Integration Success: Beauty brands using AI-generated hauls for Korean skincare products seeing millions of views. Over 4 million TikTok Shop sellers now leverage AI for "shoppertainment" content. Key trend: AI voiceovers + trending sounds = viral discovery."""

draw_text_in_zone(
    tiktok_text,
    *tiktok_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Instagram header
insta_header_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 95, content_width * 0.48, 35)
draw_text_in_zone(
    "Midjourney V1 Video Takes Over the Feed",
    *insta_header_zone,
    fonts['subhead'], sizes['subhead'], leading['subhead'], (0.2, 0.2, 0.2)
)

# Zone 5: Instagram content (right column)
insta_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 320, content_width * 0.48, 225)
insta_text = """Agency Adoption Accelerating: Creative agencies like Wieden+Kennedy and Ogilvy are sharing AI-integrated projects on Instagram, including Midjourney video pilots from mid-2025. Agencies host virtual showcases via Instagram Live, demonstrating V1's enterprise potential for quick prototyping.

Top AI Art Accounts to Watch:
• @midjourney: Official V1 video teasers and community highlights
• @theaiart: Started posting short V1 videos in July—dreamlike sequences going viral
• @digitaldreamsai: Midjourney V1 experiments with immersive narratives
• @ai.storyteller: Character-driven worlds now featuring animated video clips

Trending Hashtags: #MidjourneyV1, #AIVideoArt, and #MidjourneyVideo showcase user-generated content with 5-10 second fantastical scenes. The Art Newspaper notes influencer power and AI tools are driving art world trends, with agencies collaborating for branded content."""

draw_text_in_zone(
    insta_text,
    *insta_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 6: Cross-platform insights
cross_platform_zone = (margins[3], margins[2] + 10, content_width, 60)
draw_text_in_zone(
    "Cross-Platform Pattern: TikTok drives viral discovery, Instagram showcases polished results. Agencies using both for complete AI content strategies.",
    *cross_platform_zone,
    fonts['body_italic'], sizes['body'], leading['body'], (0.4, 0.4, 0.4)
)

# =============================================================================
# PAGE 7: ACTION ITEMS & CONCLUSION
# =============================================================================
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

# Zone 1: Action header
action_header_zone = (margins[3], page_height - margins[0] - 60, content_width, 60)
draw_text_in_zone(
    "💡 Action Items for The Barbarian Group",
    *action_header_zone,
    fonts['heading'], sizes['heading'], leading['heading'], (0, 0, 0)
)

# Zone 2: Try this month
try_zone = (margins[3], page_height - margins[0] - 200, content_width * 0.48, 140)
try_text = """Try This Month:

1. Midjourney V1 Video ($10/month): Perfect for rapid concept visualization. Start with the --loop command for social content.

2. ChatGPT Agent Mode: Test on a low-stakes workflow automation project. Expect 70% success, plan for human finishing.

3. Abacus AI Trial: If you need dashboards or data viz, this beats manual work every time."""

draw_text_in_zone(
    try_text,
    *try_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 3: Watch trends
watch_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 200, content_width * 0.48, 140)
watch_text = """Watch These Trends:

• Manus AI's full launch (could disrupt if pricing stays competitive)

• Disney vs. Midjourney outcome (will set content generation precedents)

• "Agentic AI" implementations beyond chat interfaces"""

draw_text_in_zone(
    watch_text,
    *watch_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 4: Skip for now
skip_zone = (margins[3], page_height - margins[0] - 320, content_width * 0.48, 120)
skip_text = """Skip For Now:

• GPT-5 rumors (August maybe, but who knows)
• Expensive "AI transformation" consultants (tools are democratized enough)
• Waiting for "perfect" AI (good enough is profitable now)"""

draw_text_in_zone(
    skip_text,
    *skip_zone,
    fonts['body'], sizes['body'], leading['body'], (0, 0, 0)
)

# Zone 5: Research transparency
research_zone = (margins[3] + content_width * 0.52, page_height - margins[0] - 380, content_width * 0.48, 180)
research_text = """📊 Research Transparency

Sources Analyzed:
• 20 X/Twitter posts on trending topics
• 19 news/blog sources on AI agents  
• 15 LinkedIn professional case studies and reviews
• 10 TikTok viral AI creators and trends
• 10 Instagram AI art showcases and agency projects
• Multiple Reddit threads (r/AI_Agents, r/ChatGPTCoding, r/midjourney)
• Time period: July 1-29, 2025

Notable Sources: @hotgirltarotsha (viral astrology), @JulianGoldieSEO (Manus AI hype), @bindureddy (Abacus AI CEO), OpenAI Blog, Reuters, TechRadar Live Coverage"""

draw_text_in_zone(
    research_text,
    *research_zone,
    fonts['body'], sizes['caption'], leading['caption'], (0, 0, 0)
)

# Zone 6: Final conclusion
conclusion_zone = (margins[3], margins[2] + 40, content_width, 80)
draw_text_in_zone(
    "The Punchline: July 2025 marks the shift from 'AI that talks' to 'AI that does'—but like teaching a teenager to drive, it works better with supervision. Agencies embracing the mess while competitors wait for perfection will own the next 18 months.",
    *conclusion_zone,
    fonts['body_bold'], sizes['body'], leading['body'], (0, 0, 0)
)

# Save the complete editorial report
saveImage("output/barbarian_ai_proper_editorial.pdf")
print("Proper zone-based editorial report generated: output/barbarian_ai_proper_editorial.pdf")
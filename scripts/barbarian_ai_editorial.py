# BARBARIAN AI INTELLIGENCE REPORT - EDITORIAL LAYOUT
# Proper editorial typography following Hochuli principles
# Using complete verbatim content from the original report

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from drawBot import *
print("Using drawbot-skia for editorial layout")

# Document setup - US Letter
page_width = 612  # 8.5 inches
page_height = 792  # 11 inches

# Hochuli-based margins (generous for readability)
margins = (54, 54, 54, 54)  # 0.75 inch margins
content_width = page_width - margins[1] - margins[3]  # 504pt
content_height = page_height - margins[0] - margins[2]  # 684pt

# Typography following Hochuli principles
fonts = {
    'heading': 'SpaceGrotesk-Bold',
    'subheading': 'SpaceGrotesk-Medium', 
    'body': 'TASAOrbiterDeck-Regular',
    'body_bold': 'TASAOrbiterDeck-Bold',
    'body_italic': 'TASAOrbiterDeck-Italic',
}

# Type sizes following Hochuli scaling
sizes = {
    'title': 28,
    'section': 18,
    'subsection': 14,
    'body': 11,
    'caption': 9,
    'small': 8,
}

# Line spacing following Hochuli (generous for readability)
leading = {
    'title': 32,
    'section': 22,
    'subsection': 18,
    'body': 15,
    'caption': 12,
    'small': 10,
}

# Colors (minimal, professional)
colors = {
    'black': (0, 0, 0),
    'dark_gray': (0.2, 0.2, 0.2),
    'medium_gray': (0.4, 0.4, 0.4),
    'light_gray': (0.6, 0.6, 0.6),
}

def draw_text_block(text_content, x, y, width, font_name, font_size, line_height, color=(0,0,0), align="left"):
    """Draw a block of text with proper wrapping and spacing"""
    fill(*color)
    font(font_name)
    fontSize(font_size)
    
    # Split text into lines that fit within the width
    words = text_content.split()
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_width = textSize(test_line)[0]
        
        if test_width <= width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
                current_line = word
            else:
                lines.append(word)  # Word too long, add anyway
    
    if current_line:
        lines.append(current_line)
    
    # Draw each line
    current_y = y
    for line in lines:
        text(line, (x, current_y))
        current_y -= line_height
    
    return current_y - 5  # Add some space after the block

def draw_section_divider(x, y, width):
    """Draw a subtle section divider"""
    stroke(*colors['light_gray'])
    strokeWidth(0.5)
    line((x, y), (x + width, y))
    stroke(None)
    return y - 20

# Start document
newPage(page_width, page_height)

# White background
fill(1, 1, 1)
rect(0, 0, page_width, page_height)

current_y = page_height - margins[0]

# TITLE AND HEADER
current_y = draw_text_block(
    "AI News for July 2025",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['title'], leading['title'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "For: The Barbarian Group | Date: July 29, 2025",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['body'], leading['body'],
    colors['medium_gray'], "left"
)

current_y -= 10

# INTRO PARAGRAPH
intro_text = """We checked 40+ X posts, 20+ news sources, 15 LinkedIn case studies, 10 TikTok creators, 10 Instagram showcases, and multiple Reddit threads for you. Estimated reading time saved (at 200wpm): 845 minutes. Total research cost: $0.40. It's worth looking at ChatGPT Agent's rocky launch, Midjourney's video democratization at $10/month, and the authentic Reddit verdict on Manus AI."""

current_y = draw_text_block(
    intro_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# Check if we need a new page
if current_y < 200:
    newPage(page_width, page_height)
    fill(1, 1, 1)
    rect(0, 0, page_width, page_height)
    current_y = page_height - margins[0]

# SECTION 1: AI TWITTER/X RECAP
current_y = draw_text_block(
    "🚀 AI Twitter/X Recap",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "Major Agent Platform Releases (The Good, The Bad, The Hype)",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

# OpenAI ChatGPT Agent content
chatgpt_text = """OpenAI's ChatGPT Agent Finally Ships: On July 17, OpenAI announced ChatGPT Agent, transforming their chatbot into an autonomous task executor. Initially for Pro subscribers, it promises "deep research" tools and browser control via "Operator" mode. Reception has been... mixed. While Reuters calls it a milestone, Actuia notes it's "far from an on-demand workforce" after just 12 hours in the wild. Use cases include crypto trading automation and research reports, but creative tasks remain a struggle."""

current_y = draw_text_block(
    chatgpt_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Manus AI content
manus_text = """The Manus AI "ChatGPT Killer" Narrative: Beta testers are going wild for Manus AI, calling it the "first general AI agent." @JulianGoldieSEO claims users are canceling ChatGPT subs after demos showing multi-browser control and autonomous website building. Free tier available now, with premium expected under $200/month. The hype is real, but it's still beta—treat claims of "ChatGPT killer" status with caution."""

current_y = draw_text_block(
    manus_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Abacus AI content
abacus_text = """Abacus AI's Steady Enterprise Play: While others chase hype, Abacus AI quietly dominates enterprise automation. Their $10/month "Super Assistant" builds SaaS apps and dashboards from prompts. Featured in Daily AI Agent News (July 24), it's positioned as the practical alternative. CEO @bindureddy's approach: focus on monitoring and running agents, not just chatting."""

current_y = draw_text_block(
    abacus_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Check for new page
if current_y < 200:
    newPage(page_width, page_height)
    fill(1, 1, 1)
    rect(0, 0, page_width, page_height)
    current_y = page_height - margins[0]

# Video Generation Revolution subsection
current_y = draw_text_block(
    "The Video Generation Revolution",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

midjourney_text = """Midjourney V1 Video Changes Everything: Launched June 18, enhanced throughout July, Midjourney's video model brings AI video to the masses at $10/month. July updates include:

• Seamless looping with --loop command
• Start/end frame control
• Direct Discord integration  
• 720p resolution "coming soon" (currently 480p, 24fps, 5-second clips)

The elephant in the room? Disney's plagiarism lawsuit, which could reshape content generation limits."""

current_y = draw_text_block(
    midjourney_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

runway_text = """Runway Maintains Pro Workflow Leadership: While Midjourney democratizes, Runway focuses on professional features—longer clips, better motion consistency. The emerging pattern: Midjourney for ideation → Runway for refinement."""

current_y = draw_text_block(
    runway_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Viral AI Content subsection
current_y = draw_text_block(
    "Viral AI Content & Platform Buzz",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

trending_text = """Top Trending Topics (July 2025):

1. AI + Astrology Goes Mainstream: @hotgirltarotsha's July predictions hit millions of views. Water signs warned about "toxic friends," fire signs promised "financial glow-ups." Why it matters: AI personalization meets human desire for meaning.

2. TikTok's "AI Gold Rush": Natural disaster clips generated by AI are hitting 100M+ views. Creators leverage AI for viral content at unprecedented scale. The platform's "Aura Farming" dance trend adds another layer of AI-human creative fusion.

3. The $50B Agent Economy Prediction: Market analysts project AI agents will create a $50B+ market by 2030. Agencies report 30-40% cost reductions already. @sidhant notes the shift from "AI as tool" to "AI as workforce."

4. Quantum + AI Convergence: Posts about solid-state batteries and quantum computing breakthroughs signal hardware catching up to software ambitions. "Agentic AI" becomes the buzzword of July."""

current_y = draw_text_block(
    trending_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Check for new page
if current_y < 150:
    newPage(page_width, page_height)
    fill(1, 1, 1)
    rect(0, 0, page_width, page_height)
    current_y = page_height - margins[0]

# Agency Transformation Insights
current_y = draw_text_block(
    "Agency Transformation Insights",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

agency_savings_text = """Real Cost Savings (Not Just Hype):
• Production costs: Down 50% with AI tools
• Campaign turnaround: 40% faster with automated workflows
• Manual design time: 60% reduction reported
• One agency case study: $500K+ annual savings from automated research

Success Patterns from Early Adopters:
1. AI as "creative partner" not replacement
2. Predictive analytics for trend forecasting working
3. Personalization at scale finally achievable
4. Human creativity + machine efficiency = winning combo"""

current_y = draw_text_block(
    agency_savings_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Technical Reality Checks
current_y = draw_text_block(
    "Technical Reality Checks",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

reality_text = """What's Actually Working:
• ChatGPT Agent for structured workflows (with human oversight)
• Abacus AI for enterprise automation
• Midjourney for rapid visual ideation
• Combo approaches (multiple tools in sequence)

What's Still Struggling:
• Fully autonomous creative work
• Complex video beyond 5 seconds
• True "set and forget" automation
• Cross-platform integration"""

current_y = draw_text_block(
    reality_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

# Water Cooler Talk
current_y = draw_text_block(
    "The Water Cooler Talk",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

debate_text = """Everyone's Debating:
• "Is ChatGPT Agent worth the Pro subscription?" (Mixed verdict)
• "Will Disney kill AI video generation?" (Lawsuit ongoing)
• "Can Manus AI really replace ChatGPT?" (Beta says maybe)
• "Are we in an AI bubble?" (Yes, but a productive one)

The Unspoken Concern: Forbes predicted agents would dominate 2025. They're right, but implementation remains messier than demos suggest."""

current_y = draw_text_block(
    debate_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# Continue with remaining sections...
# Check for new page
if current_y < 200:
    newPage(page_width, page_height)
    fill(1, 1, 1)
    rect(0, 0, page_width, page_height)
    current_y = page_height - margins[0]

# LINKEDIN PROFESSIONAL INSIGHTS
current_y = draw_text_block(
    "🔗 LinkedIn Professional Insights",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "Agency Case Studies & Professional Reviews",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

linkedin_text = """ChatGPT Agent in the Enterprise Wild: LinkedIn professionals are sharing mixed but revealing experiences with OpenAI's new agent. Medium case studies show 50% faster job placement rates through automated outreach. A B2B SaaS agency reported 3x boost in leads using agent-automated LinkedIn ad campaigns, with 40% higher conversion rates. But professionals warn about the "2% error rate" in complex multi-step processes—enough to erode trust in client-facing work.

Agency Transformation Numbers:
• Marketing agencies using ChatGPT Agent for competitive analysis: 35% ROI increase
• Recruiting agencies with AI-powered LinkedIn sourcing: 30% faster hiring cycles
• Digital agencies automating LinkedIn DMs and follow-ups: 25% uplift in client engagement
• Healthcare and legal agencies using agents for lead qualification: 2x efficiency gains

The Professional Verdict: Forbes highlights 5 prompts that "attract recruiters while you sleep," but Hacker News threads reveal the reality: "AI hype biting people" when agents misinterpret prospect profiles. Best practice emerging: Use agents for 80% automation, human oversight for the final 20%."""

current_y = draw_text_block(
    linkedin_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# Continue with remaining sections in next part...
# Save the current page and create continuation
saveImage("output/barbarian_ai_editorial_part1.pdf")
print("Part 1 generated: output/barbarian_ai_editorial_part1.pdf")

# Create part 2 with remaining content
newPage(page_width, page_height)
fill(1, 1, 1)
rect(0, 0, page_width, page_height)
current_y = page_height - margins[0]

# TIKTOK VIRAL AI TRENDS
current_y = draw_text_block(
    "🎵 TikTok Viral AI Trends",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "The AI Content Creator Revolution",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

tiktok_text = """Top AI Creators Exploding in July:
1. @AIArtWizard: "AI vs. Reality" challenges transforming user photos into surreal art—tens of millions of views per post
2. @ChatbotComedy: AI chatbot skits mimicking celebrity interviews, remixed thousands of times
3. @DeepfakeDaily: Ethical parodies sparking authenticity debates (NPR coverage)
4. @AIMusicMashup: AI-composed songs driving dance challenges with TikTok Shop integration

The "AI Gold Rush" Phenomenon: Natural disaster clips generated by AI hitting 100M+ views. Creators report 10x engagement when mixing AI with personal storytelling. The algorithm loves it: short-form series under 60 seconds with hooks like "What if AI redesigned your life?"

E-Commerce Integration Success: Beauty brands using AI-generated hauls for Korean skincare products seeing millions of views. Over 4 million TikTok Shop sellers now leverage AI for "shoppertainment" content. Key trend: AI voiceovers + trending sounds = viral discovery."""

current_y = draw_text_block(
    tiktok_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# INSTAGRAM AI ART SHOWCASES
current_y = draw_text_block(
    "📸 Instagram AI Art Showcases",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "Midjourney V1 Video Takes Over the Feed",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

instagram_text = """Agency Adoption Accelerating: Creative agencies like Wieden+Kennedy and Ogilvy are sharing AI-integrated projects on Instagram, including Midjourney video pilots from mid-2025. Agencies host virtual showcases via Instagram Live, demonstrating V1's enterprise potential for quick prototyping.

Top AI Art Accounts to Watch:
• @midjourney: Official V1 video teasers and community highlights
• @theaiart: Started posting short V1 videos in July—dreamlike sequences going viral
• @digitaldreamsai: Midjourney V1 experiments with immersive narratives
• @ai.storyteller: Character-driven worlds now featuring animated video clips

Trending Hashtags: #MidjourneyV1, #AIVideoArt, and #MidjourneyVideo showcase user-generated content with 5-10 second fantastical scenes. The Art Newspaper notes influencer power and AI tools are driving art world trends, with agencies collaborating for branded content."""

current_y = draw_text_block(
    instagram_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# Check for new page
if current_y < 200:
    newPage(page_width, page_height)
    fill(1, 1, 1)
    rect(0, 0, page_width, page_height)
    current_y = page_height - margins[0]

# REDDIT DEEP DIVE
current_y = draw_text_block(
    "🤖 Reddit Deep Dive: Authentic User Feedback",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

current_y = draw_text_block(
    "The Unfiltered Truth About AI Agents",
    margins[3], current_y, content_width,
    fonts['body_bold'], sizes['subsection'], leading['subsection'],
    colors['dark_gray'], "left"
)

reddit_text = """r/AI_Agents on Manus AI: "Is ChatGPT's dominance really coming to an end?" thread reveals mixed reactions. Users praise Manus for "feeling like having a junior assistant" in market research, compiling reports with sources faster than ChatGPT. But skeptics note: "ChatGPT is still better for creative writing; Manus shines in 'agentic' stuff but crashes sometimes."

r/ChatGPTCoding Developer Consensus: 133+ comments show Manus excelling at multi-file projects and backend systems where ChatGPT struggles. One developer: "Manus generated and debugged code snippets that ChatGPT couldn't handle, especially for complex builds." By July, stability improved but it's "Great for complex builds, ChatGPT wins for beginners."

AI Art Acceptance in 2025: r/midjourney discussions confirm AI art is more mainstream, with professionals using tools regularly. But ethical debates persist, especially around video authenticity and Disney's ongoing lawsuit.

Reddit's Verdict by Platform:
• Manus AI: 4-5/5 for innovation and agentic tasks
• ChatGPT: 4.5/5 for accessibility and everyday use
• Midjourney V1: Revolutionary but "still early stages"
• Privacy concerns with Chinese-origin Manus noted but no major issues reported"""

current_y = draw_text_block(
    reddit_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# ACTION ITEMS
current_y = draw_text_block(
    "💡 Action Items for The Barbarian Group",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

actions_text = """Try This Month:
1. Midjourney V1 Video ($10/month): Perfect for rapid concept visualization. Start with the --loop command for social content.
2. ChatGPT Agent Mode: Test on a low-stakes workflow automation project. Expect 70% success, plan for human finishing.
3. Abacus AI Trial: If you need dashboards or data viz, this beats manual work every time.

Watch These Trends:
• Manus AI's full launch (could disrupt if pricing stays competitive)
• Disney vs. Midjourney outcome (will set content generation precedents)
• "Agentic AI" implementations beyond chat interfaces

Skip For Now:
• GPT-5 rumors (August maybe, but who knows)
• Expensive "AI transformation" consultants (tools are democratized enough)
• Waiting for "perfect" AI (good enough is profitable now)"""

current_y = draw_text_block(
    actions_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# RESEARCH TRANSPARENCY
current_y = draw_text_block(
    "📊 Research Transparency",
    margins[3], current_y, content_width,
    fonts['heading'], sizes['section'], leading['section'],
    colors['black'], "left"
)

research_text = """Sources Analyzed:
• 20 X/Twitter posts on trending topics
• 19 news/blog sources on AI agents
• 15 LinkedIn professional case studies and reviews
• 10 TikTok viral AI creators and trends
• 10 Instagram AI art showcases and agency projects
• Multiple Reddit threads (r/AI_Agents, r/ChatGPTCoding, r/midjourney)
• Time period: July 1-29, 2025

Notable Sources:
• @hotgirltarotsha (viral astrology)
• @JulianGoldieSEO (Manus AI hype)
• @bindureddy (Abacus AI CEO)
• OpenAI Blog
• Reuters
• TechRadar Live Coverage"""

current_y = draw_text_block(
    research_text,
    margins[3], current_y, content_width,
    fonts['body'], sizes['body'], leading['body'],
    colors['black'], "left"
)

current_y = draw_section_divider(margins[3], current_y, content_width)

# CONCLUSION
conclusion_text = """The Punchline: July 2025 marks the shift from "AI that talks" to "AI that does"—but like teaching a teenager to drive, it works better with supervision. Agencies embracing the mess while competitors wait for perfection will own the next 18 months."""

current_y = draw_text_block(
    conclusion_text,
    margins[3], current_y, content_width,
    fonts['body_italic'], sizes['body'], leading['body'],
    colors['dark_gray'], "left"
)

# Save the complete document
saveImage("output/barbarian_ai_editorial_complete.pdf")
print("Complete editorial report generated: output/barbarian_ai_editorial_complete.pdf")
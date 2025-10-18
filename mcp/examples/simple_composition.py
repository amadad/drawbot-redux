"""
Simple example demonstrating compositional DrawBot design.

This shows how the system can build up a design from natural language descriptions,
layer by layer, allowing for iterative refinement.
"""

import asyncio
from fastmcp import Client


async def create_business_card():
    """Create a business card design compositionally."""
    
    client = Client("../drawbot_mcp.py")
    
    async with client:
        # Start a business card design
        await client.call_tool("start_design_session", {
            "session_id": "business_card",
            "width": 350,
            "height": 200,
            "description": "Modern minimalist business card"
        })
        
        # Layer 1: Background
        await client.call_tool("add_layer", {
            "session_id": "business_card",
            "layer_description": "Clean white background with subtle shadow",
            "layer_type": "background"
        })
        
        # Layer 2: Logo/Icon area
        await client.call_tool("add_layer", {
            "session_id": "business_card",
            "layer_description": "Geometric logo mark in top left corner, circular shape",
            "layer_type": "shape"
        })
        
        # Layer 3: Name
        await client.call_tool("add_layer", {
            "session_id": "business_card",
            "layer_description": "Name 'Jane Designer' in large bold type",
            "layer_type": "text"
        })
        
        # Layer 4: Title
        await client.call_tool("add_layer", {
            "session_id": "business_card",
            "layer_description": "Job title 'Creative Director' in smaller text below name",
            "layer_type": "text"
        })
        
        # Layer 5: Contact info
        await client.call_tool("add_layer", {
            "session_id": "business_card",
            "layer_description": "Contact details at bottom: email and phone, small and subtle",
            "layer_type": "text"
        })
        
        # Modify the logo to be more specific
        await client.call_tool("modify_layer", {
            "session_id": "business_card",
            "layer_index": 1,
            "modification": "Make the circle filled with a gradient from blue to purple"
        })
        
        # Compose with style hints
        result = await client.call_tool("compose_design", {
            "session_id": "business_card",
            "style_hints": "Minimalist, professional, good use of whitespace, modern typography"
        })
        
        print("Business card design composed!")
        print(f"Composition result: {result}")
        
        # The DrawBot expert sub-agent would generate code like:
        sample_code = """
# Business Card Design - Modern Minimalist
db.newPage(350, 200)

# Background
db.fill(1)
db.rect(0, 0, db.width(), db.height())

# Subtle shadow effect
db.fill(0, 0, 0, 0.05)
db.rect(2, -2, db.width(), db.height())

# Logo - Gradient circle
db.linearGradient(
    (30, db.height()-30), (60, db.height()-60),
    [(0.2, 0.4, 0.8), (0.6, 0.2, 0.8)]
)
db.oval(30, db.height()-60, 30, 30)

# Name
db.font("Helvetica-Bold", 24)
db.fill(0.1)
db.text("Jane Designer", (30, db.height()/2 + 10))

# Title
db.font("Helvetica", 12)
db.fill(0.4)
db.text("Creative Director", (30, db.height()/2 - 15))

# Contact info
db.font("Helvetica", 9)
db.fill(0.5)
db.text("jane@designstudio.com", (30, 30))
db.text("+1 (555) 123-4567", (30, 15))
"""
        
        # Execute the design
        result = await client.call_tool("execute_drawbot_code", {
            "code": sample_code,
            "session_id": "business_card",
            "output_name": "business_card.png",
            "sandbox": "local"
        })
        
        print(f"\nExecution result: {result}")
        
        # Iterate based on feedback
        await client.call_tool("iterate_design", {
            "session_id": "business_card",
            "feedback": "The gradient is nice but maybe too bold",
            "specific_changes": "Make the logo smaller and use a single color instead"
        })
        
        print("\nDesign iteration recorded for refinement")


if __name__ == "__main__":
    asyncio.run(create_business_card())
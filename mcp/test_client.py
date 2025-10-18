import asyncio
from fastmcp import Client


async def test_compositional_design():
    """Test the compositional DrawBot MCP server."""
    
    # Create client pointing to our MCP server
    client = Client("mcp/drawbot_mcp.py")
    
    async with client:
        print("=== Testing DrawBot Compositional Design System ===\n")
        
        # 1. Start a design session
        print("1. Starting design session...")
        result = await client.call_tool("start_design_session", {
            "session_id": "magazine_layout",
            "width": 800,
            "height": 1000,
            "description": "A magazine-style layout with modern typography"
        })
        print(f"Result: {result}\n")
        
        # 2. Add background layer
        print("2. Adding background layer...")
        result = await client.call_tool("add_layer", {
            "session_id": "magazine_layout",
            "layer_description": "Subtle gradient background from light gray to white",
            "layer_type": "background"
        })
        print(f"Result: {result}\n")
        
        # 3. Add headline layer
        print("3. Adding headline layer...")
        result = await client.call_tool("add_layer", {
            "session_id": "magazine_layout",
            "layer_description": "Large bold headline 'DESIGN SYSTEMS' at the top with generous spacing",
            "layer_type": "text"
        })
        print(f"Result: {result}\n")
        
        # 4. Add grid layout
        print("4. Adding grid layout layer...")
        result = await client.call_tool("add_layer", {
            "session_id": "magazine_layout",
            "layer_description": "Two-column grid layout below headline with 40px margins and 20px gutter",
            "layer_type": "element"
        })
        print(f"Result: {result}\n")
        
        # 5. Modify a layer
        print("5. Modifying headline layer...")
        result = await client.call_tool("modify_layer", {
            "session_id": "magazine_layout",
            "layer_index": 1,
            "modification": "Use Helvetica Bold, 72pt, in dark blue color"
        })
        print(f"Result: {result}\n")
        
        # 6. View current session state
        print("6. Viewing session state...")
        result = await client.call_tool("view_session", {
            "session_id": "magazine_layout"
        })
        print(f"Result: {result}\n")
        
        # 7. Compose the design
        print("7. Composing final design...")
        result = await client.call_tool("compose_design", {
            "session_id": "magazine_layout",
            "style_hints": "Clean, modern, professional with good visual hierarchy"
        })
        print(f"Result: {result}\n")
        
        # Note: The actual code generation would happen through the DrawBot sub-agent
        # For testing, let's create sample code
        sample_code = """
# Magazine Layout Design
db.newPage(800, 1000)

# Background gradient
db.linearGradient(
    (0, 0), (0, db.height()),
    [(0.95, 0.95, 0.95), (1, 1, 1)]
)
db.rect(0, 0, db.width(), db.height())

# Headline
db.font("Helvetica-Bold", 72)
db.fill(0.1, 0.2, 0.6)  # Dark blue
db.text("DESIGN SYSTEMS", (db.width()/2, db.height() - 100), align="center")

# Two-column grid
margin = 40
gutter = 20
col_width = (db.width() - 2 * margin - gutter) / 2

# Left column placeholder
db.fill(0.9)
db.rect(margin, 200, col_width, 600)

# Right column placeholder  
db.rect(margin + col_width + gutter, 200, col_width, 600)
"""
        
        # 8. Execute the code
        print("8. Executing DrawBot code...")
        result = await client.call_tool("execute_drawbot_code", {
            "code": sample_code,
            "session_id": "magazine_layout",
            "output_name": "magazine_layout.png",
            "sandbox": "local"  # Use local for testing
        })
        print(f"Result: {result}\n")
        
        # 9. List all sessions
        print("9. Listing all sessions...")
        result = await client.call_tool("list_sessions", {})
        print(f"Result: {result}\n")


if __name__ == "__main__":
    asyncio.run(test_compositional_design())
# DrawBot MCP Server - Compositional Design System

A Model Context Protocol (MCP) server that enables natural language-driven compositional design with DrawBot. This system allows you to build complex layouts iteratively through conversational interaction with a Claude sub-agent.

## Key Features

### 🎨 Compositional Design
- Build designs layer by layer using natural language
- Modify individual layers without affecting others
- Iterate on designs based on feedback
- Maintain design history and sessions

### 🤖 Claude Sub-agent Integration
- Specialized DrawBot expert agent
- Interprets natural language into DrawBot code
- Understands design principles and layout systems
- Provides intelligent suggestions and refinements

### 🔒 Secure Execution
- Sandboxed code execution using Dagger containers
- Code validation to prevent malicious operations
- Isolated environment for each execution
- Resource limits and timeouts

## Installation

```bash
# Install dependencies
uv install

# Or with pip
pip install fastmcp dagger-io drawbot-skia anthropic
```

## Usage

### 1. Start the MCP Server

```bash
# Using FastMCP CLI
fastmcp run mcp/drawbot_mcp.py

# Or directly with Python
python mcp/drawbot_mcp.py
```

### 2. Register with Claude Desktop

```bash
fastmcp install mcp/drawbot_mcp.py
```

### 3. Use with Claude

Once registered, you can interact with the DrawBot system through Claude:

```
You: Use the drawbot-expert to create a magazine layout with a bold headline and two columns

Claude: I'll help you create a magazine layout using the DrawBot compositional system. Let me start by setting up a design session and building it layer by layer.

[Claude will use the MCP tools to create the design]
```

## Compositional Workflow

### Starting a Session
```python
# Claude initiates a design session
await start_design_session(
    session_id="my_design",
    width=800,
    height=1000,
    description="Magazine layout"
)
```

### Adding Layers
```python
# Add background
await add_layer(
    session_id="my_design",
    layer_description="Gradient background from blue to white",
    layer_type="background"
)

# Add headline
await add_layer(
    session_id="my_design",
    layer_description="Large bold headline at top",
    layer_type="text"
)
```

### Modifying Layers
```python
# Refine specific layer
await modify_layer(
    session_id="my_design",
    layer_index=1,
    modification="Change color to dark red"
)
```

### Generating Code
```python
# Compose all layers into DrawBot code
await compose_design(
    session_id="my_design",
    style_hints="Modern, clean, professional"
)
```

## Natural Language Examples

### Basic Layout
"Create a poster with a centered title and grid of images below"

### Typography Focus
"Design a typographic composition with varying font sizes creating visual rhythm"

### Complex Composition
"Build a dashboard layout with header, sidebar navigation, and main content area with data visualization placeholders"

### Iterative Refinement
"Make the headline bigger and add more spacing between the columns"

## Architecture

```
mcp/
├── drawbot_mcp.py      # Main MCP server
├── sandbox/
│   ├── executor.py     # Sandboxed execution
│   └── __init__.py
├── resources/
│   └── drawbotdoc.md   # DrawBot documentation
└── test_client.py      # Test client

.claude/
└── agents/
    └── drawbot-expert.md  # Sub-agent definition
```

## Security

- All code execution happens in isolated containers
- Dangerous operations are blocked (file system access, network, etc.)
- Resource limits prevent infinite loops
- Output files are saved to designated directory only

## Testing

Run the test client to verify functionality:

```bash
python mcp/test_client.py
```

## Advanced Usage

### Custom Sandbox
```python
# Use Dagger for production
await execute_drawbot_code(
    code=generated_code,
    sandbox="dagger"
)

# Use local for development
await execute_drawbot_code(
    code=generated_code,
    sandbox="local"
)
```

### Session Management
```python
# View all sessions
sessions = await list_sessions()

# Export session for sharing
export = await export_session(
    session_id="my_design",
    include_history=True
)
```

## Contributing

The system is designed to be extensible:

1. Add new layer types in `drawbot_mcp.py`
2. Enhance sandbox security in `executor.py`
3. Improve sub-agent prompts in `drawbot-expert.md`
4. Add more design patterns and examples

## Future Enhancements

- [ ] Animation support
- [ ] Multi-page documents
- [ ] Design system templates
- [ ] Real-time preview
- [ ] Collaborative sessions
- [ ] Export to various formats
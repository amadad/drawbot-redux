# DrawBot (Redux)

DrawBot (Redux) builds on the Python branch of the powerful programmatic graphic software. The built-in graphics primitives support rectangles, ovals, (bezier) paths, polygons, text objects, colors, transparency and much more. You can program multi-page documents and stop-motion animations. Export formats include PDF, SVG, PNG, JPEG, TIFF, animated GIF and MP4 video.

### Installation

To install DrawBot as a Python module using [uv](https://github.com/astral-sh/uv):

1. Install uv:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Clone and setup:
    ```bash
    git clone https://github.com/amadad/drawbot-redux.git
    cd drawbot-redux
    uv venv
    source .venv/bin/activate
    uv install -e .
    ```

3. Required for GIF support:
    ```bash
    brew install gifsicle
    ```

4. For the Anthropic Design System:
    ```bash
    export ANTHROPIC_API_KEY="your-api-key"
    ```

## Projects

### Anthropic Design System
`anthro.py` is an AI-powered design reproduction system that:
- Uses Claude to analyze images and generate DrawBot code
- Uses prompt caching for DrawBot documentation to optimize responses
- Automatically converts visual designs into programmatic graphics
- Provides iterative refinement through AI critique
- Supports various output formats (PNG, GIF, PDF)
- Handles color, layout, typography, and complex visual elements

---

The original source code for [DrawBot](https://github.com/typemytype/drawbot) along with the [Mac app](http://www.drawbot.com/content/download.html) were created by Just van Rossum, Erik van Blokland, Frederik Berlaen.
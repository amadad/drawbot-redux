#!/usr/bin/env python3
"""
Simplified DrawBot Layout System
Build layouts from the bottom up with clear patterns
"""

try:
    from drawBot import *
    import drawBot as db
except ImportError:
    import drawBot as db
    from drawBot import *

class LayoutSystem:
    """Base layout system with grid and flow control"""
    
    def __init__(self, width=612, height=792, margin=72, columns=12, gutter=24):
        self.width = width
        self.height = height
        self.margin = margin
        self.columns = columns
        self.gutter = gutter
        
        # Calculate column width
        self.content_width = width - (2 * margin)
        self.content_height = height - (2 * margin)
        self.column_width = (self.content_width - (gutter * (columns - 1))) / columns
        
        # Current position tracking
        self.cursor_x = margin
        self.cursor_y = height - margin  # Start from top
        
    def grid_x(self, column, span=1):
        """Get x position for column (0-indexed)"""
        return self.margin + (column * (self.column_width + self.gutter))
    
    def grid_width(self, span):
        """Get width for spanning columns"""
        return (span * self.column_width) + ((span - 1) * self.gutter)
    
    def reset_cursor(self):
        """Reset to top-left of content area"""
        self.cursor_x = self.margin
        self.cursor_y = self.height - self.margin
    
    def move_cursor(self, dx=0, dy=0):
        """Move cursor relatively"""
        self.cursor_x += dx
        self.cursor_y += dy
    
    def next_line(self, line_height=20):
        """Move to next line"""
        self.cursor_x = self.margin
        self.cursor_y -= line_height


class TextBlock:
    """Handles text with proper measurement and flow"""
    
    @staticmethod
    def measure(text, font_name, font_size):
        """Measure text dimensions"""
        db.font(font_name, font_size)
        return db.textSize(text)
    
    @staticmethod
    def draw(text, x, y, width=None, font_name="Helvetica", font_size=12, color=(0,0,0)):
        """Draw text with optional width constraint"""
        db.fill(*color)
        db.font(font_name, font_size)
        
        if width:
            # Simple word wrapping
            words = text.split()
            lines = []
            current_line = []
            
            for word in words:
                test_line = " ".join(current_line + [word])
                test_width, _ = db.textSize(test_line)
                
                if test_width <= width:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(" ".join(current_line))
                        current_line = [word]
                    else:
                        lines.append(word)
            
            if current_line:
                lines.append(" ".join(current_line))
            
            # Draw lines
            line_height = font_size * 1.4
            for i, line in enumerate(lines):
                db.text(line, (x, y - (i * line_height)))
            
            return len(lines) * line_height
        else:
            db.text(text, (x, y))
            return font_size * 1.4


class Box:
    """Simple box primitive for layout"""
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, fill_color=None, stroke_color=None, stroke_width=1):
        """Draw the box"""
        if fill_color:
            db.fill(*fill_color)
            db.rect(self.x, self.y, self.width, self.height)
        
        if stroke_color:
            db.stroke(*stroke_color)
            db.strokeWidth(stroke_width)
            db.fill(None)
            db.rect(self.x, self.y, self.width, self.height)
    
    def inset(self, amount):
        """Return inset box"""
        return Box(
            self.x + amount,
            self.y + amount,
            self.width - (2 * amount),
            self.height - (2 * amount)
        )


class Stack:
    """Vertical stack layout"""
    
    def __init__(self, x, y, width, spacing=0):
        self.x = x
        self.y = y
        self.width = width
        self.spacing = spacing
        self.current_y = y
    
    def add_space(self, height):
        """Add vertical space"""
        self.current_y -= height
        return self.current_y
    
    def add_text(self, text, font_name="Helvetica", font_size=12, color=(0,0,0)):
        """Add text to stack"""
        height = TextBlock.draw(text, self.x, self.current_y, self.width, 
                                font_name, font_size, color)
        self.current_y -= (height + self.spacing)
        return height
    
    def add_box(self, height, fill_color=None, stroke_color=None):
        """Add box to stack"""
        box = Box(self.x, self.current_y - height, self.width, height)
        box.draw(fill_color, stroke_color)
        self.current_y -= (height + self.spacing)
        return box


class Row:
    """Horizontal row layout"""
    
    def __init__(self, x, y, width, height, spacing=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spacing = spacing
        self.current_x = x
    
    def add_column(self, width_ratio):
        """Add column with width as ratio of total"""
        col_width = (self.width * width_ratio) - self.spacing
        col = Stack(self.current_x, self.y + self.height, col_width, spacing=10)
        self.current_x += col_width + self.spacing
        return col


def create_simple_report():
    """Create a simple, well-structured report"""
    
    # Setup
    db.newPage(612, 792)
    db.fill(1, 1, 1)
    db.rect(0, 0, 612, 792)
    
    # Initialize layout system
    layout = LayoutSystem(width=612, height=792, margin=72, columns=12)
    
    # Header block
    header_box = Box(layout.grid_x(0), layout.cursor_y - 80, 
                     layout.grid_width(12), 80)
    header_box.draw(fill_color=(0.2, 0.3, 0.7))
    
    # Title in header
    db.fill(1, 1, 1)
    db.font("Helvetica-Bold", 32)
    db.text("Quarterly Report", (layout.margin + 20, layout.cursor_y - 50))
    
    layout.move_cursor(dy=-100)
    
    # Three metric cards in a row
    row = Row(layout.margin, layout.cursor_y, layout.content_width, 60, spacing=20)
    
    metrics = [("Revenue", "$2.4M"), ("Growth", "+23%"), ("Users", "1,247")]
    
    for i, (label, value) in enumerate(metrics):
        col = row.add_column(0.31)
        
        # Card background
        card = Box(col.x, col.current_y - 60, col.width, 60)
        card.draw(fill_color=(0.95, 0.95, 0.95))
        
        # Metric value
        db.fill(0.2, 0.3, 0.7)
        db.font("Helvetica-Bold", 24)
        db.text(value, (col.x + 10, col.current_y - 40))
        
        # Metric label
        db.fill(0.5, 0.5, 0.5)
        db.font("Helvetica", 10)
        db.text(label.upper(), (col.x + 10, col.current_y - 55))
    
    layout.move_cursor(dy=-80)
    
    # Main content in two columns
    left_col = Stack(layout.grid_x(0), layout.cursor_y, 
                     layout.grid_width(7), spacing=20)
    
    right_col = Stack(layout.grid_x(8), layout.cursor_y, 
                      layout.grid_width(4), spacing=20)
    
    # Left column content
    left_col.add_text("Executive Summary", "Helvetica-Bold", 18, (0.2, 0.3, 0.7))
    left_col.add_text(
        "This quarter showed exceptional performance across all key metrics. "
        "Revenue exceeded targets by 15%, driven by strong customer acquisition "
        "and improved retention rates. The team successfully launched three new "
        "product features that have been well-received by our user base.",
        "Helvetica", 11, (0.3, 0.3, 0.3)
    )
    
    left_col.add_space(20)
    left_col.add_text("Key Achievements", "Helvetica-Bold", 14, (0.2, 0.3, 0.7))
    
    achievements = [
        "• Launched mobile app with 10K downloads",
        "• Expanded to 3 new markets",
        "• Improved customer satisfaction to 94%",
        "• Reduced churn rate by 30%"
    ]
    
    for achievement in achievements:
        left_col.add_text(achievement, "Helvetica", 10, (0.3, 0.3, 0.3))
    
    # Right column - simple bar chart
    right_col.add_text("Monthly Revenue", "Helvetica-Bold", 14, (0.2, 0.3, 0.7))
    right_col.add_space(10)
    
    # Simple bars
    months = [("Oct", 0.7), ("Nov", 0.85), ("Dec", 0.9)]
    bar_height = 100
    bar_width = right_col.width / 3 - 10
    
    for i, (month, value) in enumerate(months):
        x = right_col.x + (i * (bar_width + 10))
        h = bar_height * value
        
        # Bar
        db.fill(0.2, 0.3, 0.7, 0.8)
        db.rect(x, right_col.current_y - bar_height, bar_width, h)
        
        # Label
        db.fill(0.5, 0.5, 0.5)
        db.font("Helvetica", 9)
        db.text(month, (x + 5, right_col.current_y - bar_height - 15))
    
    # Footer
    db.stroke(0.8, 0.8, 0.8)
    db.strokeWidth(1)
    db.line((layout.margin, 50), (layout.width - layout.margin, 50))
    
    db.fill(0.6, 0.6, 0.6)
    db.font("Helvetica", 8)
    db.text("Generated with DrawBot Layout System", (layout.margin, 35))
    
    # Save
    db.saveImage("output/reports/simple_structured_report.pdf")
    print("Generated: output/reports/simple_structured_report.pdf")


if __name__ == "__main__":
    create_simple_report()
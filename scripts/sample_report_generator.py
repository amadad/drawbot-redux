#!/usr/bin/env python3
"""
Sample DrawBot Report Generator
Demonstrates using DrawBot to create professional PDF reports from data
"""

try:
    # Try to import drawbot-skia for cross-platform support
    from drawBot import *
    import drawBot as db
except ImportError:
    # Fall back to native DrawBot on macOS
    try:
        import drawBot as db
        from drawBot import *
    except ImportError:
        print("Error: Neither drawbot-skia nor native DrawBot is available")
        print("Please install: pip install drawbot-skia")
        exit(1)
import json
from datetime import datetime
import random

class ModernReportGenerator:
    def __init__(self):
        # Design system
        self.page_width = 612  # Letter size
        self.page_height = 792
        self.margin = 72
        self.column_gap = 24
        self.baseline = 12
        
        # Colors
        self.colors = {
            'primary': (0.2, 0.4, 0.8),      # Blue
            'secondary': (0.95, 0.95, 0.95),  # Light gray
            'accent': (0.9, 0.3, 0.3),       # Red
            'text': (0.1, 0.1, 0.1),         # Dark gray
            'light': (0.98, 0.98, 0.98)      # Almost white
        }
        
        # Typography
        self.fonts = {
            'headline': ('Helvetica-Bold', 36),
            'subhead': ('Helvetica', 24),
            'body': ('Georgia', 11),
            'caption': ('Helvetica', 9),
            'data': ('Courier', 10)
        }
    
    def create_header(self, title, subtitle=None, page_num=1):
        """Create report header with title and metadata"""
        # Background accent
        db.fill(*self.colors['primary'])
        db.rect(0, self.page_height - 120, self.page_width, 120)
        
        # Title
        db.fill(1, 1, 1)  # White
        db.font(self.fonts['headline'][0], self.fonts['headline'][1])
        db.text(title, (self.margin, self.page_height - 80))
        
        # Subtitle
        if subtitle:
            db.font(self.fonts['subhead'][0], 18)
            db.fill(0.9, 0.9, 0.9)
            db.text(subtitle, (self.margin, self.page_height - 100))
        
        # Date and page
        db.font(self.fonts['caption'][0], self.fonts['caption'][1])
        db.fill(1, 1, 1, 0.7)
        db.text(datetime.now().strftime("%B %d, %Y"), 
             (self.margin, self.page_height - 35))
        db.text(f"Page {page_num}", 
             (self.page_width - self.margin - 50, self.page_height - 35))
    
    def create_data_visualization(self, data, viz_type='bar'):
        """Create data visualization component"""
        viz_width = self.page_width - (2 * self.margin)
        viz_height = 200
        y_position = 400
        
        if viz_type == 'bar':
            # Bar chart
            bar_width = viz_width / len(data)
            max_value = max(data.values())
            
            for i, (label, value) in enumerate(data.items()):
                bar_height = (value / max_value) * viz_height
                x = self.margin + (i * bar_width)
                
                # Bar
                db.fill(*self.colors['primary'], 0.8)
                db.rect(x + 10, y_position, bar_width - 20, bar_height)
                
                # Value label
                db.fill(*self.colors['text'])
                db.font(self.fonts['data'][0], self.fonts['data'][1])
                db.text(str(value), (x + bar_width/2 - 10, y_position + bar_height + 10))
                
                # Category label
                db.font(self.fonts['caption'][0], self.fonts['caption'][1])
                db.text(label, (x + bar_width/2 - 20, y_position - 20))
    
    def create_text_section(self, heading, content, y_position):
        """Create a text content section"""
        # Heading
        db.fill(*self.colors['primary'])
        db.font(self.fonts['subhead'][0], self.fonts['subhead'][1])
        db.text(heading, (self.margin, y_position))
        
        # Content
        db.fill(*self.colors['text'])
        db.font(self.fonts['body'][0], self.fonts['body'][1])
        
        # Text with manual positioning (drawbot-skia compatibility)
        db.text(content[:200], (self.margin, y_position - 40))
        
        return y_position - 120
    
    def create_key_metrics(self, metrics, y_position):
        """Create key metrics cards"""
        card_width = (self.page_width - 2*self.margin - 2*self.column_gap) / 3
        card_height = 80
        
        for i, (label, value) in enumerate(metrics.items()):
            x = self.margin + i * (card_width + self.column_gap)
            
            # Card background
            db.fill(*self.colors['light'])
            db.rect(x, y_position, card_width, card_height)
            
            # Metric value
            db.fill(*self.colors['primary'])
            db.font(self.fonts['headline'][0], 28)
            db.text(str(value), (x + 20, y_position + 45))
            
            # Metric label
            db.fill(*self.colors['text'])
            db.font(self.fonts['caption'][0], self.fonts['caption'][1])
            db.text(label.upper(), (x + 20, y_position + 20))
        
        return y_position - card_height - 40
    
    def generate_sample_report(self):
        """Generate a complete sample report"""
        # Page 1
        db.newPage(self.page_width, self.page_height)
        db.fill(1, 1, 1)  # White background
        db.rect(0, 0, self.page_width, self.page_height)
        
        # Header
        self.create_header("Quarterly Performance Report", "Q4 2024 Analysis")
        
        # Key Metrics
        metrics = {
            "Revenue": "$2.4M",
            "Growth": "+23%",
            "Customers": "1,247"
        }
        y_pos = self.create_key_metrics(metrics, 650)
        
        # Executive Summary
        summary = """This quarter showed exceptional growth across all key metrics. 
Revenue exceeded projections by 15%, driven primarily by new customer 
acquisition and improved retention rates. Market expansion into three 
new regions contributed significantly to overall performance."""
        
        y_pos = self.create_text_section("Executive Summary", summary, 520)
        
        # Data Visualization
        monthly_data = {
            "Oct": 750000,
            "Nov": 820000,
            "Dec": 830000
        }
        self.create_data_visualization(monthly_data, 'bar')
        
        # Footer line
        db.stroke(*self.colors['secondary'])
        db.strokeWidth(1)
        db.line((self.margin, 50), (self.page_width - self.margin, 50))
        
        # Save the report
        db.saveImage("output/reports/sample_quarterly_report.pdf")
        print("Report generated: output/reports/sample_quarterly_report.pdf")

if __name__ == "__main__":
    # Create output directory
    import os
    os.makedirs("output/reports", exist_ok=True)
    
    # Generate report
    generator = ModernReportGenerator()
    generator.generate_sample_report()
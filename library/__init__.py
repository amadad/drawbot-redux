"""
DrawBot Design Library
======================
A collection of design systems, foundations, and components for DrawBot.
"""

import sys
import os

def import_drawbot():
    """
    Import the local DrawBot module by adding the project root to Python path.
    Returns the drawBot module or raises ImportError if not found.
    """
    # Get the project root (3 levels up from this file)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Add to Python path if not already there
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    try:
        import drawBot as db
        return db
    except ImportError as e:
        raise ImportError(f"Could not import DrawBot: {e}. Make sure you're running from the project root.")

# Convenience function to get DrawBot
def get_drawbot():
    """Get the DrawBot module, importing it if necessary."""
    return import_drawbot() 
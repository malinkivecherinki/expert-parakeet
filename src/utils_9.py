#!/usr/bin/env python3
"""
File utility functions.
"""

import os
from pathlib import Path

def read_file(filepath):
    """Read file contents."""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

def file_exists(filepath):
    """Check if file exists."""
    return os.path.exists(filepath)


"""
Expert Parakeet - Code Refactoring
"""

from typing import List, Dict, Optional

def optimize_algorithm(data: List[Dict]) -> List[Dict]:
    """Optimized version with better performance"""
    return [
        {**item, 'processed': True}
        for item in data
        if item.get('active', True)
    ]

def extract_metadata(obj: Dict) -> Optional[Dict]:
    """Extract metadata with type hints"""
    if not isinstance(obj, dict):
        return None
    
    return {
        'id': obj.get('id'),
        'timestamp': obj.get('timestamp'),
        'version': obj.get('version', '1.0.0')
    }

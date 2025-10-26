#!/usr/bin/env python3
"""
CodeAnalyzer - Static code analysis tool for multiple languages.
"""

import re
from pathlib import Path
from typing import Dict, List

class CodeAnalyzer:
    """Analyze code files for various metrics."""
    def __init__(self):
        self.results = {}
    
    def analyze_file(self, filepath: str) -> Dict:
        """Analyze a single code file."""
        path = Path(filepath)
        if not path.exists():
            return {"error": "File not found"}
        
        content = path.read_text()
        
        # Count lines
        lines = content.split('\n')
        total_lines = len(lines)
        code_lines = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        comment_lines = len([l for l in lines if l.strip().startswith('#')])
        
        # Count functions/classes
        functions = len(re.findall(r'def\s+\w+', content))
        classes = len(re.findall(r'class\s+\w+', content))
        
        return {
            "file": str(path),
            "total_lines": total_lines,
            "code_lines": code_lines,
            "comment_lines": comment_lines,
            "functions": functions,
            "classes": classes
        }
    
    def analyze_directory(self, directory: str, extensions: List[str] = ['.py']) -> List[Dict]:
        """Analyze all files in a directory."""
        results = []
        path = Path(directory)
        
        for ext in extensions:
            for filepath in path.rglob(f'*{ext}'):
                results.append(self.analyze_file(str(filepath)))
        
        return results

if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    print("CodeAnalyzer initialized")

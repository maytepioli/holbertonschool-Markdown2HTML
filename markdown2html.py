#!/usr/bin/env python3
"""
Converts a Markdown file to HTML.
"""

import sys
import os

def main():
    # Check if there are at least 2 arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)
    # Read Markdown content
    try:
        with open(md_file, 'r') as f:
            markdown_text = f.read()
    except Exception as e:
        print(f"Error reading {md_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML using the markdown module
    try:
        import markdown
        html_output = markdown.markdown(markdown_text)
    except ImportError:
        print("Missing markdown module. Install it with: pip install markdown", file=sys.stderr)
        sys.exit(1)

    # Write HTML output
    try:
        with open(html_file, 'w') as f:
            f.write(html_output)
    except Exception as e:
        print(f"Error writing {html_file}: {e}", file=sys.stderr)
        sys.exit(1)
    # If everything went fine, exit with code 0 and print nothing
    sys.exit(0)

if __name__ == "_main_":
    main()
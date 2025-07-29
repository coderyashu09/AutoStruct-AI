# file_parser.py

import re

def clean_filename(name):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', name).strip()

def parse_structure(raw_text):
    lines = raw_text.splitlines()
    paths = []
    stack = []

    for line in lines:
        if not line.strip():
            continue

        # Detect indentation based on special characters
        depth = line.count('│') + line.count('    ')

        # Remove ├── └── │
        name = re.sub(r'[│├└─]+', '', line).strip()
        name = clean_filename(name)

        # Update stack to current depth
        stack = stack[:depth] + [name]

        # Join path and add
        full_path = '/'.join(stack)
        paths.append(full_path)

    return paths

# main.py

import os
from file_parser import parse_structure
from file_creator import create_structure

def normalize_text(text):
    # Replace corrupted characters (in case of bad copy-paste)
    replacements = {
        'â”œâ”€â”€': '├──',
        'â””â”€â”€': '└──',
        'â”‚': '│',
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text

def main():
    file_path = input("Enter path to structure .txt file: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        raw_text = normalize_text(f.read())

    drive_letter = input("Enter drive letter (C, D, E): ").strip().upper()
    root_name = input("Enter root folder name: ").strip()

    base_path = os.path.join(f"{drive_letter}:\\", root_name)

    structure = parse_structure(raw_text)
    create_structure(base_path, structure)

    print(f"\n✅ Folder and file structure created at: {base_path}")

if __name__ == "__main__":
    main()

import os

def create_structure(base_path, paths):
    for relative_path in paths:
        full_path = os.path.join(base_path, relative_path.replace('/', os.sep))
        if '.' in os.path.basename(full_path):  # File
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(full_path, 'w').close()
        else:  # Folder
            os.makedirs(full_path, exist_ok=True)

import os
import shutil
import sys
from pathlib import Path
FILE_CATEGORIES = {
    'PDF': ['.pdf'],
    'RAR': ['.rar'],
    'ZIP & Archives': ['.zip', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz', '.cab'],
    'Word Documents': ['.doc', '.docx', '.odt', '.rtf'],
    'Excel Spreadsheets': ['.xls', '.xlsx', '.ods', '.csv'],
    'PowerPoint': ['.ppt', '.pptx', '.odp'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.ico', '.heic', '.raw', '.psd', '.ai', '.eps'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.mid', '.midi'],
    'Executables & Installers': ['.exe', '.msi', '.apk', '.app', '.dmg', '.deb', '.rpm', '.bin'],
    'Code & Scripts': ['.py', '.java', '.js', '.html', '.htm', '.css', '.cpp', '.c', '.cs', '.php', '.swift', '.go', '.rb', '.sh', '.bat', '.ps1', '.json', '.xml', '.yaml', '.yml', '.sql'],
    'Text Files': ['.txt', '.md', '.log'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
    '3D & Design': ['.blend', '.obj', '.fbx', '.stl', '.dwg', '.dxf', '.fig', '.sketch'],
    'Databases': ['.db', '.sqlite', '.sqlite3', '.mdb', '.accdb'],
    'E-Books': ['.epub', '.mobi', '.azw3'],
    'Torrents': ['.torrent'],
    'Disc Images': ['.iso', '.img', '.vcd']
}

def organize_files():
    base_dir = Path.cwd()
    script_name = Path(sys.argv[0]).name

    extension_mapping = {}
    for folder_name, extensions in FILE_CATEGORIES.items():
        for ext in extensions:
            extension_mapping[ext] = folder_name

    # Iterate through all items in the current directory
    for item in base_dir.iterdir():
        # Skip directories, hidden files, and the python script itself
        if item.is_dir() or item.name.startswith('.') or item.name == script_name:
            continue
            
        file_ext = item.suffix.lower()
        
        # If the file has no extension at all, group it in an 'Others' folder
        if not file_ext:
            target_folder_name = 'Others'
        else:
            # If extension is in our dataset, use the mapped folder.
            # FALLBACK: If a rare data type isn't in the dataset (e.g., .xyz), 
            # it automatically creates a folder named after the extension (e.g., 'XYZ').
            target_folder_name = extension_mapping.get(file_ext, file_ext.replace('.', '').upper())
            
        target_folder = base_dir / target_folder_name
        
        # Create the folder if it doesn't already exist
        target_folder.mkdir(exist_ok=True)
        
        # Determine the destination path
        destination_path = target_folder / item.name
        
        # Safety mechanism: Prevent overwriting if a file with the same name already exists in the folder
        if destination_path.exists():
            counter = 1
            while True:
                new_name = f"{item.stem} ({counter}){item.suffix}"
                destination_path = target_folder / new_name
                if not destination_path.exists():
                    break
                counter += 1
                
        # Move the file to its designated folder
        try:
            shutil.move(str(item), str(destination_path))
            print(f"Moved: {item.name} -> {target_folder_name}/")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

if __name__ == '__main__':
    print(f"Organizing files in: {Path.cwd()}\n")
    organize_files()
    print("\nFile organization complete!")
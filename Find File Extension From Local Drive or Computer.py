import os
from tqdm import tqdm

def find_files_with_extensions(root_dir, extensions):
    found_files = []
    for dirpath, _, filenames in tqdm(os.walk(root_dir), desc="Searching files"):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() in extensions:
                found_files.append(os.path.join(dirpath, filename))
    return found_files

if __name__ == "__main__":
    root_directory = r"d:"  # Change this to the directory you want to search
    file_extensions = [".mp4", ".mp3", ".ts", ".wmv", ".zip", ".mkv", ".rar"]
    
    found_files = find_files_with_extensions(root_directory, file_extensions)
    
    if found_files:
        print("Found files:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No files found with specified extensions.")

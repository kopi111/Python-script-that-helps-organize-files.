import os
import shutil

# Get the path to your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create a dictionary to store the extensions and their corresponding folder names
extension_to_folder = {
    ".txt": "Text Files",
    ".docx": "Word Documents",
    ".pdf": "PDFs",
    ".jpg": "JPEG Images",
    ".png": "PNG Images",
    ".mp4": "Video Files",
    ".mp3": "Audio Files",
    ".xlsx": "Excel Files",
    ".psd": "Photoshop Files",
    ".py": "Python Files",
    ".html": "HTML Files",
    ".css": "CSS Files",
    ".js": "JavaScript Files",
    ".cpp": "C++ Files",
    ".c": "C Files",
    ".rar" : "Rar Files",
    "pptxn":"Power Point"

    # Add more extensions and folder names as needed
}


# Move the files to their respective folders
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1]
        folder_name = extension_to_folder.get(extension, "Unknown Files")
        if folder_name != "Unknown Files":
            folder_path = os.path.join(desktop_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, folder_path)
            print(f"Moved {filename} to {folder_name} folder.")
        else:
            folder_path = os.path.join(desktop_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, folder_path)
            print(f"Moved {filename} to {folder_name} folder.")
            
# Remove the empty folders
for folder_name in extension_to_folder.values():
    folder_path = os.path.join(desktop_path, folder_name)
    if os.path.exists(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)
        print(f"Removed {folder_name} folder.")

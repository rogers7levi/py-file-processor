import os
import shutil

input_folders = "input_files"
text = "Text"
images = "Images"
csv = "csv"
path = "./"
files = os.listdir(input_folders)

print(f"files in folder: {files}")
#files = [file for file in files if not file.startswith(".")]
#print(f"file after filtering: {files}")


os.makedirs(text, exist_ok=True)
os.makedirs(images, exist_ok=True)
os.makedirs(csv, exist_ok=True)

print(f"files that need processing: {files}")

for file in files:
    file_path = os.path.join(input_folders, file)
    
    _, extension = os.path.splitext(file)
extension = extension.lower()
            

print(f"Processing: {file} (Full Path: {file_path})")

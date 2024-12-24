import os
import shutil

input_folders = "input_files"
text = "Text"
images = "Images"
csv = "csv"
path = "./"
files = os.listdir(input_folders)

if not files: 
    print("No files to process")

    print(f"file in folder: {files}")


def struc(file, file_path, extension):
    print(f"ext being proccessed: {extension}")
    if extension == '.txt':
        shutil.move(file_path, os.path.join(text, file))
        print(f"Moved {file} to {text}")
    elif extension == '.csv':
        shutil.move(file_path, os.path.join(csv, file))
        print(f"Moved {file} to {csv}")
    elif extension == '.jpeg':
        shutil.move(file_path, os.path.join(images, file))
        print(f"Moved {file} to {images}")
    else:
        print(f"Unknown file type: {file} cannot move")
        
        
for file in files:
    file_path = os.path.join(input_folders, file)
        
    _, extension = os.path.splitext(file)
    extension = extension.lower()
        

    struc(file , file_path, extension)


import os
import subprocess 
import sys

if len(sys.argv) > 1:
    path= sys.argv[1]
else:
    path = "."


walk_data=os.walk(path)
files_list = []

for root, dirs, files in (walk_data):
    for file in files:
        try:
            full_path = os.path.join(root,file)
            size = os.path.getsize(full_path)
            print(f"File name is {full_path} and it's size is {size/1024:.2f}")
            files_list.append((full_path,size))
        except (FileNotFoundError, PermissionError):
            print(f"Skipping file {full_path}")

#Sorting using lambda

files_list.sort(key = lambda x: x[1], reverse=True)

for files, size in files_list[:5]:
    print(f"File is {files} and size is {size/(1024*1024):.2f} MB")

#def list_files(given_path):


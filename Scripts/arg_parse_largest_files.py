"""
This script:
    - Accepts a directory path using --path
    - Accepts how many top files to show using --top
    - Lists the top N largest files
"""




import os
import argparse

parser = argparse.ArgumentParser(description="List top N largest files in a directory")
parser.add_argument('--path', type=str, default='.', help="Directory to scan")
parser.add_argument('--top', type=int, default=5, help="Number of top largest files to show")
parser.add_argument('--unit', choices=['bytes','kb','mb'], default='mb', help="Unit to display file sizes")
parser.add_argument('--min-size', type=int, default=0, help="Minimum file size")
args=parser.parse_args()


file_details = []

for root, dirs, files in os.walk(args.path):
    for file in files:
        full_path = os.path.join(root,file)
        if not os.path.isfile(full_path):
            continue
        try:
            size = os.path.getsize(full_path)
            file_details.append((full_path,size))
        except (FileNotFoundError, PermissionError):
            continue


#Sorting the file

file_details.sort(key=lambda x:x[1], reverse=True)

#Prininting top N files

for path,size in file_details[:args.top]:
    if args.unit == 'kb':
        display_size = size/1024
        label = 'KB'
    elif args.unit == 'bytes':
        display_size = size
        lable = 'bytes'
    else:
        display_size = size /(1024*1024)
        label = 'MB'


    print(f"File {path} has size {display_size:.2f} {label}")


for path, size in file_details:
    if size < args.min_size:
        print (f"These are the files smaller than {file}, {args.min_size}, File size is {size}")

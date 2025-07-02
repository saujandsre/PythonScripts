#Write a script that loops over 5 filenames and prints whether each exists if they do prinbt size. 


import os 


file_path="/home/saujan/Google/PythonScripts/Scripts/"

filename=["27June.py","28June.py","29June.py","30June.py","1July.py"]

for file in filename:
    fullpath = os.path.join(file_path,file)
    if os.path.isfile(fullpath):
        size = os.path.getsize(fullpath)
        print(f"Size of file {file} is {size/1024:.2f} KB")
    else:
        print(f"This file doesn't exist here {file}")





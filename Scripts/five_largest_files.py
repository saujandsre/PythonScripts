"""
This script does the following:
    1. Walks through a given directory
    2. Finds all files recursively
    3. Collects their sizes
    4. Sorts by size (descending)
    5. Prints the top 5 largest files in readable format
    """


import os
import sys


if len(sys.argv) > 1:
    path=sys.argv[1]
else:
    path = "."

walk_data=os.walk(path)

def walk_dir(walk_data):
    try:
        file_details=[]
        for root, dirs, files in (walk_data):
            for file in files:
                full_path=os.path.join(root,file)
                if not os.path.isfile(full_path):
                    continue
                size=os.path.getsize(full_path)
                file_details.append((full_path,size))

        #Sorting the list now

        file_details.sort(key = lambda x : x[1], reverse=True)

        print("Top largest  files are")
        for file,size in file_details[:5]:
            print(f"{file} : {size/(1024*1024):.2f} MB")
    except Exception as e:
        print(e)





if __name__ == "__main__":
    print(walk_dir(walk_data))



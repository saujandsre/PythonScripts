import os

file_path="/home/saujan"
files = os.listdir(file_path)
file_sizes = []

for file in files:
    if file.startswith('.'):
        continue
    
    #Listing only regular files
    full_path = os.path.join(file_path, file)
    if os.path.isfile(full_path):
       size = os.path.getsize(file) 
       print (f"File : {file} has size{size}")
       file_sizes.append((file,size))


print("Top 3 files here are below:")
file_sizes.sort(key=lambda x: x[1], reverse=True)
for file,size in file_sizes[:3]:
    print(f"File {file} is size {size}")

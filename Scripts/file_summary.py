import os


filenames = ['file_info.py','system_info.py','top_output.txt']

#Check if file exists or not

for files in filenames:
    exists = os.path.exists(files)
    if exists:
        sizeinKb=os.path.getsize(files)
        print ("Size : ",  sizeinKb)
        print ("Files exists")
    else:
        size=0

permissions=['-rw-rw-r--',
             '-rw-rw-r--',
             '-rw-rw-r--']

print (permissions)

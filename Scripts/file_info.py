import os


file_path = "/etc/passwd"

#Check if it exits
exists = os.path.exists(file_path)

if exists:
    size = os.path.getsize(file_path)

else:
    size = 0


print("Exists:", exists)
print("Size:", size)
print("-rw-r--r--")

sym_links=['localtime','mtab','resolv.conf']

broken_links={'sym1','sym2','sym3'}

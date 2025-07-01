import os
file_path="/home/saujan"
files=os.listdir(file_path)

for file in files:
    if file.startswith('.'):
        continue

    full_path=os.path.join(file_path,file)
    if os.path.isfile(full_path):
        print(f"Found: {file}")



#Counts number of txt files
def count_txt_files(path):
    txt_files=os.listdir(path)
    file_count = 0
    for file in txt_files:
        if file.endswith(".txt"):
           file_count += 1

    return file_count


def count_lines(file_path):
    line_count = 0
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line_count += 1
    return line_count


print(count_txt_files("/home/saujan/Google/Scripts"))

print("Number of lines in /var/log/syslog is :", count_lines("/var/log/syslog"))

#Step 2 
# Count how many lines contain the keyword
def count_lines_with_keyword(file_path, keyword):
    keyword_count = 0
    with open (file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if keyword in line:
                keyword_count += 1
    return keyword_count




file_path="/home/saujan/Google/Scripts/natureEssay.txt"
keyword="nature"


print(count_lines_with_keyword(file_path,keyword))

#Print the filenames of the 3 largest .log files.


log_path="/var/log"
logfiles=os.listdir(log_path)
log_file_sizes=[]

for file in logfiles:
    full_path=os.path.join(log_path, file)
    if file.endswith('.log') and os.path.isfile(full_path):
        size = os.path.getsize(full_path)
        log_file_sizes.append((file,size))


print ("Top 3 files are listed below")
log_file_sizes.sort(key=lambda x: x[1], reverse=True)
for file,size in log_file_sizes[:3]:
    print(f"File {file} has size {size/1024:2f} KB")





import os
import subprocess



#Task 1 : Basic command execution

#Using os.system
#os.system("ls -lh")

#Using subprocess
subprocess.run(["ls","-lh"])


#Task 2 : Capture and use command ouput

output = subprocess.check_output(["df","-lh"], text=True)
for line in output.strip().split("\n"):
    print(line)


#Task 3 : Run free -h extract just meme info 

mem_usage=subprocess.check_output(["free","-h"], text=True)

for mem_line in mem_usage.strip().split("\n"):
    if mem_line.startswith("Mem:"):
        print(mem_line)
        parts = mem_line.split()
        first = parts[0]
        total = parts[1]
        used = parts[2]
        print(f"Memory used:  {used} / {total}")



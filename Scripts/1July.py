import csv
import subprocess
import os


def openFile(file_path):
    output=[]
    user_with_shells=0
    if not os.path.isfile(file_path):
        print("Not a valid file")

    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) < 7:
                    continue
                shell = parts[6]
                if shell in ("/usr/sbin/nologin, /bin/false"):
                    continue
                output.append({
                     'username' : parts[0],
                     'shell' : shell
                    })
        print("There are ", len(output) , "users with shell")
    except Exception as e:
        print(f"There is an issue {e}")

    return output

def save_to_csv(output, csv_path="users_and_Shells.csv"):
    with open (csv_path, "w", encoding="utf-8") as f:
        f.write("username,shell\n")
        for entry in output:
            f.write(f"{entry['username']},{entry['shell']}\n")


if __name__== "__main__":
    users = (openFile("/etc/passwd"))
    if users:
        save_to_csv(users) 
        subprocess.run(["cat" , "/home/saujan/Google/PythonScripts/Scripts/users_and_Shells.csv"])

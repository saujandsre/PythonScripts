import os
import subprocess


def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout



if __name__ == "__main__":
    with open("system_stats.txt", "w") as f:
        f.write("===Disk Usage (df-h) ===\n")
        f.write(run_command(["df", "-h"]))
        f.write("\n\n===Memory Usage (free -m) ===\n")
        f.write(run_command(["free","-m"]))


    print("All outputs saved")

print("Using cat now")
subprocess.run(["cat" , "/home/saujan/Google/PythonScripts/Scripts/system_stats.txt"])

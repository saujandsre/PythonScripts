import os 

#Log line counter, Opens a file ingores empty lines and counts total lines



def count_lines(file_path):
    files = os.listdir(file_path)
    for file in files:
        full_path = os.path.join(file_path, file)
        line_counter = 0

        if not os.path.isfile(full_path):
            continue

        try:
            with open (full_path, 'r', encoding="utf-8") as f:
                for line in f:
                   if line.strip():
                      line_counter += 1
            print(f"{file} has : {line_counter} lines")
        except (UnicodeDecodeError, OSError):
                print(f"File {file} is not a valid file.")

if __name__ == "__main__":
    count_lines("/var/log/")




import os


#File Not found handling
def safe_line_count(file_path):
    line_counter = 0
    try:
        with open (file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_counter += 1
   # except FileNotFoundError:
    #    print (f"File not found {file_path}")
    except Exception as e:
        print(f"An error occurred : {e}")


    return line_counter

def bad_data_validator(file_path):
    line_Number = 0
    clean_data=[]
    try:    
        with open(file_path, 'r' , encoding='utf-8') as file:
            next(file)
            for line in file:
                name, age = line.strip().split(',')
                if name and not name.isdigit() and age.isdigit():
                    clean_data.append({"name":name, "age":int(age)})
                    line_Number += 1
    except Exception as e:
         print(f"Error: {e}")
    return clean_data

if __name__ == "__main__":
    print(safe_line_count("/home/saujan/Google/PythonScripts/Scripts/Files/os-release.txt"))
    print(bad_data_validator("/home/saujan/Google/PythonScripts/Scripts/Files/fake.csv"))
            


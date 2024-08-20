from os import listdir
from os.path import isfile, join
import sys

def is_a_type(line):
    return(line[:4] == "void" or line[:3] == "int" or line[:4] == "char")

def add_prototypes(path, file_name, list):
    file = open(path +  file_name, "r")
    lines = file.readlines()
    for i in range(len(lines) - 1):
        if is_a_type(lines[i]) and lines[i+1][0] == "{" and lines[i][:8] != "int\tmain":
            if(lines[i][:3] == "int"):
                lines[i] = lines[i][:3] + "\t" + lines[i][3:]
            list.append(lines[i][:-1] + ";\n")
    file.close()

def parse_input(path, header_file_name):
    if(path[-1] != "/"):
        path += "/"
    if(header_file_name[0] == "/"):
        header_file_name = header_file_name[1:]

def generate_output(path, header_file_name, prototype_list):
    header_file = open(path + header_file_name, "r")
    header_lines = header_file.readlines()
    header_file.close()

    i = 0
    while i < (len(header_lines)):
        if(is_a_type(header_lines[i])):
            header_lines.pop(i)
            i = i-1
        i += 1

    return header_lines[:-2] + prototype_list + header_lines[-2:]

def main():
    if len(sys.argv) != 3:
        path = input("Enter project path\n")
        header_file_name = input("Enter header file location inside directory (folder/header.h)\n")
    else:
        path = sys.argv[1]
        header_file_name = sys.argv[2]

    parse_input(path,header_file_name)

    file_in_directory = [f for f in listdir(path) if isfile(join(path, f))]
    prototype_list = []

    for file in file_in_directory:
        if file[-2:] == ".c":
            add_prototypes(path, file, prototype_list)

    new_header = generate_output(path,header_file_name, prototype_list)

    header_file = open(path + header_file_name, "w")
    header_file.write("".join(new_header))
    header_file.close()

    print("Success!")

if __name__ == "__main__":
    main()

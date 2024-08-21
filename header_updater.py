from os import listdir
from os.path import isfile, join
import sys

def is_a_type(line):
    return(line[0] != "#" and line[0] != "\t" and line[0] != "}" and line[0] != "{" and line[:7] != "typedef" and line[0] != "\n")

def add_prototypes(path, file_name, list):
    file = open(path +  file_name, "r")
    lines = file.readlines()
    for i in range(len(lines) - 1):
        if is_a_type(lines[i]) and lines[i+1][0] == "{" and lines[i][:8] != "int\tmain":
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
    while i < len(header_lines):
        if(is_a_type(header_lines[i])):
            header_lines.pop(i)
            i = i-1
        i += 1
    return header_lines[:-1] + prototype_list + header_lines[-1:]

def find_longest_type(prototype_list):
    max_len = 0
    for proto in prototype_list:
        max_len = max(len(proto.split("\t")[0]), max_len)
    return(max_len//4 + 1)

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

    tab_number = find_longest_type(prototype_list)
    
    for i in range(len(prototype_list)):
        prototype_list[i] = prototype_list[i].split("\t")[0] + "\t" * (tab_number - len(prototype_list[i].split("\t")[0])//4) + prototype_list[i].split("\t")[-1]
    new_header = generate_output(path,header_file_name, prototype_list)

    header_file = open(path + header_file_name, "w")
    header_file.write("".join(new_header))
    header_file.close()

if __name__ == "__main__":
    main()

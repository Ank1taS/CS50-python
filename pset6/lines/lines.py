# python run.py file.py 22 3
# total argumments : 4
# argv[0] : run.py

import sys

def main():
    #  check command line argv
    check_command_line_argv()

    # open file
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    # if file does not exists
    except FileNotFoundError:
        sys.exit("File does not exist")

    # initial count of valid lines
    count = 0

    # loop through files and checks if starts with # or newline
    for line in lines:
        if not check_comment_newLine(line):
            count += 1

    print(count)
    
def check_comment_newLine(line):
    if line.isspace():
        # isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
        return True    # false - line not to be count
    
    if line.lstrip().startswith("#"):
        # lstrip - there might ve spaces before comments like the corrent one
        return True
    return False

# function to check command line argv
def check_command_line_argv():
    # check numbers of arguments in commandline
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # check if it is a python file
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
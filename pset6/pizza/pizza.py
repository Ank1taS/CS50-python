
import sys
import csv
from tabulate import tabulate 

def main():
    #  check command line argv
    check_command_line_argv()
    table = []

    # open file
    try:
        with open(sys.argv[1], "r") as csv_file:
            # reading the CSV file
            items = csv.reader(csv_file)                
            for lines in items:
                table.append(lines)
    # if file does not exists
    except FileNotFoundError:
        sys.exit("File does not exist")

    # print(item_dic)
    
    # for line in item_dic:
    print(tabulate(table, headers = "firstrow", tablefmt="grid"))

# function to check command line argv
def check_command_line_argv():
    # check numbers of arguments in commandline
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # check if it is a python file
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
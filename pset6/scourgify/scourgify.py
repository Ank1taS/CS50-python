import sys
import csv


def main():
    # ckeck valid command line argument 
    check_command_line_argv()
    output = []

    # try to open file 
    try:
        # read input file
        with open(sys.argv[1], "r") as in_file:
            reader = csv.DictReader(in_file)
            # split_name : list of list contaning last and first name
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].strip(), "last": split_name[0].strip(), "house": row["house"]})
        
    # if could not open file, file does not exists
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    
    # write output file
    with open(sys.argv[2], "w") as out_file:
        writer = csv.DictWriter(out_file, fieldnames= ["first", "last", "house"])

        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
            


def check_command_line_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()

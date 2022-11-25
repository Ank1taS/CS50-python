import os
import sys
from PIL import Image
from PIL import ImageOps


def main():
    check_command_line_argv()

    try:
        # oprn input image file
        input_image = Image.open(sys.argv[1], mode='r', formats=None)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    #  opeen shirt
    shirt = Image.open("shirt.png")

    # get size of the shirt
    size = shirt.size

    # resize input file to fit shirt in it
    muppet = ImageOps.fit(input_image, size)

    # paste shirt in muppet
    muppet.paste(shirt, shirt)

    # output image
    muppet.save(sys.argv[2])



def check_command_line_argv():
    # check commandline argunment numbers
    # if the user does not specify exactly two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # check extensions
    infile_extension = sys.argv[1] [sys.argv[1].index("."): ]
    outfile_extension = sys.argv[2] [sys.argv[2].index("."): ]

    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if infile_extension != ".png" and infile_extension != ".jpeg" and infile_extension != ".jpg":
        sys.exit("Invalid output")
    
    # if the input’s name does not have the same extension as the output’s name,
    if infile_extension != outfile_extension:
        sys.exit("Input and output have different extensions")
    


if __name__ == "__main__":
    main()
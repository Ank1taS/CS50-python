# implement a program that:
# Expects zero or two command-line arguments:
#   Zero if the user would like to output text in a random font.
#   Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
#   Prompts the user for a str of text.
#   Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

# from pyfiglet import Figlet
import pyfiglet
import sys
from random import choice

def main():
    
    length = len(sys.argv)
    
    try:    
        # validate numbers of argument in commandline
        if length != 1 and length != 3:
            raise ValueError

        # retive list of font
        figletFonts = pyfiglet.FigletFont.getFonts()
        
        if length == 1:
            # choose random font if not specified by user
            fontSelect = choice(figletFonts)
        else:
            # validate commadline arg
            # checks valid flags 
            # checks supplied font is a valid font of Figlet
            if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in figletFonts:
                raise ValueError
            
            # extract font from command line
            fontSelect = sys.argv[2]

    except ValueError:
        sys.exit("Invalid usage")

    else:
        text = input("Input: ")

        # apply selected font over text
        font = pyfiglet.Figlet(font = fontSelect)
        print(font.renderText(text))


if __name__ == "__main__":
    main()

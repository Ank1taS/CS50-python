# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
# Otherwise output No.


def main():
    ans = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if isValid(ans):
        print("Yes")
    else:
        print("No")

def isValid(ans):
    # convert ans to lower case
    ans = ans.lower()

    # remove space if any
    if " " in ans:
        ans = ans.replace(" ", "")

    # remove - if any
    if "-" in ans:
        ans = ans.replace("-", "")

    if ans == "42" or ans == "fortytwo":
        return True
    else:
        return False

main()
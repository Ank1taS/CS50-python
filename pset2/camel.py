# implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.


def main():
    camelCase = input("camelCase: ")


    # iterate through each character of string
    for letter in camelCase:
        # if a upper case letter is found then print "_" and then print letter in lowercase
        if letter.isupper():
            print("_" + letter.lower(), end="")
        # otherewise print letter as it is
        else:
            print(letter, end="")
    print()


if __name__ == "__main__":
    main()

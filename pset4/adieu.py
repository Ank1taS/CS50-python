#  implement a program that prompts the user for names, one per line, until the user inputs control-d. 
#  Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, 
#  three names with two commas and one and, and N names with N-1 commas and one and, as in the below:

import inflect

def main():
    # empty list to store users name
    usersList = []

    # read users name from promt
    while True:
        try:
            name = input("Name: ")
            usersList.append(name)
        except EOFError:
            break

    #  JOIN WORDS INTO A LIST
    p = inflect.engine()
    users = p.join(usersList)
    
    # print Aideu massage
    print("Adieu, adieu, to", users)

if __name__ == "__main__":
    main()

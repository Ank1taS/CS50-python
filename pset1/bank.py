# implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting.
# treat the user’s greeting case-insensitively.


def main():
    str = input("Greeting: ")
    pay = payAmount(str)
    print("$", pay, sep="")

def payAmount(str):
    # stip leading space
    str = str.lstrip() 

    # covert str to lower case
    str = str.lower()
    
    # strip first 5 words 
    str = str[0:5]
     
    # if str = hello no payment
    if (str == "hello"):
        return 0

    # slice string
    str = str[0:1]
    
    if (str == "h"):
        return 20
    else:
        return 100


main()



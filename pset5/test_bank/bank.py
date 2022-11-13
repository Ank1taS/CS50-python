
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
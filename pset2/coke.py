#  implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
#  Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
#  Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


def main():
    dueAmount = 50
    while dueAmount > 0:
        print("Amount Due:", dueAmount)

        paidAmount = int(input("Insert coin: "))

        if paidAmount > dueAmount:
            # got a tip
            dueAmount = paidAmount - dueAmount
            break
        elif paidAmount == 25:
            dueAmount -= 25
        elif paidAmount == 10:
            dueAmount -= 10
        elif paidAmount == 5:
            dueAmount -= 5


    print("Change Owed:", dueAmount)

if __name__ == "__main__":
    main()

